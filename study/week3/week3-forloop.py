from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy(600,600) 
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        dot.background(dot.darkblue)

    def draw(self):
        positions = [0,80,160,240,320,400,480,560,640]
        for x in positions:
            y = dot.height//2
            circle(dot.canvas, (x, y), 10, dot.white,-1)
             
MySketch() 