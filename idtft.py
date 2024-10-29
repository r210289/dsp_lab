import numpy as np
import matplotlib.pyplot as plt

def idtft(X):
    N = len(X)
    n = np.arange(N)
    k = np.arange(N)
    exp_term = np.exp(1j * 2 * np.pi * np.outer(n, k) / N)
    x = np.dot(exp_term, X) / N
    return x

# Example frequency-domain signal
X = np.array([1, 2, 3, 4], dtype=complex)

# Compute the inverse DFT
x = idtft(X)
print(x)
# Plot the time-domain signal
markerline, stemlines, baseline = plt.stem(np.real(x))
plt.title('Inverse Discrete Time Fourier Transform')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


