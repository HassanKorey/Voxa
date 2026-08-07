from flask import Flask, request, send_file, render_template
from separate import extract_vocals, extract_audio_from_video, add_audio_to_video, save_audio
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/separate", methods=["POST"])
def separate():
    if "file" not in request.files:
        return "No file uploaded\n", 400
    
    uploaded_file = request.files["file"]
    uploaded_file.save(uploaded_file.filename)
    if os.path.splitext(os.path.basename(uploaded_file.filename))[1] in [".mp3", ".wav",".flac", ".m4a", ".ogg"]:
        audio_vocals, samplerate = extract_vocals(uploaded_file.filename)
        name = os.path.splitext(os.path.basename(uploaded_file.filename))[0]
        vocals_output_name = name + "_vocals.wav"
        save_audio(audio_vocals,vocals_output_name , samplerate)
        response = send_file(vocals_output_name, as_attachment=True)
        os.remove(vocals_output_name)
        os.remove(uploaded_file.filename)
        return response
    elif os.path.splitext(os.path.basename(uploaded_file.filename))[1] in [".mp4",".avi",".mkv",".webm"]:
        vidname = os.path.splitext(os.path.basename(uploaded_file.filename))[0]
        audio_output = vidname + ".wav"
        video_audio = extract_audio_from_video(uploaded_file.filename, audio_output)
        video_vocals, samplerate = extract_vocals(video_audio)
        vocals_output_name = vidname + "_vocals.wav"
        save_audio(video_vocals, vocals_output_name, samplerate)
        os.remove(audio_output)
        video_output = add_audio_to_video(uploaded_file.filename, vocals_output_name, vidname + "_vocals.mp4")
        response = send_file(video_output, as_attachment=True)
        os.remove(vocals_output_name)
        os.remove(video_output)
        os.remove(uploaded_file.filename)
        return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)