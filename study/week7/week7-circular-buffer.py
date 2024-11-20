import cv2
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        self.threshold = 50
        #How big is the buffer?
        self.window_size = 30
        #Make empty buffer
        self.buffer = np.zeros((self.window_size, dot.height, dot.width)).astype(dtype=np.uint8)
        #Make variable to hold model (avg of buffers)
        self.model = self.buffer[0]
        #Where are we in the buffer (write pointer)
        self.write_ptr = 0
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(dot.width, dot.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2GRAY)
            
            diff = cv2.absdiff(camera_feed, self.model)
            thresholded = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
            
            #Update mask with mean pixel values from buffer (axis 0 is time!)
            self.model = np.mean(self.buffer, axis=0).astype(dtype=np.uint8)
            
            #Update the circular buffer
            self.write_ptr = (self.write_ptr + 1) % self.window_size
            self.buffer[self.write_ptr] = camera_feed

            dot.canvas = thresholded
        
MySketch()          







