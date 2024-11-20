from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup)  
    def setup(self):
        radius = 40
        x = dot.width//2
        y = dot.height//2
        circle(dot.canvas, (x,y), radius*2*2*2, dot.lavender, -1)
        circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
        circle(dot.canvas, (x,y), radius*2, dot.fuchsia, -1)
        circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
MySketch() 