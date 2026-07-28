"""
speech_to_text.py — Record audio from the microphone and convert it to text
using Google's free Speech Recognition API (via the SpeechRecognition library).

Also supports transcribing an existing .wav file instead of recording live.
"""
import speech_recognition as sr


def record_and_transcribe(timeout=5, phrase_time_limit=15):
    """
    Records audio from the default microphone and transcribes it.
    - timeout: seconds to wait for speech to start before giving up
    - phrase_time_limit: max seconds to record once speech starts
    Returns the transcribed text, or None if recognition failed.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise... please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... speak now.")
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout period.")
            return None

    return _transcribe_audio(recognizer, audio)


def transcribe_wav_file(file_path):
    """Transcribes an existing .wav audio file instead of recording live."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    return _transcribe_audio(recognizer, audio)


def _transcribe_audio(recognizer, audio):
    """Shared helper: sends audio to Google's Speech Recognition API."""
    try:
        text = recognizer.recognize_google(audio)
        print(f"Transcribed text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech API; {e}")
    return None


if __name__ == "__main__":
    print("=== Speech-to-Text (Google Speech API) ===")
    print("1. Record from microphone")
    print("2. Transcribe an existing .wav file")
    choice = input("Choose an option (1/2): ").strip()

    if choice == "1":
        record_and_transcribe()
    elif choice == "2":
        path = input("Enter path to .wav file: ").strip()
        transcribe_wav_file(path)
    else:
        print("Invalid choice.")
