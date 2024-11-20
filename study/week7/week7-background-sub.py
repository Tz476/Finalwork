import cv2
from dorothy import Dorothy 

dot = Dorothy() 

class MySketch:

    

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        #Save first frame as background
        self.success, self.camera_background = self.camera.read()
        self.camera_background = cv2.resize(self.camera_background,(dot.width, dot.height))
        self.camera_background = cv2.cvtColor(self.camera_background, cv2.COLOR_BGR2GRAY)
    
    def draw(self):
        dot.background((255,255,255))
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(dot.width, dot.height))
            camera_feed= cv2.cvtColor(camera_feed, cv2.COLOR_BGR2GRAY)
            #Absolute difference between current frame and first frame (background)
            diff = cv2.absdiff(camera_feed, self.camera_background)
            dot.canvas = diff
        
MySketch()          







