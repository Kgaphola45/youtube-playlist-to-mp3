import os
import subprocess
import shutil
import argparse
import logging
import sys


def _check_executable(name):
    return shutil.which(name) is not None


def _resolve_yt_dlp_cmd():
    exe = shutil.which('yt-dlp')
    if exe:
        return [exe]

    # Fallback to the active Python environment, e.g. .venv\Scripts\python.exe -m yt_dlp
    try:
        import yt_dlp  # noqa: F401
        return [sys.executable, '-m', 'yt_dlp']
    except ImportError:
        return None


def _ensure_yt_dlp_available():
    cmd = _resolve_yt_dlp_cmd()
    if cmd:
        return cmd

    print("`yt-dlp` is not installed in this environment.")
    answer = input("Install it now with pip? [Y/n]: ").strip().lower()
    if answer not in ('', 'y', 'yes'):
        return None

    install_cmd = [sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp']
    try:
        subprocess.run(install_cmd, check=True)
    except subprocess.CalledProcessError:
        return None

    return _resolve_yt_dlp_cmd()


def _prompt_non_empty(prompt_text, default_value=None):
    while True:
        suffix = f" [{default_value}]" if default_value else ""
        value = input(f"{prompt_text}{suffix}: ").strip()
        if value:
            return value
        if default_value:
            return default_value
        print("Please enter a value.")


def download_playlist_to_mp3(playlist_url, download_folder, output_template='%(playlist_index)s - %(title)s.%(ext)s'):
    os.makedirs(download_folder, exist_ok=True)

    logging.info("Downloading playlist: %s", playlist_url)

    yt_dlp_cmd = _ensure_yt_dlp_available()
    if not yt_dlp_cmd:
        logging.error("`yt-dlp` not found in PATH and Python module `yt_dlp` is not installed.")
        logging.error("Install in your active environment with: %s -m pip install -U yt-dlp", sys.executable)
        raise RuntimeError('yt-dlp not found')

    if not _check_executable('ffmpeg'):
        logging.warning("`ffmpeg` not found in PATH. Conversion may fail. Install ffmpeg from https://ffmpeg.org/")

    cmd = yt_dlp_cmd + [
        '-x', '--audio-format', 'mp3',
        '-o', os.path.join(download_folder, output_template),
        playlist_url
    ]

    logging.debug("Running command: %s", ' '.join(cmd))
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error("yt-dlp failed with exit code %s", e.returncode)
        raise


def main():
    parser = argparse.ArgumentParser(description='Download a YouTube playlist and convert videos to MP3 using yt-dlp')
    parser.add_argument('playlist_url', nargs='?', help='YouTube playlist URL')
    parser.add_argument('-d', '--dest', dest='download_folder', default=os.path.join(os.path.expanduser('~'), 'Downloads', 'Music'),
                        help='Destination folder for downloaded MP3s (default: ~/Downloads/Music)')
    parser.add_argument('-t', '--template', dest='template', default='%(playlist_index)s - %(title)s.%(ext)s',
                        help='Output filename template for yt-dlp (default: "%(playlist_index)s - %(title)s.%(ext)s")')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')

    args = parser.parse_args()

    if not args.playlist_url:
        args.playlist_url = _prompt_non_empty('Enter YouTube playlist URL')

    if '-d' not in sys.argv and '--dest' not in sys.argv:
        args.download_folder = _prompt_non_empty('Enter destination folder path', args.download_folder)

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format='%(levelname)s: %(message)s')

    try:
        download_playlist_to_mp3(args.playlist_url, args.download_folder, args.template)
    except Exception as exc:
        logging.error("Failed: %s", exc)
        sys.exit(1)

    logging.info("Download and conversion complete!")


if __name__ == '__main__':
    main()
