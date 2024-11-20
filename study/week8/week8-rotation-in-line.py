from cv2 import rectangle, circle
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup)  

    def setup(self):
        print("setup")
        size = 40
        border = 10
        grid = 5
        x_offset = (dot.width - ((size+border)*grid)) //2
        theta = np.pi/6
        for i in range(5):
            x = i * (size+border) + x_offset
            y = dot.height//2

            #get a new canvas
            new_canvas = dot.get_layer()
            #Draw to it
            top_left = (x,y)
            bottom_right = (x+size, y+size)
            rectangle(new_canvas, top_left, bottom_right, (77, 72, 79), -1)
            origin = (x+size//2, y+size//2)
            circle(new_canvas, origin, 5, dot.red, -1)
            new_canvas = dot.rotate(new_canvas, theta, origin)
            #push it back onto layer stack
            dot.draw_layer(new_canvas)

MySketch()          