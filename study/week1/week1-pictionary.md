# Drawing Task Instructions 

## Make your own sketch 

Use the file explorer on the left to copy and paste a new version of the file ``week1.py``. Give it a new name! You can do this by right clicking and selecting ``Rename``.

In the terminal (bottom window), run

```
pip3 install dorothy-cci
```

### Run the file

Click the play button in the top right when your new `.py` file is open, it should open a separate window with a rectangle in it. 

## Task - Pictionary 

This task is adapted from [Angi Chau](https://teach.angichau.com/starter-kit-for-teaching-with-p5-js/drawing-colors-collapsible/). 

The task here is to draw the prompt you are given by this [generator](https://mimicproject.com/code/f0224dd6-0e09-398f-2c35-8ff311c9fe28?embed=true&showCode=false) using the shapes available in the openCV [drawing functions](https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html). 

The main ones to try are below. Replace the names of the parameters with numbers to control where, how big and what colour / style to draw. 

You should put all your code under the `def setup(self):` function

Remember you will need to `import` them from `cv2`!

* Rectangle
    * Import using:       
       * `from cv2 import rectangle`
    * Arguments:
       * ```rectangle(dot.canvas, (top_left_x, top_left_y), (bottom_right_x, bottom_y), color, border_weight (-1 for fill))```
    * Example
       * ```rectangle(dot.canvas, (0,0), (100,100), dot.red, 2)```    

* Line
    * Import using:    
       * `from cv2 import line`
    * Arguments:
       * ```line(dot.canvas, (x1,y1), (x2, y2), color, line_weight)```
    * Example:
       * ```line(dot.canvas, (0,0), (100,100), dot.black, 4)```

* Circle
    * Import using: 
       * `from cv2 import circle`
    * Arguments:
       * ``circle(dot.canvas, (centre_x, centre_y), radius, color, border_weight (-1 for fill))``
    * Example:
       * ``circle(dot.canvas, (100,100), 50, dot.yellow, -1)``


### Common Issues 

* I can't see my changes! 
    * Is the old window still open?
    * Press `q` whilst the window is in focus to quit, or use `ctrl+z` in the terminal. You should kill the window **before** you re-run the code to see changes. 

* `ModuleNotFoundError`. 
    * Are you in the `stem-24-25` conda environment? 
    * It will be in brackets at the beginning of your terminal window
    * And in the bottom left next to `Python`

* Things are where they are supposed to be! 
    * Remember, the top left is `(0,0)`, the bottom right is `(dot.width, dot.height)`.

* I'm getting errors related to my coordinate and length values! 
    * `> Overload resolution failed: .... is required to be an integer`
    * Are your coordinates and lengths integers? OpenCV requires exact pixel values so you may need to convert using `int()`.

* All available colours are [here](https://github.com/Louismac/dorothy/blob/main/src/dorothy/css_colours.py)

Happy Drawing! 

Make a screen shot and add your picture to the padlet when you are done!

Take a look at others pictures on the [padlet](https://artslondon.padlet.org/lmccallum3/stem-week-1-2224dy57i8e7r53b), can you guess the prompt?. Add in a comment with your guess!
