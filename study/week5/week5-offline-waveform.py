from dorothy import Dorothy 
import librosa
from cv2 import line

dot = Dorothy(640, 480) 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
         
    def setup(self):
        audio, sr = librosa.load("week5/audio/keys4.wav")
        
        window_size = 2048
        windows = librosa.util.frame(audio, frame_length=window_size, hop_length=window_size)
        windows = windows.transpose()
        amps = []
        for buffer in windows:
            mean = (buffer**2).mean()
            amps.append(mean)
        
        self.waveform_layer = dot.get_layer()
        for i, val in enumerate(amps):
            #Where to draw horizontally (time)? 
            x = int(i*dot.width/len(windows))
            #How much height?
            h = int(val*dot.height)*10
            #Centre vertically
            y = dot.height//2 - h//2
            line(self.waveform_layer, (x, y), (x, y + h), dot.red, 2)
        dot.music.start_sample_stream(audio, sr=sr)

    def draw(self):
        dot.background(dot.black)
        #Draw playhead (col=None for waveform e.g. dont draw)
        dot.draw_waveform(dot.canvas, col = None, with_playhead = True)
        #Draw semi-transparent waveform (0.8 alpha)
        dot.draw_layer(self.waveform_layer, 0.8)
    
               
MySketch() 