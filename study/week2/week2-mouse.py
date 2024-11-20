from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        pass

    def draw(self):
        radius = 20
        x = dot.mouse_x
        y = dot.mouse_y
        circle(dot.canvas, (x,y), radius*2*2*2, dot.lavender, -1)
        circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
        circle(dot.canvas, (x,y), radius*2, dot.fuchsia, -1)
        circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
        
MySketch() 