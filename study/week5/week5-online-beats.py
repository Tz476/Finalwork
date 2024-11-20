from dorothy import Dorothy 
from cv2 import line

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        file_path = "week5/audio/drums.wav"
        dot.music.start_file_stream(file_path, fft_size=512)
        self.show_beat = 0

    def draw(self):
        col = dot.black
        if dot.music.is_beat():
            self.show_beat = 10

        if self.show_beat > 0:
            col = dot.white

        dot.background(col)
        self.show_beat -= 1
    
MySketch() 