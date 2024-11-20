from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    
    def __init__(self):
        
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        pass

    def draw(self):
        dot.background(dot.darkblue)
        snow = [[0,0],[80,0],[160,0],[240,0],[320,0],[400,0],[480,0],[560,0],[640,0]]
        ptr = 0
        for pt in snow:
            circle(dot.canvas, pt, 10, dot.white, -1)
            #update the y position by 10 
            snow[ptr][1] = (snow[ptr][1] + 10) % dot.height 
            ptr = ptr +1    
MySketch() 