from dorothy import Dorothy 
import librosa
from util import draw_bars
import numpy as np

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/drums.wav")
        ramp = np.linspace(0, 1, len(audio), dtype=np.float32)
        audio = audio * ramp
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(dot.canvas, col=dot.black, with_playhead=True)
        draw_bars(dot.canvas, 2, 4)
    
MySketch() 