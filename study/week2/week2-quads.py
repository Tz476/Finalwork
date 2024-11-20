from dorothy import Dorothy 
from cv2 import rectangle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        print("setup")

    def draw(self):
        dot.background(dot.white)
        #Top left
        if dot.mouse_x < dot.width//2 and dot.mouse_y < dot.height//2:
            rectangle(dot.canvas, (0,0),(dot.width//2,dot.height//2), dot.red, 10)
        #Bottom left
        elif dot.mouse_x < dot.width//2 and dot.mouse_y > dot.height//2:
            rectangle(dot.canvas, (0,dot.height//2),(dot.width//2,dot.height), dot.red, 10)
        #Top Right
        elif dot.mouse_x > dot.width//2 and dot.mouse_y < dot.height//2:
            rectangle(dot.canvas, (dot.width//2,0),(dot.width,dot.height//2), dot.red, 10)
        #Bottom Right
        else:
            rectangle(dot.canvas, (dot.width//2,dot.height//2),(dot.width,dot.height), dot.red, 10)
        
MySketch() 