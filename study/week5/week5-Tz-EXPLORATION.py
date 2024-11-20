from dorothy import Dorothy

dot = Dorothy()

def setup():
    file_path = "week5/audio/drums.wav" 
    dot.music.start_file_stream(file_path)

def draw():
    dot.background(dot.black) 

    amplitude = dot.music.amplitude()  
    size = int(amplitude * 200)  


    dot.circle(dot.canvas, (dot.width // 2, dot.height // 2), size, dot.red)
