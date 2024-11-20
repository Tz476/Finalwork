from dorothy import Dorothy 
import numpy as np

dot = Dorothy(600,200) 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup) 

    def setup(self):
        dataset = dot.get_images("week6/data/animal_thumbnails/land_mammals", thumbnail_size = (100,100))
        print(f"the dataset has 4 dimensions: {dataset.shape} (images x width x height x channels)")
        mean_rgb_dataset = np.apply_over_axes(np.mean, dataset, [1,2])
        print(f"when we average over the [h, w] dimensions, we get {mean_rgb_dataset.shape}, which is one rgb pixel (the average colour) for each image")
        x = 0
        for i in np.random.randint(len(dataset), size=(6)):
            src = dataset[i]
            pixel = mean_rgb_dataset[i]
            colour = np.full((100, 100, 3), pixel, dtype=np.uint8)
            dot.paste(dot.canvas, src, (x, 0))
            dot.paste(dot.canvas, colour, (x, 100))
            x += 100
          
MySketch()