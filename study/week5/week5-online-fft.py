from dorothy import Dorothy 
from cv2 import line

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        file_path = "week5/audio/drums.wav"
        dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)

    def draw(self):
        dot.background(dot.black)
        for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
            pt1 = (bin_num*5, dot.height)
            pt2 = (bin_num*5, dot.height-int(bin_val*200))
            line(dot.canvas, pt1, pt2, (0,255,255), 2)
    
MySketch() 