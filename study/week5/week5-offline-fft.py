from dorothy import Dorothy 
import librosa
import numpy as np
from cv2 import line
from sklearn.preprocessing import MinMaxScaler

dot = Dorothy(640, 480) 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)   
    def setup(self):
        audio, sr = librosa.load("week5/audio/gospel.wav")
        #Do fft
        self.fft_full_track = np.abs(librosa.stft(audio)).T
        #Normalise to 0-1
        self.fft_full_track = MinMaxScaler().fit_transform(self.fft_full_track)
        self.fft_layer = dot.get_layer()
        #Go through each frame
        for pos, frame in enumerate(self.fft_full_track):
            #Where to draw horizontally (time)? 
            x = int(pos/len(self.fft_full_track)*dot.width)
            for bin, val in enumerate(frame):
                #Where to draw vertically (frequency bin)?
                y = dot.height - int(bin/len(frame)*dot.height)
                colour = (int(val*255), 0, 0)
                #Draw to layer (only need to calculate once)
                line(self.fft_layer ,(x, y), (x, y+2), colour, 3)
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.black)
        #Draw playhead (col=None for waveform e.g. dont draw)
        playhead = dot.get_layer()
        dot.draw_waveform(playhead, col = None, with_playhead = True)
        dot.draw_layer(playhead)
        #Draw fft
        dot.draw_layer(self.fft_layer)
    
               
MySketch() 