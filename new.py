import io
import tkinter as tk
from tkinter import scrolledtext, messagebox
import pygame
from gtts import gTTS
import os
import tempfile

# Initialize pygame mixer ONCE
pygame.mixer.init()

def speak(text):
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text.")
        return
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmpfile:
        gTTS(text, lang='en').write_to_fp(tmpfile)
        tmpfile_path = tmpfile.name

    # Stop any currently playing audio
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

    pygame.mixer.music.load(tmpfile_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        root.update()  # Keep the GUI responsive

    os.remove(tmpfile_path)

def on_speak():
    text = text_area.get("1.0", tk.END)
    speak(text)

# GUI setup
root = tk.Tk()
root.title("Text to Speech")

tk.Label(root, text="Enter text to speak:").pack(pady=5)
text_area = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_area.pack(padx=10, pady=5)

speak_btn = tk.Button(root, text="Speak", command=on_speak)
speak_btn.pack(pady=10)

root.mainloop()