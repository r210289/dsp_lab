import numpy as np
import matplotlib.pyplot as plt

# Define time array
t = np.arange(-10, 11, 1)

# Define signal x(t)
x = np.exp(-np.abs(t))

# Calculate Fourier Transform of x(t)
X = np.fft.fftshift(np.fft.fft(x))

# Define frequency array
f = np.fft.fftshift(np.fft.fftfreq(len(t), d=1))

# Plot x(t) and X(f)
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.plot(t, x)
plt.title('x(t)')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(122)
plt.plot(f, np.abs(X))
plt.title('X(f)')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
