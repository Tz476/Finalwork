from dorothy import Dorothy 
import librosa
from util import draw_bars

dot = Dorothy(1200,300) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/keys4.wav")
        audio2, sr = librosa.load("week4/audio/harp1.wav")
        drums, sr = librosa.load("week4/audio/drums75.wav") 
        samples_in_bar = len(audio) // 2
        samples_in_beat = samples_in_bar // 4
        cut = audio2[:samples_in_beat*2 ]
        audio[samples_in_beat:samples_in_beat*3] = cut
        dot.music.start_sample_stream(audio + drums, sr=sr)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(dot.canvas, col=dot.black, with_playhead=True)
        draw_bars(dot.canvas, 2, 4)
               
MySketch() 