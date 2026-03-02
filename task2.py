import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import tkinter as tk

# Sampling settings
fs = 8000
T = 0.3
t = np.linspace(0, T, int(fs*T), endpoint=False)

# DTMF frequency table
dtmf = {
    "1": (697,1209), "2": (697,1336), "3": (697,1477), "A": (697,1633),
    "4": (770,1209), "5": (770,1336), "6": (770,1477), "B": (770,1633),
    "7": (852,1209), "8": (852,1336), "9": (852,1477), "C": (852,1633),
    "*": (941,1209), "0": (941,1336), "#": (941,1477), "D": (941,1633)
}

def play_tone(key):
    f_low, f_high = dtmf[key]
    
    signal = np.sin(2*np.pi*f_low*t) + np.sin(2*np.pi*f_high*t)
    signal = signal / np.max(np.abs(signal))  # normalize
    
    sd.play(signal, fs)
    
    plt.figure()
    plt.plot(t[:400], signal[:400])  # zoom first part
    plt.title(f"DTMF Signal for {key}")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

# GUI
root = tk.Tk()
root.title("DTMF Keypad")

keys = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

for r in range(4):
    for c in range(4):
        btn = tk.Button(root, text=keys[r][c], width=5, height=2,
                        command=lambda k=keys[r][c]: play_tone(k))
        btn.grid(row=r, column=c)

root.mainloop()
