"""
main.py — Combined menu for the mini STT/TTS project.
Run this file to try speech-to-text or text-to-speech interactively.
"""
from speech_to_text import record_and_transcribe, transcribe_wav_file
from text_to_speech import speak_with_gtts, speak_with_pyttsx3


def main():
    while True:
        print("\n=== Mini Voice Assistant ===")
        print("1. Speech to Text (record from mic)")
        print("2. Speech to Text (from .wav file)")
        print("3. Text to Speech (gTTS - online)")
        print("4. Text to Speech (pyttsx3 - offline)")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            record_and_transcribe()
        elif choice == "2":
            path = input("Enter path to .wav file: ").strip()
            transcribe_wav_file(path)
        elif choice == "3":
            text = input("Enter text: ").strip()
            speak_with_gtts(text)
        elif choice == "4":
            text = input("Enter text: ").strip()
            speak_with_pyttsx3(text)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
