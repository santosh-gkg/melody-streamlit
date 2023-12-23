from pydub import AudioSegment

# Load the audio files
vocals = AudioSegment.from_file("vocal.wav")
background_music = AudioSegment.from_file("background.wav")

# Ensure that both audio files have the same duration
min_length = min(len(vocals), len(background_music))
vocals = vocals[:min_length]
background_music = background_music[:min_length]

# Combine the audio files
combined_audio = vocals.overlay(background_music)

# Export the combined audio to a new file
combined_audio.export("combined_song.mp3", format="mp3")
