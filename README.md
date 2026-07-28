# Mini Voice Assistant — STT + TTS

A small Python project demonstrating:
- Speech-to-Text (STT): microphone or .wav file to text, using Google's free Speech Recognition API (via the SpeechRecognition library)
- Text-to-Speech (TTS): text to speech, using either gTTS (online, saves an mp3) or pyttsx3 (fully offline)

## Files
- speech_to_text.py — record from mic or transcribe a .wav file
- text_to_speech.py — convert text to speech (gTTS or pyttsx3)
- main.py — combined interactive menu tying both together
- requirements.txt — dependencies

## Setup

    pip install -r requirements.txt

### Note on pyaudio (needed for microphone recording)
pyaudio can be tricky to install directly on some systems.

Windows: if pip install pyaudio fails, run:

    pip install pipwin
    pipwin install pyaudio

Mac: install portaudio first, then pyaudio:

    brew install portaudio
    pip install pyaudio

Linux:

    sudo apt-get install portaudio19-dev python3-pyaudio
    pip install pyaudio

## Usage

Run the combined menu:

    python main.py

Or run each script individually:

    python speech_to_text.py
    python text_to_speech.py

## How it works

STT — speech_recognition captures audio (from mic or file) and sends it to Google's public Speech Recognition API, which returns the transcribed text. No API key needed for basic use, but it requires an internet connection.

TTS — gTTS sends text to Google's Text-to-Speech service and returns an mp3 file (needs internet). pyttsx3 uses your operating system's built-in speech engine, works fully offline, and speaks immediately without saving a file.

## Notes
- Recording requires a working microphone and system permissions to access it.
- gTTS requires internet access; pyttsx3 does not.
