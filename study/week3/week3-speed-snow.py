from dorothy import Dorothy 
from cv2 import circle
import numpy as np
import random

dot = Dorothy() 
class MySketch:
    
    def __init__(self):
        
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        num_flakes = 100
        x = np.linspace(0,dot.width,num_flakes).astype(int)
        y = np.zeros(num_flakes).astype(int)
        self.speed = np.random.randint(1, 7, 100)
        self.snow = []
        #iterate through both and combine into the variable pt
        for pt in zip(x,y):
            self.snow.append(list(pt))
        dot.start_record(end=1000)

    def draw(self):
        dot.background(dot.darkblue)
        ptr = 0
        for pt in self.snow:
            circle(dot.canvas, pt, 10, dot.white, -1)
            move_by = self.speed[ptr]
            self.snow[ptr][1] = (self.snow[ptr][1] + move_by) % dot.height
            ptr = ptr + 1 
MySketch() 