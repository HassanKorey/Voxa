from demucs.api import Separator 



def extract_vocals(audio_file):
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
    save_audio(vocals, "vocals_output.wav", samplerate)
    print("Saved vocals to vocals_output.wav")