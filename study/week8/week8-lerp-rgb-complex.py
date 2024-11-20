from cv2 import circle, rectangle
from dorothy import Dorothy

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        self.color = [0,0,0]  
        self.a = dot.cyan
        self.b = dot.magenta
        
    def draw(self):
        
        layer = dot.get_layer()
        slices = 10
        #darken based on y coordinate
        darken = dot.mouse_y/dot.height

        for s in range(slices*2):
            #Intepolate based on y position on screen
            t = s/slices
            #Every second slice is a darkenend version
            if s % 2 == 1:
                t *= 0.9
            #Calculate new colour
            for i in range(3):
                self.color[i] = int(self.a[i] + (self.b[i] - self.a[i]) * t)*darken
            #Draw rectangle
            y = int(((s)/(2*slices))*dot.height)
            h = int(dot.height/(2*slices))
            rectangle(layer,(0,y),(dot.width, y+h), self.color, -1)
        
        factor = dot.mouse_x/dot.width
        origin = (dot.width//2,dot.height//2)
        layer = dot.scale(layer,factor,factor,origin)
        dot.draw_layer(layer)


MySketch()          