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

if __name__ == "__main__":
    import sys
    from demucs.api import save_audio

    audio_file = sys.argv[1]  # takes filename from command line, e.g. python separate.py test.mp3
    vocals, samplerate = extract_vocals(audio_file)
    name = os.path.splitext(os.path.basename(audio_file))[0]
    save_audio(vocals, name+"_Vocals.wav", samplerate)
    print(f"Saved vocals to: {name}_Vocals.wav")