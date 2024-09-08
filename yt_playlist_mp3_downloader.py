import os
import subprocess

def download_playlist_to_mp3(playlist_url, download_folder):
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Download entire playlist as mp3 using yt-dlp
    print(f"Downloading playlist from: {playlist_url}")
    
    # yt-dlp command to download and convert to mp3
    subprocess.run([
        'yt-dlp', '-x', '--audio-format', 'mp3',
        '-o', os.path.join(download_folder, '%(title)s.%(ext)s'),
        playlist_url
    ])

if __name__ == "__main__":
    # Playlist URL and download folder
    playlist_url = "https://youtube.com/playlist?list=PLlP1XFFAc1ODcFHfp-H5GjKs9v-l7W5SW&si=XxSaP35vUB-JaaJa"
    download_folder = r"C:\Users\Emmanuel_Kgaphola\Downloads\House"

    # Run the function to download the playlist
    download_playlist_to_mp3(playlist_url, download_folder)
    print("Download and conversion complete!")
