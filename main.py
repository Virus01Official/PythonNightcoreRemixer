import os
from pytube import YouTube
from pydub import AudioSegment

def create_nightcore(input_file, output_file, speed_factor=1.35, pitch_factor=5):
    # Load the input audio file
    audio = AudioSegment.from_file(input_file)

    # Speed up the audio (adjust tempo)
    faster_audio = audio.speedup(playback_speed=speed_factor)

    # Increase the pitch (higher frequency)
    pitched_audio = faster_audio.set_frame_rate(int(audio.frame_rate * pitch_factor))

    # Export the Nightcore remix
    pitched_audio.export(output_file, format="mp3")

def download_and_create_nightcore(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        filename = f"{yt.title}.mp3"
        video.download(filename=filename)
        output_filename = f"nightcore_{yt.title}.mp3"
        create_nightcore(filename, output_filename)
        print(f"Nightcore remix complete: {output_filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Replace with the URL of the YouTube video you want to create a Nightcore remix of
url = input("Paste a youtube link for a video you want to remix ")
download_and_create_nightcore(url)
