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
        #Get a new canvas to draw the shapes to
        new_canvas = dot.get_layer()
        for i in range(grid):
            for j in range(grid):
                #Where to draw the shape?
                x = i * (size+border)
                y = j * (size+border)
                rectangle(new_canvas, (x,y), (x+size, y+size), (77, 72, 79), -1)
                
        #How quickly to change?
        period = 100
        #Where are we in the cycle?
        factor = (dot.frame%period)/period
        #Get angle
        theta = factor * 2 * np.pi
        rotate = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])
                
        origin = (dot.width//2, dot.height//2)
        circle(new_canvas, origin, 5, dot.red, -1)
        new_canvas = dot.transform(new_canvas, rotate, origin)
        #push it back onto layer stack
        dot.draw_layer(new_canvas)
        
MySketch()          
