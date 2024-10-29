

import numpy as np
from scipy.signal import upsample
import matplotlib.pyplot as plt

# Original signal
t = np.arange(0, 1, 0.01)
x = np.sin(2 * np.pi * 10 * t)

# Upsample by factor of 4
x_upsampled = np.zeros(len(x) * 4)
x_upsampled[::4] = x

# Alternatively, use scipy.signal.upsample
x_upsampled_scipy = upsample(x, 4)

# Plot original and upsampled signals
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(122)
plt.plot(np.arange(len(x_upsampled)) / 4 / 100, x_upsampled)
plt.title('Upsampled Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
