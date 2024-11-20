from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup)  
    def setup(self):
        radius = dot.width//2
        circle(dot.canvas, (radius,radius), radius, dot.fuchsia, -1)
        circle(dot.canvas, (radius,0), radius, dot.aqua, -1)
        circle(dot.canvas, (0,radius), radius, dot.blueviolet, -1)
        circle(dot.canvas, (0,0), radius, dot.lavender, -1)
MySketch() 