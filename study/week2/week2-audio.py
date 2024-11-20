from dorothy import Dorothy
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        #Check out https://git.arts.ac.uk/lmccallum/samples/ to find some new samples
        dot.music.start_file_stream("week2/audio/test.wav")
        dot.start_record()
        self.r = 0

    def draw(self):
        dot.background(dot.white)
        self.r -= (self.r*0.3)
        self.r += (10000*dot.music.amplitude())*0.3
        circle(dot.canvas, (dot.width//2, dot.height//2), int(self.r), dot.black, -1)
        if dot.frame == 9999999:
            dot.stop_record()
               
MySketch() 