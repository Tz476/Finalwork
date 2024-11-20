from dorothy import Dorothy 
import librosa
import numpy as np

dot = Dorothy(600,150) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        audio, sr = librosa.load("week4/audio/drums.wav")
        #Get from the beginning to sr (this is the first second)
        beginning = audio[:sr]
        print(len(beginning)) 
        #Get from the (end - sr) to the end (this is the last second)
        end = audio[-sr:]
        print(len(end)) 
        #Get from sr to sr*3 (this is second 1-3)
        mid = audio[sr:sr*3]
        print(len(mid)) 
        joined = np.concatenate((end,beginning,mid))
        print(joined.shape)
        dot.music.start_sample_stream(joined, sr = sr)

    def draw(self):
        dot.background((255,255,255))
        dot.draw_waveform(dot.canvas, col=dot.black, with_playhead=True)
               
MySketch() 