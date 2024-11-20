from dorothy import Dorothy
from cv2 import line
import math

# problem --> how do we draw a cross in the centre of the screen? each line is 100 pixels long
# what we know --> centre of the screen is C = (dot.width//2, dot.height//2), a cross forms 4 right angles (90 degrees)
# how to approach this --> we need to find the coordinates of the top left, top right, bottom left and bottom right corners of the cross, and then draw lines between them. to find these coordinates, we can use trigonometry.

# A             B
#   \          /
#    \        /
#     \      /
#      \    /
#       \  /
#        C
#       /  \
#      /    \
#     /      \
#    /        \
#   /          \
#  D            E
#
# (each angle in the cross is 90 degrees)


dot = Dorothy()


class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        lin_length = 100
        angle = 90 // 2
        # c is the centre of the screen
        x_c = dot.width//2
        y_c = dot.height//2

        # a is the top left corner of the cross, which we can obtain by rotating the coordinate (xc, yc-lin_length), by 45 degrees to the left
        x_a = round(x_c - (lin_length // 2) * math.cos(math.radians(angle)))
        y_a = round(y_c - (lin_length // 2) * math.sin(math.radians(angle)))

        # b is the top right corner of the cross, which we can obtain by rotating the coordinate (xc+lin_length//2, yc-lin_length), by 45 degrees to the right
        x_b = round(x_c + (lin_length // 2) * math.cos(math.radians(angle)))
        y_b = round(y_c - (lin_length // 2) *math.sin(math.radians(angle)))  # = y_a

        # d is the bottom left corner of the cross, which we can obtain by rotating the coordinate (xc-lin_length//2, yc+lin_length), by 45 degrees to the right
        x_d = round(x_c - (lin_length // 2) *math.cos(math.radians(angle)))  # = x_a
        y_d = round(y_c + (lin_length // 2) * math.sin(math.radians(angle)))

        # e is the bottom right corner of the cross, which we can obtain by rotating the coordinate (xc+lin_length//2, yc+lin_length), by 45 degrees to the left
        x_e = round(x_c + (lin_length // 2) *math.cos(math.radians(angle)))  # = x_b
        y_e = round(y_c + (lin_length // 2) *math.sin(math.radians(angle)))  # = y_d

        line(dot.canvas, (x_a, y_a), (x_e, y_e), dot.red, 2)
        line(dot.canvas, (x_b, y_b), (x_d, y_d), dot.red, 2)

    def draw(self):
        # extra task: rotate the cross
        pass


MySketch()
