from dorothy import Dorothy 
import numpy as np
from PIL import Image

dot = Dorothy(550, 183) 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup) 

    def setup(self):
        rgb_image = Image.open('week6/images/space.jpg')
        grayscale = rgb_image.convert('L')

        rgb_image = np.array(rgb_image)
        grayscale = np.array(grayscale)
        
        #How big is it?
        h = rgb_image.shape[0]
        w = rgb_image.shape[1]
        
        print(f"the image loaded in is {w} pixels wide and {h} pixels high")
        print(f"the original image loaded in has {rgb_image.ndim} dimensions (h x w x c)")
        
        dot.paste(dot.canvas, grayscale, (0,0))
        dot.paste(dot.canvas, rgb_image, (w,0))
          
MySketch()