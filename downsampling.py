import numpy as np

# Create a sample signal
t = np.linspace(0, 1, 1000)  # Time vector
signal = np.sin(2 * np.pi * 5 * t)  # Example signal

# Downsample the signal
downsample_factor = 10
signal_downsampled = signal[::downsample_factor]

# For better visualization, you can use matplotlib
import matplotlib.pyplot as plt

plt.plot(t, signal, label='Original Signal')
plt.plot(t[::downsample_factor], signal_downsampled, label='Downsampled Signal', marker='o')
plt.legend()
plt.show()

