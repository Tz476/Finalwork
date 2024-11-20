from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy(600,600) 
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        dot.background(dot.yellow)

    def draw(self):
        face = [
            [450, 300], [437, 361], [400, 411], [346, 442], [284, 449], [225, 429],
            [178, 388], [153, 331], [153, 268], [178, 211], [224, 170], [284, 150],
            [346, 157], [400, 188], [437, 238], [270, 250], [256, 269], [233, 261],
            [233, 238], [256, 230], [370, 250], [356, 269], [333, 261], [333, 238],
            [356, 230], [356, 376], [330, 393], [300, 400], [269, 393], [243, 376]
        ]

        for pt in face:
            circle(dot.canvas, pt, 10, dot.black,-1)
             
MySketch() 