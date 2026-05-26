from pytube import Playlist
from pytube import YouTube
import os

# Download single video

input_message = """
Choose what you want to download:
"s" => Single video
"a" => Audio
"l" => Playlist
"""

user_input = input(input_message).strip().lower()

commands_list = ["s", "a", "l"]

def finish():
    print("Download completed!")

def ensure_download_dir():
    download_dir = os.path.expanduser("~/Downloads/Video")
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir

def download_single_video():
    try:
        link = input("Please enter the video URL: ").strip()
        video = YouTube(link)
        print(f"The video duration is: {video.length/60:.2f} minutes\n-------------------")
        download_dir = ensure_download_dir()
        video.streams.get_highest_resolution().download(output_path=download_dir)
        video.register_on_complete_callback(finish)
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_audio():
    try:
        link = input("Please enter the video URL: ").strip()
        audio = YouTube(link)
        print(f"The audio duration is: {audio.length/60:.2f} minutes\n-------------------")
        download_dir = ensure_download_dir()
        audio.streams.get_audio_only().download(output_path=download_dir)
        audio.register_on_complete_callback(finish)
    except Exception as e:
        print(f"Error downloading audio: {e}")

def download_playlist():
    try:
        play_list_link = input("Please enter the playlist URL: ").strip()
        playlist = Playlist(play_list_link)
        download_dir = ensure_download_dir()

        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path=download_dir)

        finish()
    except Exception as e:
        print(f"Error downloading playlist: {e}")

if user_input in commands_list:
    print(f'Command found "{user_input}"')

    if user_input == "s":
        download_single_video()
    elif user_input == "a":
        download_audio()
    elif user_input == "l":
        download_playlist()
else:
    print(f'Sorry, this command "{user_input}" is not found')
