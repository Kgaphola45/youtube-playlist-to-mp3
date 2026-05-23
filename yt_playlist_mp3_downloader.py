import os
import subprocess
import shutil
import argparse
import logging
import sys


def _check_executable(name):
    return shutil.which(name) is not None


def download_playlist_to_mp3(playlist_url, download_folder, output_template='%(playlist_index)s - %(title)s.%(ext)s'):
    os.makedirs(download_folder, exist_ok=True)

    logging.info("Downloading playlist: %s", playlist_url)

    if not _check_executable('yt-dlp'):
        logging.error("`yt-dlp` not found. Install with: pip install -U yt-dlp")
        raise RuntimeError('yt-dlp not found')

    if not _check_executable('ffmpeg'):
        logging.warning("`ffmpeg` not found in PATH. Conversion may fail. Install ffmpeg from https://ffmpeg.org/")

    cmd = [
        'yt-dlp', '-x', '--audio-format', 'mp3',
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
    parser.add_argument('playlist_url', help='YouTube playlist URL')
    parser.add_argument('-d', '--dest', dest='download_folder', default=os.path.join(os.path.expanduser('~'), 'Downloads', 'Music'),
                        help='Destination folder for downloaded MP3s (default: ~/Downloads/Music)')
    parser.add_argument('-t', '--template', dest='template', default='%(playlist_index)s - %(title)s.%(ext)s',
                        help='Output filename template for yt-dlp (default: "%(playlist_index)s - %(title)s.%(ext)s")')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format='%(levelname)s: %(message)s')

    try:
        download_playlist_to_mp3(args.playlist_url, args.download_folder, args.template)
    except Exception as exc:
        logging.error("Failed: %s", exc)
        sys.exit(1)

    logging.info("Download and conversion complete!")


if __name__ == '__main__':
    main()
