#import the library
print("import the Dorothy Library")
from dorothy import Dorothy 
#Make an instance of it
print("Making a Dorothy object and saving it in the variable \"dot\"")
dot = Dorothy() 

#Define your sketch class
print("Defining MySketch") 
class MySketch:

    #Called when a MySketch object is made
    def __init__(self):
        print("MySketch __init__()")
        dot.start_loop(self.setup)  

    #Called once at the beginning by start_loop
    def setup(self):
        print("MySketch setup()")
        dot.background(dot.red)

#Make an instance of your sketch  
print("Making MySketch")
MySketch()   