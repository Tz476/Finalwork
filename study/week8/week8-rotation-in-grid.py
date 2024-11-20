from cv2 import rectangle, circle
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")        
        
    def draw(self):
        
        dot.background((22, 208, 165))

        size = 40
        border = 10
        grid = 5
        x_offset = (dot.width - ((size+border)*grid)) //2
        y_offset = (dot.height - ((size+border)*grid)) //2
        #How quickly to change?
        period = 100
        #Where are we in the cycle?
        factor = (dot.frame%period)/period
        #Get angle
        theta = factor * 2 * np.pi

        for i in range(grid):
            for j in range(grid):
                #Where to draw the shape?
                x = i * (size+border) + x_offset
                y = j * (size+border) + y_offset

                #get a new canvas
                new_canvas = dot.get_layer()
                #Draw to it
                top_left = (x,y)
                bottom_right = (x+size, y+size)
                rectangle(new_canvas, top_left, bottom_right, (77, 72, 79), -1)
                origin = (x+size//2, y+size//2)
                circle(new_canvas, origin, 2, (22, 208, 165), -1)
                new_canvas = dot.rotate(new_canvas, theta, origin)
                #push it back onto layer stack
                dot.draw_layer(new_canvas)

MySketch()          