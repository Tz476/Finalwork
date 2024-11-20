import cv2
from cv2 import circle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)  

    def setup(self):
        print("setup")
        self.camera = cv2.VideoCapture(0)
        self.face_cascade=cv2.CascadeClassifier("week7/data/haarcascade_frontalface_default.xml")

    
    def draw(self):
        success, camera_feed = self.camera.read()
        if success:
            camera_feed = cv2.resize(camera_feed,(dot.width, dot.height))
            camera_feed = cv2.cvtColor(camera_feed, cv2.COLOR_BGR2RGB)
            camera_feed_grayscale = cv2.cvtColor(camera_feed, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(camera_feed_grayscale, 1.1, 4)

            for face_x, face_y, face_w, face_h in faces:
                #Draw circle around face
                ##ADD YOUR OWN CODE IN HERE
                circle(camera_feed,
                            (face_x+face_w//2,face_y+face_h//2),
                            face_w//2,255,-1)
            
            dot.canvas = camera_feed
        
MySketch()          







