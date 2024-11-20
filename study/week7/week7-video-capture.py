import cv2
from dorothy import Dorothy 

dot = Dorothy() 

class MySketch:
    
    

    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        #Set up camera
        self.camera = cv2.VideoCapture(0)
    
    def draw(self):
        #Pull in frame
        success, camera_feed = self.camera.read()
        if success==True:
            #Convert color
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            #Resize to canvas size
            camera_feed = cv2.resize(camera_feed,(dot.width, dot.height))
            #Write to screen
            dot.canvas = camera_feed
        
MySketch()          







