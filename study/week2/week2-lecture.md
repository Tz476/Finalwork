# Week 2 - Introduction to Algorithms 

In this second week, we are building on last week’s foundation of static sketches by introducing key programming concepts like `variables`, `responsiveness`, and `conditionals`. While the sketches we created before were based on hard coded values, this week we’ll begin to explore how to make our sketches more **dynamic** and **responsive**. 

``Variables`` allow us to store and manipulate data, making it possible to adjust the elements of a sketch in real time. By responding to user input, other inputs (such as `audio`) or even the passing of time, we use **dynamic data** to effect the output of our code.

By introducing `conditionals`, we open the door to creating more complex behaviours within our sketches. `Conditionals` allow us to set up rules and decisions in our code, defining how the program reacts under different circumstances. 

This combination of `variables`, `responsiveness`, and `conditionals` forms the core of what we call **algorithms**: structured sets of instructions that can adapt to different inputs and conditions. In doing so, we move from creating static art to writing dynamic, **interactive programs that act and respond like systems**.

## Variables 

A ``Variable`` is a place that we can use to store values (``text`` or ``numbers`` or larger ``objects`` (like the whole ``Dorothy`` library!). 

We can then use them later and just use the **names of the variable**, and the code will interpret that as **the value stored inside it**.

Once you have declared the variable, you can change the value in it. The code will interpret it as whatever is in the variable **at that particular time**.

#### What variable is being used in this code from last week?

```python
from dorothy import Dorothy 
from cv2 import line

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup)  
    def setup(self):
        line(dot.canvas, (0,0), (100,100), dot.black, 2)
MySketch() 
```
When the code is run, the **actual value** stored in the variable ``dot.black`` is looked up, and it is replaced with `(0,0,0)`

We can look at this code that draws a circle. We can take parts where we have hardcoded numbers and replace them with named variables.

These two bits of code do this same thing, but the addition of variables doesn't necssarily help us much

```python
circle(dot.canvas, (100,100), 100, dot.black, -1)
```

```python
#Extracted in variables
x = 100
y = 100
radius = 100
circle(dot.canvas, (x,y), radius, dot.black, -1)
```

But once you start with more complex code, you now have 1 variable that controls the position and size of all four circles!

```python
#week2-variables.py
radius = dot.width//2
circle(dot.canvas, (radius,radius), radius, dot.fuchsia, -1)
circle(dot.canvas, (radius,0), radius, dot.aqua, -1)
circle(dot.canvas, (0,radius), radius, dot.blueviolet, -1)
circle(dot.canvas, (0,0), radius, dot.lavender, -1)
```
## Numbers

There are **two types of numbers** in Python. 

1. ``Int`` (short for integer). These are rounded numbers with **no decimal places**. You`ll notice I often use the ``//`` division as the openCV drawing functions require integers for positions and sizes. 


2. ``Float`` (not short for anything, thats it). You can use these if you need the precision of decimal places


In most cases, Python will just work out whats best to use, but in some cases its necsesary to specify, **more on that later**


### Maths

You can do basic maths with numbers 

* Addition `+`
    ```python
    #week2-add.py
    radius = 100
    x = radius
    y = radius
    circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
    x = x + radius
    y = y + radius
    circle(dot.canvas, (x,y), radius, dot.fuchsia, -1)
    x = x + radius
    y = y + radius
    circle(dot.canvas, (x,y), radius, dot.aqua, -1)
    x = x + radius
    y = y + radius
    circle(dot.canvas, (x,y), radius, dot.lavender, -1)
    x = x + radius
    y = y + radius
    ```

* Subtraction `-`
    ```
    10 - 2
    ```
    **Output**:
    <code style="font-family: Monaco">
    8
    </code>

* Multiplication `*`
    ```python
    #week2-multiply.py
    radius = 40
    x = dot.width//2
    y = dot.height//2
    circle(dot.canvas, (x,y), radius*2*2*2, dot.lavender, -1)
    circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
    circle(dot.canvas, (x,y), radius*2, dot.fuchsia, -1)
    circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
    ```

* Division `/`
    ```
    10 / 2
    ```
    **Output**:
    <code style="font-family: Monaco">
    5
    </code>

#### Special Division Cases

* Integer Division `//`. This always returns a whole number

* Modulo `%`. This returns the remainder of the division and is an excellent tool for looping. 

## Draw Loop

To really complete the basics of `Dorothy`, we actually need another function in our sketch, `draw()`. This is called on a loop so we can update our drawing dynamically. This can be over time, or in response to user input.

If we move our drawing code into the `draw()` not much changes. 

But if we change our code so that there is a different value in for `x` and `y` each time its called, then things get exciting!

### Mouse Interaction

We can use `dot.mouse_x` and `dot.mouse_y`.

```python
#week2-mouse.py
from dorothy import Dorothy 
from cv2 import circle

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw) 

    def setup(self):
        print("setup")

    def draw(self):
        radius = 20
        x = dot.mouse_x
        y = dot.mouse_y
        circle(dot.canvas, (x,y), radius*2*2*2, dot.lavender, -1)
        circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
        circle(dot.canvas, (x,y), radius*2, dot.fuchsia, -1)
        circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
        
MySketch() 
```

### Over Time 

```dot.frame``` can be used to tell us **how many frames have been drawn since we started the program**

We can use that to move things over time. But what happens when the frame number is bigger than our canvas?!?!

```python
#week2-frame.py
radius = 10
x = dot.frame
y = dot.height-dot.frame
circle(dot.canvas, (x,y), radius*2*2*2, dot.lavender, -1)
circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
circle(dot.canvas, (x,y), radius*2, dot.fuchsia, -1)
circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
```
We can use the `modulo(%)` to loop back around

```python
x = dot.frame%dot.width
y = (dot.height-dot.frame)%dot.height
```

### Clearing the frame

When we never clear the frame, we end up with trails, which can be fun but often for the illusion of movement we want each frame to start fresh! We can use `dot.background(dot.white)` (or another colour!) to overwrite everything at the start of the `draw()` loop

```python
#week2-background.py
def draw(self):
    dot.background(dot.white)
    radius = 10
    x = dot.frame%dot.width
    y = (dot.height-dot.frame)%dot.height
    circle(dot.canvas, (x,y), radius*2*2*2, dot.lavender, -1)
    circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
    circle(dot.canvas, (x,y), radius*2, dot.fuchsia, -1)
    circle(dot.canvas, (x,y), radius, dot.blueviolet, -1)
```

## Strings

``Strings`` are used in Python to represent **text**. 

We tell Python that something is a ``string`` by surrounding it with quotation marks 

```python
"This is a string"
"singleword"
"123456789 is using the number characters, but everything inside the quotes is still a string"
```

### Concatenation 

Its a long word for a simple thing (welcome to coding!). 

This just means **joining strings together**. When we use `+` with numbers, it does a mathematical operation, when we use it with strings, it combines them!

## File Paths 

Outside of `print`, one great use of `Strings` is file paths!

Every item on your computer has an address that tells us how to get there from the root of your file system. 

For example ``/Users/student/documents/music/vanessa_charlton.mp3``

### Relative vs Absolute Paths

The one above is an **absolute** path. That means it provides the full location directly from the top. 

* This makes it specific to a certain file system / computer 

* This means it doesn't matter where the file is run from, the path will always be right

* They always start with a slash `/` (osx) `\` (windows)

However, we can also provide paths *relative* to where we have run the code from 

* `vanessa_charlton.mp3` if the mp3 is in the same location as where we run the code from (e.g. the terminal directory that you executed the `python` command). This is not the same as where the code lives. 

### Loading Audio

```python
dot.music.start_file_stream("audio/drums.wav")
```

### Reacting to the Volume

```python
#week2-audio.py
dot.background(dot.white)
r = int(200*dot.music.amplitude())
circle(dot.canvas, (dot.width//2, dot.height//2), r, dot.black, -1)
```


## Making Choices 

When we write code, we often make it to do one thing in one situation, and another thing in another situation. In other words, **making choices**. _Algo-choices_.

For example

* **If** a persons birthday is today, send them a card. 


* **If** a button is pressed, turn the lights on.


* **If** the robot detect a person, smile, **else** whistle awkwardly. 

### Conditionals

Including choices in our code formulated in this manner is **super useful** and are often called **Conditionals** (if you're fancy), or **If-else statements**. 

They follow the structure:

```python
if <some condition>:
    
    some code!
    
else:
    
    some more code!

```

So that is 


* first is the keyword `if`


* then comes the condition: e.g age == 18

    * this is a **Boolean** (more on that later); it is either True or False
    
    
* then comes a colon `:`


* everything that is indented is part of the conditional
    
* Python will only run the indented code if the condition holds
    

Or in actual Python Code

```python
birthday_month = "January"
this_month = "January"
if birthday_month == this_month:
    print("HAPPY BIRTHDAY!")
```

**Output**:
<code style="font-family: Monaco">
HAPPY BIRTHDAY!
</code>
```python
laser_strength = 3
if laser_strength == 0 :
    print("Phew")
elif laser_strength == 1:
    print("Ouch")
else:
    print("Now we're in trouble!")
```

**Output**:
<code style="font-family: Monaco">
Now we're in trouble!
</code>

### Find the middle 

Here we split the screen into 5 width ways and draw a rectangle in the middle if we are in middle segment and trigger drums.

```python
#week2-segment.py
def setup(self):
    print("setup")
    dot.music.start_file_stream("audio/drums.wav")
    dot.music.pause()

def draw(self):
    dot.background(dot.white)
    seg = math.floor((dot.mouse_x/dot.width)*5)
    print(seg)
    if seg==2:
        rectangle(dot.canvas, (dot.width//2-100,0),(dot.width//2+100, dot.height), dot.green, -1)
        dot.music.resume()
    else:
        dot.music.pause()
```

### Question

Can you work out how the mouse x coordinate is turned from 0 to 640 into 0 to 5? Can you find out what `math.floor()` does?
 
`seg = math.floor((dot.mouse_x/dot.width)*5)`
 
How could you change the range, for example, from 0 to 10? 

### Booleans 

Having previously seen `Ints`, `Floats`, and `Strings`, the first thing to pick up is our **fourth and final data type in Python!**. Its a `Boolean` and can **only have one of two values**. 

If Python data types were Pokemon, and there was only four of them, you would have caught them all. 

Booleans are either ``True`` or ``False``. That is it.

### Keywords 

We have been introduced to some new protected keywords in Python that are reserved for specific purposes. 

* `if` : The start of a conditional statement 


* `elif` : Any extra conditional statements (think **else if**)


* `else`: The last part of a conditional statement (if nothing else has been reached)


* `True`: A Boolean value representing a condition that is true 


* `False`: A Boolean value representing a condition that is false


### Indentation Matters

In our **If-else statements**, the code following the colon `:` starts on a new line, and is indented by one tab. 

Everything that is at this level of indentation will be exectued if the statement is true, up until the point that we return to the original indentation 


### Types of Comparison 

So far we have used conditional statements in the form ``a == b``. **IMPORTANT** to remember that 

* `=` is an assignment of a **variable** (e.g. `my_favourite_lecturer = "Louis"`) 


* `==` is an equality comparison (e.g ``if class_is_taught_by == "Louis"``)


There are some other ways we can compare things to make decisions that will either be **True or False**


* `a > b`: a is greater than b


* `a < b`: a is less than than b


* `a >= b`: a is greater than or equal to  b


* `a <= b`: a is less than or equal to b


### Threshold Volume

```python
#week2-cat.py
def setup(self):
    print("setup")
    dot.music.start_file_stream("audio/meow.wav")

def draw(self):
    dot.background(dot.white)
    print(dot.music.amplitude())
    if dot.music.amplitude() > 0.01:
        circle(dot.canvas, (dot.width//2,dot.height//2),200, dot.black, -1)
```

### Multiple Comparisons 

There are a few more **keywords** we can include in our logical expressions when building our conditionals

#### `and`

We can use the `and` keyword with multiple comparisons. This will only return `True` if **both** conditions are `True`, otherwise it will return `False`


```python
if a > 9 and b < 10:
    print("both are True")
else:
    print("one or both is False")

```

#### `or`

We can also use the `or` keyword with multiple comparisons. This will return `True` if **either one** of the conditions are `True`, otherwise it will return `False`

```python
if a > 9 or b < 10:
    print("one or both is True")
else:
    print("both are False")

```

#### `not`

You can also add the keyword `not` in front of your conditionals, which returns `True` if the conditional statement is **not True**

```python
if not a == 4:
    print("a isnt 4!")

```

### Four Quadrants
```python
def draw(self):
    dot.background(dot.white)
    #Top left
    if dot.mouse_x < dot.width//2 and dot.mouse_y < dot.height//2:
        rectangle(dot.canvas, (0,0),(dot.width//2,dot.height//2), dot.red, 10)
    #Bottom left
    elif dot.mouse_x < dot.width//2 and dot.mouse_y > dot.height//2:
        rectangle(dot.canvas, (0,dot.height//2),(dot.width//2,dot.height), dot.red, 10)
    #Top Right
    elif dot.mouse_x > dot.width//2 and dot.mouse_y < dot.height//2:
        rectangle(dot.canvas, (dot.width//2,0),(dot.width,dot.height//2), dot.red, 10)
    #Bottom Right
    else:
        rectangle(dot.canvas, (dot.width//2,dot.height//2),(dot.width,dot.height), dot.red, 10)
```

# Explorations 

We are now going to add some movement into our sketches! You can choose to either animate part of your existing Pictionary sketch, or start from scratch. 

There are some key ways we have learnt today that can add some animation to our sketches, and in both cases we will be able to test out our skills with ``if statements``

In all cases, we will also be adding our drawing into the `def draw(self):` function. This gets called repeatedly on a loop, so our drawing can keeping get refreshed. Below we detail approaches for how to update the shapes positions or colours.

#### Overwriting previous frames with `dot.background(colour)`

As we are drawing new things every frames, we might want to overwrite the old stuff! We can do this by calling `dot.background()` and passing in the colour we want the background to be

```
def draw(self):
    dot.background(dot.red)
```

#### Recording a video of the sketch

If you want to keep a record sketch, you can generate a video of it as in the `week2-audio.py` example:

```python
# week2-audio.py
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        dot.music.start_file_stream("audio/test.wav")
        dot.start_record()
        self.r = 0

    def draw(self):
        dot.background(dot.white)
        self.r -= (self.r*0.3)
        self.r += (10000*dot.music.amplitude())*0.3
        circle(dot.canvas, (dot.width//2, dot.height//2), int(self.r), dot.black, -1)
        if dot.frame == 175:
            dot.stop_record()

MySketch()
```

In this example, we start the recording with the method `dot.start_record()`, which is called in `setup`. In the drawing loop (`draw()`), after 175 frames, we stop the recording with `dot.stop_record()`.

## Explorations (choose one or more!)

The ``Dorothy`` library (stored in the `dot` variable), has properties that that relate to time, user input and audio. Think of these as `variables` that belong to the object. They are updated under the hood and we can use them to make our drawings move!

1. Audio Response

    * Find an audio file on your computer and use `dot.music.amplitude()` 
    
    * Use a new shape(s) to make an audio responsive drawing.

2. Mouse Interaction

    * We can use `dot.mouse_x` and `dot.mouse_y` to get the current mouse coordinates

    * We have seen how things can follow the mouse, or can get triggered when the mouse enters a certain area. 

3. Time 

    * `dot.millis` tells us how many milliseconds have passed since the start of the sketch. `dot.frame` tells us how many frames have passed (e.g. how many times the ``draw()`` function has been called). 
    
    * Make use of the `%` (modulo) operator which returns the remainder of the division between the two operators. This is useful when we have a number that is always rising (e.g `dot.frame`) and we want it to loop back to zero after a given maximum.
