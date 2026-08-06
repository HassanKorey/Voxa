from flask import Flask, request
from separate import extract_vocals, extract_audio_from_video, add_audio_to_video, save_audio
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Vocal isolation API is running"

@app.route("/separate", methods=["POST"])
def separate():
    if "file" not in request.files:
        return "No file uploaded\n", 400
    
    uploaded_file = request.files["file"]
    uploaded_file.save(uploaded_file.filename)
    if os.path.splitext(os.path.basename(uploaded_file.filename))[1] in [".mp3", ".wav",".flac", ".m4a", ".ogg"]:
        audio_vocals, samplerate = extract_vocals(uploaded_file.filename)
        save_audio(audio_vocals, uploaded_file.filename + "_vocals.wav", samplerate)
        return f"Received file: {uploaded_file.filename}\n"
    elif os.path.splitext(os.path.basename(uploaded_file.filename))[1] in [".mp4",".avi",".mkv",".webm"]:
        vidname = os.path.splitext(os.path.basename(uploaded_file.filename))[0]
        audio_output = vidname + ".wav"
        video_audio = extract_audio_from_video(uploaded_file.filename, audio_output)
        video_vocals, samplerate = extract_vocals(video_audio)
        vocals_output_name = uploaded_file.filename + "_vocals.wav"
        save_audio(video_vocals, vocals_output_name, samplerate)
        os.remove(audio_output)
        video_output = add_audio_to_video(uploaded_file.filename, vocals_output_name, vidname + "_vocals.mp4")
    return f"Received file: {uploaded_file.filename}\n"

if __name__ == "__main__":
    app.run(debug=True)