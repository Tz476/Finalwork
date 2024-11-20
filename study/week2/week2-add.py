from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup)  
    def setup(self):
        radius = 100
        x = radius
        y = radius
        circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
        x = x + radius
        y = y + radius
        circle(dot.canvas, (x,y), radius, dot.fuchsia, -1)
        x = x + radius
        y = y + radius
        circle(dot.canvas, (x,y), radius, dot.aqua, -1)
        x = x + radius
        y = y + radius
        circle(dot.canvas, (x,y), radius, dot.lavender, -1)
        x = x + radius
        y = y + radius
MySketch() 