from dorothy import Dorothy 
import librosa

dot = Dorothy(600,150) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/drums.wav")
        num_samples = len(audio)
        print(f"{num_samples} samples at {sr} lasts for {num_samples / sr:.2f} seconds")
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(dot.canvas, col=dot.black, with_playhead=True)
               
MySketch() 