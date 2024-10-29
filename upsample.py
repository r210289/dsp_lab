import numpy as np
import matplotlib.pyplot as plt

# Original signal (e.g., a sine wave)
t = np.linspace(0, 1, 10)  # 10 samples
signal = np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave

# Upsampling factor
upsampling_factor = 5

# Upsample the signal
upsampled_signal = np.repeat(signal, upsampling_factor)

# Create new time array for the upsampled signal
upsampled_t = np.linspace(0, 1, len(upsampled_signal))

# Plot the original and upsampled signals
plt.figure(figsize=(10, 6))
plt.plot(t, signal, 'o-', label='Original Signal (10 samples)')
plt.plot(upsampled_t, upsampled_signal, 'x-', label='Upsampled Signal (50 samples)')
plt.title('Signal Upsampling')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

