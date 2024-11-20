from dorothy import Dorothy 
from cv2 import circle
import random

dot = Dorothy() 
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        self.snow = [[0,0],[80,0],[160,0],[240,0],[320,0],[400,0],[480,0],[560,0],[640,0]]

    def draw(self):
        dot.background(dot.darkblue)
        ptr = 0
        for pt in self.snow:
            circle(dot.canvas, pt, 10, dot.white, -1)
            #update the y position by random between 0 and 5
            move_by = random.randint(0,5)
            self.snow[ptr][1] = (self.snow[ptr][1] + move_by) % dot.height
            ptr = ptr + 1      
MySketch() 