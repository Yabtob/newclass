# Text to Speech GUI (Python)

This project is a simple Text-to-Speech (TTS) application with a graphical user interface (GUI) built using Python's `tkinter`, `gtts`, and `pygame` libraries. It allows you to enter any text, click "Speak", and hear the text spoken aloud.

## Features

- Enter long or short text in a scrollable text box
- Click "Speak" to convert the text to speech
- Supports multiple uses without restarting the app
- Simple and clean GUI

## Requirements

- Python 3.7+
- [gtts](https://pypi.org/project/gTTS/)
- [pygame](https://pypi.org/project/pygame/)

## Installation

1. **Clone or download this repository.**
2. **Install the required packages:**

   ```
   pip install gtts pygame
   ```

## Usage

1. Run the script:

   ```
   python new.py
   ```

2. Enter your text in the text box.
3. Click the **Speak** button to hear your text spoken aloud.

## How it works

- The text is converted to speech using Google Text-to-Speech (`gtts`).
- The speech is saved as a temporary `.mp3` file.
- `pygame` plays the audio file.
- The temporary file is deleted after playback.

## Notes

- Requires an internet connection for `gtts` to work.
- Works on Windows, macOS, and Linux.

## License

This project is for educational purposes.
