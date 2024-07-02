import sounddevice as sd
import wavio
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import threading

# Global variables
is_recording = False
recording = None
sample_rate = 44100
filename = "recorded_audio.wav"

def start_recording(duration):
    global is_recording, recording
    if not is_recording:
        is_recording = True
        recording_indicator.config(text="Recording...", fg="red")
        recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
        sd.wait()
        recording_indicator.config(text="")
        messagebox.showinfo("Info", "Recording started")

def stop_recording():
    global is_recording
    if is_recording:
        sd.stop()
        is_recording = False
        wavio.write(filename, recording, sample_rate, sampwidth=2)
        messagebox.showinfo("Info", f"Recording stopped and saved as {filename}")

def play_audio():
    try:
        audio_data = wavio.read(filename)
        sd.play(audio_data.data, audio_data.rate)
        sd.wait()
        messagebox.showinfo("Info", "Playback finished")
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found. Please record audio first.")

def record_thread():
    global filename
    duration = simpledialog.askinteger("Input", "Enter recording duration (seconds):", minvalue=1, maxvalue=600)
    if duration:
        filename = simpledialog.askstring("Input", "Enter file name (without extension):") + ".wav"
        if filename:
            record_button.config(state="disabled")
            stop_button.config(state="normal")
            play_button.config(state="disabled")
            threading.Thread(target=start_recording, args=(duration,)).start()

def stop_thread():
    stop_button.config(state="disabled")
    record_button.config(state="normal")
    play_button.config(state="normal")
    threading.Thread(target=stop_recording).start()

# Create GUI window
root = tk.Tk()
root.title("Voice Recorder")
root.geometry("350x250")
root.config(bg="#f0f0f0")

# Create buttons
record_button = tk.Button(root, text="Record", command=record_thread, width=20, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
record_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_thread, state="disabled", width=20, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
stop_button.pack(pady=10)

play_button = tk.Button(root, text="Play", command=play_audio, state="disabled", width=20, bg="#2196F3", fg="white", font=("Arial", 12, "bold"))
play_button.pack(pady=10)

# Recording indicator
recording_indicator = tk.Label(root, text="", fg="red", bg="#f0f0f0", font=("Arial", 12, "bold"))
recording_indicator.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
