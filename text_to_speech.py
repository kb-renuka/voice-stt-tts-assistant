"""
text_to_speech.py — Convert text to speech using either:
  1. gTTS (Google Text-to-Speech) — needs internet, saves an .mp3 file
  2. pyttsx3 — works fully offline, speaks directly through your speakers
"""
from gtts import gTTS
import pyttsx3
import os


def speak_with_gtts(text, output_file="output.mp3", lang="en", play_after=True):
    """Converts text to speech using gTTS and saves it as an mp3 file."""
    tts = gTTS(text=text, lang=lang)
    tts.save(output_file)
    print(f"Saved speech to {output_file}")

    if play_after:
        try:
            from playsound import playsound
            playsound(output_file)
        except Exception as e:
            print(f"Could not auto-play the file ({e}). Open {output_file} manually to listen.")


def speak_with_pyttsx3(text, rate=175, volume=1.0):
    """Converts text to speech offline using pyttsx3 and speaks it immediately."""
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    print("=== Text-to-Speech ===")
    print("1. gTTS (online, saves mp3)")
    print("2. pyttsx3 (offline, speaks directly)")
    choice = input("Choose an option (1/2): ").strip()
    text = input("Enter the text to convert to speech: ").strip()

    if choice == "1":
        speak_with_gtts(text)
    elif choice == "2":
        speak_with_pyttsx3(text)
    else:
        print("Invalid choice.")
