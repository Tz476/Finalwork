from dorothy import Dorothy 
import librosa
from util import draw_bars

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/keys4.wav")
        dot.music.start_sample_stream(audio, sr=sr/2)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(dot.canvas, col=dot.black, with_playhead=True)
        draw_bars(dot.canvas, 2, 4)
    
        
MySketch() 