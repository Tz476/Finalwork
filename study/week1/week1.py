from dorothy import Dorothy 
from cv2 import line

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup)  
    def setup(self):
        line(dot.canvas, (0,0), (100,100), dot.black, 2)
MySketch() 