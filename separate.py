import os
from demucs.api import Separator 



def extract_vocals(audio_file):
    if not os.path.exists(audio_file):
        raise FileNotFoundError(f"Input File Not Found: {audio_file}")
    separator = Separator()  # capital S = the class; () creates an instance with default settings
    origin, separated = separator.separate_audio_file(audio_file)
    # separated is a dict: {"vocals": tensor, "drums": tensor, "bass": tensor, "other": tensor}
    vocals = separated["vocals"]
    return vocals, separator.samplerate

import subprocess

def extract_audio_from_video(video_file, audio_output):
    subprocess.run([
        "ffmpeg", "-i", video_file,
        "-vn", "-acodec", "pcm_s16le", "-ar", "44100",
        audio_output
    ])
    return audio_output

if __name__ == "__main__":
    import sys
    from demucs.api import save_audio
    if len(sys.argv) < 2:
        print("Usage: python3 separate.py <audio_file>")
        sys.exit(1)
    
    
    input_file = sys.argv[1]  # takes filename from command line, e.g. python separate.py test.mp3

    if os.path.splitext(os.path.basename(input_file))[1] in [".mp3", ".wav",".flac", ".m4a", ".ogg"]:
        vocals, samplerate = extract_vocals(input_file)
        name = os.path.splitext(os.path.basename(input_file))[0]
        save_audio(vocals, name+"_Vocals.wav", samplerate)
        print(f"Saved vocals to: {name}_Vocals.wav")

    # Check if the file is a video
    elif os.path.splitext(os.path.basename(input_file))[1] in [".mp4",".avi",".mkv",".webm"]:
        vidname = os.path.splitext(os.path.basename(input_file))[0]
        audio_output = vidname + "_Audio.wav"
        output = extract_audio_from_video(input_file, audio_output)
        vocals,samplerate = extract_vocals(output)
        os.remove(output)
        output_name = vidname + "_vocals.wav"
        save_audio(vocals,output_name,samplerate)
        print(f"saved vocals as {output_name}")
    else:
        print("NOT A VIDEO/AUDIO FILE")