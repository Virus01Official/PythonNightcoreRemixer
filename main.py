from pydub import AudioSegment

def create_nightcore(input_file, output_file, speed_factor=1.25, pitch_factor=1.5):
    # Load the input audio file
    audio = AudioSegment.from_file(input_file)

    # Speed up the audio (adjust tempo)
    faster_audio = audio.speedup(playback_speed=speed_factor)

    # Increase the pitch (higher frequency)
    pitched_audio = faster_audio.set_frame_rate(int(audio.frame_rate * pitch_factor))

    # Export the Nightcore remix
    pitched_audio.export(output_file, format="mp3")

# Example usage
input_music_file = "audio.mp3"
output_nightcore_file = "nightcore_remix.mp3"
print("Creating Nightcore Remix...")
create_nightcore(input_music_file, output_nightcore_file)

print(f"Nightcore remix saved as {output_nightcore_file}")
