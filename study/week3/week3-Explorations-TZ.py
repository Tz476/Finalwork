from dorothy import Dorothy
import cv2 
import numpy as np

dot = Dorothy()
class MySketch:
    
    def __init__(self):
        
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        dot.music.start_file_stream("week2/audio/test.wav")#播放音乐
        dot.start_record()
        num_code = 200#小球数量
        
        x = np.linspace(0,dot.width,num_code).astype(int)
        y = np.random.randint(0,dot.height ,num_code)

        self.speed = np.random.randint(1,7,num_code)#速度

        self.colors = [tuple(np.random.randint(0, 256, size=3).tolist()) for _ in range(num_code)]
        self.code = []
        for pt in zip(x,y):
            self.code.append(list(pt))

    def draw(self):
        background_color = (
            50,
            int(np.clip(255-(dot.music.amplitude() * 1000000), 0, 255)),  
            int(np.clip(100+(dot.music.amplitude() * 500000), 0, 255)),  
        )
        print(background_color,dot.music.amplitude())
        ptr = 0
        for pt in self.code:
            speed = self.speed[ptr]
            radius = int(speed + dot.music.amplitude() * 500)    

            # trail_radius = int(radius*1.5) 
            # cv2.circle(dot.canvas, pt, trail_radius, self.colors[ptr], -1) 

            cv2.circle(dot.canvas, pt, radius, self.colors[ptr], -1)

            self.code[ptr][1] = (self.code[ptr][1] + speed) % dot.height
            ptr = ptr + 1 
        cover = dot.get_layer()

        cv2.rectangle(cover, (0,0),(dot.width, dot.height),background_color, -1)

        dot.draw_layer(cover, 0.2)   

MySketch() 