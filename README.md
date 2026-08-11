<div align="center">
  <h1>🎙️ Voxa</h1>
  <p><strong>Keep the voice. Lift out the music.</strong></p>
  <p>An AI-powered application that isolates vocals from any audio or video file.</p>
</div>

---


## 🌟 About The Project

Voxa is a sophisticated audio processing tool wrapped in a sleek, premium, dark-mode user interface. Built with Python and Flask, it leverages Meta's state-of-the-art **Demucs** deep learning model to perform high-quality audio source separation. 

Whether you upload an MP3 song or an MP4 video clip, Vocalizer intelligently strips away the instrumental backing tracks and returns a crystal-clear file containing only the isolated human vocals.

### ✨ Key Features
- **Unrivaled AI Separation:** Uses PyTorch and the Demucs model for industry-leading vocal extraction.
- **Video & Audio Support:** Seamlessly handles `.mp3`, `.wav`, `.flac`, `.mp4`, `.mkv`, and more. If a video is uploaded, it extracts the audio, processes it, and stitches the isolated vocals back onto the original video file.
- **Premium UI/UX:** A gorgeous, responsive, glass-inspired dark theme with drag-and-drop file support and dynamic loading states.
- **Integrated Feedback:** Built-in form submission for collecting user feedback directly to your inbox.

---

## 🛠️ Tech Stack

- **Frontend:** HTML5, Vanilla CSS (Custom Design System), JavaScript
- **Backend:** Python 3, Flask, Gunicorn
- **AI & Processing:** PyTorch, Meta's Demucs API, FFmpeg

---

## 🚀 Getting Started Locally

Because this application runs heavy machine learning models, it is designed to be run locally or hosted on a dedicated server with sufficient RAM (4GB+ recommended).

### Prerequisites
1. **Python 3.9+** installed on your machine.
2. **FFmpeg** installed and accessible in your system's PATH.
   - *Ubuntu/Debian:* `sudo apt install ffmpeg`
   - *Mac:* `brew install ffmpeg`
   - *Windows:* Download via `winget install ffmpeg`

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/HassanKorey/Voxa.git
   cd Audio Filterer
   ```

2. **Create a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```
   
5. **Open your browser** and navigate to `http://127.0.0.1:7860`. Drag and drop an audio file to see the magic happen!


## 📜 Acknowledgements
- [Demucs by Meta Research](https://github.com/facebookresearch/demucs) - The incredible AI model powering the audio separation.
- [FormSubmit](https://formsubmit.co/) - Handling the frontend feedback form.

---
<div align="center">
  <i>Designed and Built by HassanKorey © 2026</i>
</div>
