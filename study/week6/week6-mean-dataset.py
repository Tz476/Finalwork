from dorothy import Dorothy 
import numpy as np
from PIL import Image

dot = Dorothy() 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup) 

    def setup(self):
        dataset = dot.get_images("week6/data/animal_thumbnails/land_mammals", thumbnail_size = (300,300))
        print(f"the dataset has 4 dimensions: {dataset.shape} (images x width x height x channels)")
        mean_image =  np.apply_over_axes(np.mean, dataset, [0])
        mean_image = np.squeeze(mean_image).astype(np.uint8)
        dot.paste(dot.canvas, mean_image, (0,0))

        mean_rgb_dataset = np.apply_over_axes(np.mean, dataset, [1,2])
        print(f"when we average over the [h, w] dimensions, we get {mean_rgb_dataset.shape}, which is one rgb pixel (the average colour) for each image")
          
MySketch()