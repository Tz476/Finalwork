from cv2 import rectangle
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")

    def draw(self):
        
        dot.background((255,255,255))
        #get a new canvas
        new_canvas = dot.get_layer()
        #Draw to it
        rectangle(new_canvas, (0,0), (dot.width, dot.height), (0,255,0), -1)
        
        #How quickly to change?
        period = 300
        #Where are we in the cycle?
        factor = (dot.frame%period)/period

        # theta = factor * 2 * np.pi
        # rotate = np.array([[np.cos(theta), -np.sin(theta)],
        #                    [np.sin(theta), np.cos(theta)]])
        
        scale = np.array([[factor,0.0],
                          [0.0,factor]])
        
        #linear transform
        origin = (0,0)
        origin = (dot.width//2,dot.height//2)
        new_canvas = dot.transform(new_canvas, scale, origin)
        #push it back onto layer stack
        dot.draw_layer(new_canvas)
        

MySketch()          







