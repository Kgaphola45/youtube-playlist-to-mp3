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

1. Update the `playlist_url` and `download_folder` in the script, or you can directly pass them as input arguments.
2. Run the script:

    ```bash
    python yt_playlist_to_mp3.py
    ```

3. The MP3 files will be saved in the specified folder.

## **Example**

```bash
playlist_url = "https://youtube.com/playlist?list=YOUR_PLAYLIST_ID"
download_folder = r"C:\Users\YourUser\Downloads\Music"
