import cv2
from dorothy import Dorothy

dot = Dorothy()

class Myvideowork:
      
    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        self.camera = cv2.VideoCapture(0)
        self.success, self.camera_background = self.camera.read()
        self.threshold = 120
        self.camera.set(cv2.CAP_PROP_AUTOFOCUS, 0)
        self.camera_background = cv2.resize(self.camera_background,(dot.width, dot.height))
    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(dot.width, dot.height))
            diff = cv2.absdiff(camera_feed, self.camera_background)
            diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)   
            thresholded = cv2.threshold(diff, self.threshold, 255, cv2.THRESH_BINARY)[1]
            dot.canvas = thresholded
        
Myvideowork()          
