from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        pass

    def draw(self):
        positions = [0,80,160,240,320,400,480,560,640]
        
        #Only change every 10 frames
        if dot.frame % 10 == 0:
            dot.background(dot.darkblue)  
            #Loop around      
            x = positions[dot.frame%len(positions)]
            y = dot.height//2
            circle(dot.canvas, (x, y), 10, dot.white,-1)
             
MySketch() 
