from dorothy import Dorothy
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)   

    def setup(self):
        dot.music.start_file_stream("week2/audio/test.wav")
        dot.start_record()
        self.y_pos = dot.height//2
        self.r = 50
    

    def draw(self):
        dot.background(dot.white)
        self.r -= (self.r*0.3)
        self.r += (10000*dot.music.amplitude())*0.3

    

        circle(dot.canvas, (dot.width//2, int(self.y_pos)),20, dot.pink, -1)


        self.y_pos -= (self.y_pos * 0.3) 
        self.y_pos += (10000 * dot.music.amplitude()) * 0.3
        

        circle(dot.canvas, (dot.width//1, dot.height//2), int(self.r*1.5), dot.yellow, -1)
        circle(dot.canvas, (dot.width//1, dot.height//2), int(self.r), dot.black, -1)

        circle(dot.canvas, (0, dot.height//2), int(self.r*1.5), dot.yellow, -1)
        circle(dot.canvas, (0, dot.height//2), int(self.r), dot.black, -1)

        # circle(dot.canvas, (dot.width//1.5, dot.height//1.5), int(self.r*0.5), dot.yellow, -1)
        # circle(dot.canvas, (dot.width//1.5, dot.height//1.5), int(self.r*0.7), dot.black, -1)

        radius = 20
        a = dot.mouse_x
        b = dot.mouse_y
        # circle(dot.canvas, (a,b), radius*2*2*2, dot.lavender, -1)
        # circle(dot.canvas, (a,b), radius*2*2, dot.aqua, -1)
        circle(dot.canvas, (a,b), radius*2, dot.fuchsia, -1)
        circle(dot.canvas, (a,b), radius, dot.blueviolet, -1)
        
               
MySketch() 