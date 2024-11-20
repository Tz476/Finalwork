#import the library
from dorothy import Dorothy 
#Make an instance of it
dot = Dorothy() 

#Define your sketch class
class MySketch:

    #Called when a MySketch object is made
    def __init__(self):
        dot.start_loop(self.setup)  

    #Called once at the beginning by start_loop
    def setup(self):
        dot.background(dot.red)

#Make an instance of your sketch  
MySketch()   