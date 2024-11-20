from cv2 import circle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:

    def __init__(self):
        
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        print("setup")
        self.t = 0.05
        self.pos = [0,0]  

    def draw(self):
        dot.background((255,0,100))
        self.pos[0] = int(self.pos[0] + (dot.mouse_x - self.pos[0]) * self.t)
        self.pos[1] = int(self.pos[1] + (dot.mouse_y - self.pos[1]) * self.t)
        circle(dot.canvas, self.pos, 40, dot.black,-1)

        
        
MySketch()          







