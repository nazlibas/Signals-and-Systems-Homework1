import numpy as np
import matplotlib.pyplot as plt

# Frequencies
f0 = 82
f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# Sampling frequency
fs = 5000

# Time vector
t = np.arange(0, 0.1, 1/fs)

# Signals
x1 = np.sin(2 * np.pi * f1 * t)
x2 = np.sin(2 * np.pi * f2 * t)
x3 = np.sin(2 * np.pi * f3 * t)

# Sum signal
x_sum = x1 + x2 + x3

# Plotting
plt.figure(figsize=(10,8))

plt.subplot(4,1,1)
plt.plot(t, x1)
plt.title("x1(t) = sin(2π82t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,2)
plt.plot(t, x2)
plt.title("x2(t) = sin(2π41t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,3)
plt.plot(t, x3)
plt.title("x3(t) = sin(2π820t)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(4,1,4)
plt.plot(t, x_sum)
plt.title("Sum Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.tight_layout()
plt.show()
