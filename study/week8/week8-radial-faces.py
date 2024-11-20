from cv2 import rectangle
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    thumbnail_size = (100,100)
    dataset = dot.get_images("week8/aligned_faces", thumbnail_size)

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")

    def draw(self):
        
        dot.background((255,0,100))
        num_faces = 20
        for i in range(num_faces):
            new_canvas = dot.get_layer()
            index = np.random.randint(len(self.dataset))
            to_paste = self.dataset[index]
            #Draw inwards from top left
            coords = (100,100)
            dot.paste(new_canvas, to_paste, coords)
            #How quickly to change?
            period = 50
            #Where are we in the cycle?
            factor = (dot.frame%period)/period
            #Get angle and factor in place in list (i)
            theta = (factor * (i/num_faces)) * 2 * np.pi 
            rotate = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])
            
            #linear transform
            origin = (dot.width//2,dot.height//2)
            new_canvas = dot.transform(new_canvas, rotate, origin)
            #push it back onto layer stack
            dot.draw_layer(new_canvas)
        
MySketch()          







