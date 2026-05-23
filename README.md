# yt-playlist-to-mp3

A Python script that downloads all videos in a YouTube playlist and converts them to MP3 format using `yt-dlp` and `ffmpeg`. This script helps you easily manage and store audio content from YouTube playlists.

## **Features**
- Download entire YouTube playlists as MP3 files.
- Automatically converts video to MP3 using `yt-dlp`.
- Saves MP3 files to a user-defined folder.
- Simple setup with minimal dependencies.

## **Requirements**
- Python 3.x
- `yt-dlp` (for downloading and conversion)
- `ffmpeg` (for converting video to audio)

## **Installation**

1. Clone the repository
2. Install the required dependencies:

    ```bash
    pip install yt-dlp
    ```

3. Install `ffmpeg`:
    - [Download ffmpeg](https://ffmpeg.org/download.html) and follow the installation instructions for your OS.
    - Make sure `ffmpeg` is added to your system's PATH.

## **Usage**

You can run the script from the command line instead of editing the file. By default the script now converts audio to `webm` at `64k` bitrate; use the CLI flags below to change format and bitrate.

1. Install Python dependencies:

    ```bash
    pip install -U yt-dlp
    ```

2. Make sure `ffmpeg` is installed and available in your PATH (see https://ffmpeg.org/).

3. Run the script with the playlist URL and optional destination folder:

    ```bash
    python yt_playlist_mp3_downloader.py "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID" -d "C:\Users\YourUser\Downloads\Music"
    ```

4. Use `-t` to customize the output filename template and `-v` to enable verbose logging. Use `-a`/`--audio-format` to choose the audio format and `-b`/`--audio-bitrate` to set the target bitrate.

Example with template and verbose logging:

```bash
python yt_playlist_mp3_downloader.py "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID" -d "./Music" -t "%(playlist_index)s - %(title)s.%(ext)s" -v
```

Convert to WebM at 64k (default):

```bash
python yt_playlist_mp3_downloader.py "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

Convert to MP3 at 320k:

```bash
python yt_playlist_mp3_downloader.py "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID" -a mp3 -b 320k
```

## **Example**

```bash
playlist_url = "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID"
download_folder = r"C:\Users\YourUser\Downloads\Music"
