# to run this code you will need to install matplotlib and sounddevice
# pip install matplotlib sounddevice 

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# Sine wave parameters
duration = 2.0  # seconds
phase = 0  # radians
a1 = 1.0 
a2 = 0.5
a3 = 0.25
f1 = 440.0  # Hz
f2 = 880.0  # Hz
f3 = 1320.0  # Hz

# Sound duration in samples
sample_rate = 22050  # samples per second
duration_in_samples = int(duration * sample_rate)

# Generate time values
t = np.linspace(0, duration, duration_in_samples)

# Generate the sine wave
y1 = a1 * np.sin(2 * np.pi * f1 * t - phase)
y2 = a2 * np.sin(2 * np.pi * f2 * t - phase)
y3 = a3 * np.sin(2 * np.pi * f3 * t - phase)
y = y1 + y2 + y3

# Play the audio signal using sounddevice
sd.play(y, sample_rate)
sd.wait()  # Wait until the sound has finished playing


# Create a multiplot
fig, axs = plt.subplots(4, 1, figsize=(10, 8))

# Plot y1
plot_split = 200 # Plot the first 1000 samples for visualization

axs[0].plot(t[:plot_split], y1[:plot_split])
axs[0].set_title(f'Sine Wave at {f1} Hz')
axs[0].set_xlabel('Time [s]')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)
axs[0].set_ylim(-1.5, 1.5)  

# Plot y2
axs[1].plot(t[:plot_split], y2[:plot_split])
axs[1].set_title(f'Sine Wave at {f2} Hz')
axs[1].set_xlabel('Time [s]')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)
axs[1].set_ylim(-1.5, 1.5)  

# Plot y3
axs[2].plot(t[:plot_split], y3[:plot_split])
axs[2].set_title(f'Sine Wave at {f3} Hz')
axs[2].set_xlabel('Time [s]')
axs[2].set_ylabel('Amplitude')
axs[2].grid(True)
axs[2].set_ylim(-1.5, 1.5)  

# Plot the complex wave
axs[3].plot(t[:plot_split], y[:plot_split])
axs[3].set_title(f'Complex Wave with {f1} Hz, {f2} Hz, and {f3} Hz')
axs[3].set_xlabel('Time [s]')
axs[3].set_ylabel('Amplitude')
axs[3].grid(True)
axs[3].set_ylim(-1.5, 1.5)  

# Adjust layout
plt.tight_layout()
plt.show()