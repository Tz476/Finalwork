from cv2 import circle, rectangle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        self.color = [0,0,0]  
        #interpolate between these colours
        self.a = dot.cyan
        self.b = dot.magenta
        
    def draw(self):
        #Get x position as fraction of screen 
        t = dot.mouse_x/dot.width
        #Use to interpolate r g and b values
        for i in range(3):
            self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)
        dot.background(self.color)

            

MySketch()          