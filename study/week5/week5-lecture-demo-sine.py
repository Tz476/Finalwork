# to run this code you will need to install matplotlib and sounddevice
# pip install matplotlib sounddevice 

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Sine wave parameters
amplitude = 1.0  #
frequency = 440.0  # Hz
duration = 2.0  # seconds
phase = 0  # radians

# Sound duration in samples
sample_rate = 22050  # samples per second
duration_in_samples = int(duration * sample_rate)

# Generate time values
t = np.linspace(0, duration, duration_in_samples)

# Generate the sine wave
y = amplitude * np.sin(2 * np.pi * frequency * t - phase)

# Play the audio signal using sounddevice
sd.play(y, sample_rate)
sd.wait()  # Wait until the sound has finished playing

# Plot the sine wave
plt.plot(t[:1000], y[:1000])  # Plot the first 1000 samples for visualization
plt.title(f'Sine Wave at {frequency} Hz')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.ylim(-1.05, 1.05)  # Set the y-axis limits to -1 and 1
plt.grid(True)
plt.show()