# Week 3 Lists and Loops

## Lists 

Up until this point, all of our variables have **only referred to one value**. 

This gets us so far, but in reality, we often want to refer to a **collection** of multiple things. In Python, we use something called a `List` so store and access these types of things. 


* The `audio_data` variable we loaded in last week is **list of samples**


* If we were looking at a **whole theatre database**, not just a single member one at a time, we would store them **as a list** in a variable called `members`.


* Technically, a `String` is a **List of characters**, but we'll leave that for another day!


The cool thing about `Lists` is that we can store the **whole list** in a named variable, and then use **indexes** to access items 

### Making a list

A list sit between two `square brackets []` with each item separated by a `comma ,`

### Indexing 

We can access items in an array by using ``numerical indexes`` in `square brackets []`. 

One things to be wary of:

#### In computer science, we start counting at 0

That means the first item in a list is

``my_list[0]``

And the second item in the array is 

``my_list[1]``

If you give an index that is longer than the list, **you will get an error!**

Like any other variable, **you can also overwrite** items in a list 

``
my_list[0] = 1
``

``
camera_locations[3] = "hilltop"
``

### Adding new values 

We can also **extend** and existing list using the `append()` function 

### Example

Here we define a List called `positions` in the `draw()` function. To pick a new index each time, we can use the `dot.frame` counter to iterate through the List, picking a new position each time.

We use the `%` here both to loop the frame counter when it goes above the length of the list, and also with an `if statement` to only update every 10 frames (less chaotic!).

```python
#week3-dots.py
dot = Dorothy() 
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        pass

    def draw(self):
        positions = [0,80,160,240,320,400,480,560,640]
        
        #Only change every 10 frames
        if dot.frame % 10 == 0:
            dot.background(dot.darkblue)  
            #Loop around      
            x = positions[dot.frame%len(positions)]
            y = dot.height//2
            circle(dot.canvas, (x, y), 10, dot.white,-1)
             
MySketch() 
```

## For Loops

### One piece of code, applied over a whole list
But what if we wanted to draw them all? And we didn't want to copy the code out 9 times with a new index each time?

We can read the code below as 

* Take each item in the list one by one

* Save it in the variable `item`

* Execute the function `do_something()` on it

```python
my_list = [1,2,3,4,5]
for item in my_list:
    do_something(item)
```

This is same as above, but in more code! And the for loop works, not matter how long the list is!

```python
my_list = [1,2,3,4,5]
do_something(my_list[0])
do_something(my_list[1])
do_something(my_list[2])
do_something(my_list[3])
do_something(my_list[4])
```

### Example

```python
#week3-forloop.py
for x in positions:
    y = dot.height//2
    circle(dot.canvas, (x, y), 10, dot.white,-1)
```

Or for a more interesting set of points. Here, each item in the list is a set of 2 coordinates. So when we iterate through, we can further index each `pt` to get the `x` (first item, `pt[0]`) and `y` (second item, `pt[0]`)

```python
#week3-face.py
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
```

## Class Variables and The `self`

If we wanted to update the `y` position of these over time, for example, to make the illusion of falling snow, we could have a list of the y coordinates and then update these everytime in the `draw()` loop. 

```python
#week3-static-snow.py
def draw(self):
    dot.background(dot.darkblue)
    snow = [[0,0],[80,0],[160,0],[240,0],[320,0],[400,0],[480,0],[560,0],[640,0]]
    for pt in snow:
        circle(dot.canvas, pt, 10, dot.white, -1)
        #update the y position by 10 
        snow[i][1] = (snow[i][1] + 10) % dot.height  
```  
But theres a problem! These lists are initialised in the function, so everytime they start from scratch and any changes are forgotten about! If we want something that persists outside of this loop we can make an `instance variable`. This is attached to the object (in this case `MySketch`) and changes are kept beyond each loop. 

We use the `self` keyword to refer to the current object, and initialise in the `setup()` function.

```python
#week3-line-snow.py
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        self.snow = [[0,0],[80,0],[160,0],[240,0],[320,0],[400,0],[480,0],[560,0],[640,0]]

    def draw(self):
        dot.background(dot.darkblue)
        ptr = 0
        for pt in self.snow:
            circle(dot.canvas, pt, 10, dot.white, -1)
            #update the y position by 10 
            self.snow[ptr][1] = (self.snow[ptr][1] + 10) % dot.height
            ptr = ptr + 1      
```
We could also add some interest by adding a random number each time, instead of the constant so we get some variation and they don't all just fall in line
```python
#week3-random-snow.py
import random
.....
for pt in self.snow:
    circle(dot.canvas, pt, 10, dot.white, -1)
    #update the y position by random between 0 and 5
    move_by = random.randint(0,5)
    self.snow[ptr][1] = (self.snow[ptr][1] + move_by) % dot.height
```

## Generating Lists 

We have some hardcoded lists that are *fine*, but our snow isn't that plentiful yet! Rather than writing out lots more points, we can use functions in the `numpy` library to generate some lists of numbers, either following some simple rules, or randomly. 

We include 

```python
import numpy as np
```
At the top to say we want to use the functions from the `numpy` library. We also add the `as np` to specify an alias. This means we can refer to is as `np` in the code.

### Equally spaced numbers

Here, to get the spread across the `x` axis, we use `np.linspace` specifying `(start, end, step)`. We use `np.zeros` to initialise the `y` axes to all 0. 

We then combine all the points into a single list of points using the `zip` and `append` functions

```python
#week3-more-snow.py
def setup(self):
    num_flakes = 100
    #convert to ints 
    x = np.linspace(0,dot.width,num_flakes).astype(int)
    y = np.zeros(num_flakes).astype(int)
    self.snow = []
    #iterate through both and combine into the variable pt
    for pt in zip(x,y):
        self.snow.append(list(pt))
    print(self.snow)

def draw(self):
    dot.background(dot.darkblue)
    ptr = 0
    for pt in self.snow:
        circle(dot.canvas, pt, 10, dot.white, -1)
        #update the y position by random between 0 and 10
        move_by = random.randint(0,10)
        self.snow[ptr][1] = (self.snow[ptr][1] + move_by) % dot.height
        ptr = ptr + 1     
```

### Vary speed with randomness
The random move it not very smooth, so we want different speeds, but for the different speeds within the flakes to be constant. 

One solution is to generate some random speeds at the beginning that remain constant for each flake through. We look up each time in the `for loop` to find how mich to `move_by`.

`np.random.randint()` takes `(low, high, size)` to generate sets of random numbers.

```python
#week3-speed-snow.py
def setup(self):
    num_flakes = 100
    x = np.linspace(0,dot.width,num_flakes).astype(int)
    y = np.zeros(num_flakes).astype(int)
    self.speed = np.random.randint(1, 7, 100)
    self.snow = []
    #iterate through both and combine into the variable pt
    for pt in zip(x,y):
        self.snow.append(list(pt))

def draw(self):
    dot.background(dot.darkblue)
    ptr = 0
    for pt in self.snow:
        circle(dot.canvas, pt, 10, dot.white, -1)
        move_by = self.speed[ptr]
        self.snow[ptr][1] = (self.snow[ptr][1] + move_by) % dot.height
        ptr = ptr + 1 
```

We can also initialse y as random to avoid the grouping 

```python
y = np.random.randint(0, dot.height, num_flakes)
```

## Extras

### Use speed for size 

We can use the speed for size as well. The different speeds kind of imply some depth and we can further highlight this by making those in the foreground big and fast and those further back slow and small

```python
circle(dot.canvas, pt, self.speed[ptr], dot.white, -1)
```
### Alpha trails 

Finally, we can add a trail by adding a partially transparent layer over top each time, as opposed to completely wiping with `dot.background()` at the top

Here we use `dot.get_layer()` to get a new layer (the same size as `dot.canvas`), we draw to that instead and then use `dot.draw_layer` to draw it over the top of `dot.canvas`, adding in an argument to make its `alpha` value 0.1. This ranges from 0 (transparent) to 1 (fully opaque).

```python
#week3-final-snow.py
def draw(self):
    ptr = 0
    for pt in self.snow:
        speed = self.speed[ptr]
        circle(dot.canvas, pt, speed, dot.white, -1)
        self.snow[ptr][1] = (self.snow[ptr][1] + speed) % dot.height
        ptr = ptr + 1  
    cover=dot.get_layer()
    rectangle(cover, (0,0),(dot.width, dot.height),dot.darkblue, -1)
    dot.draw_layer(cover,0.1)   
```

# Explorations 

1. Experiment with different values 

    * Colours 

    * Ranges 

    * Shapes 

    * Sizes

    * Random bounds 

    * Alpha 

2. Experiment with removing randomness 
    
    * What happens if you make the starting positions and movement for uniform

    * This involves changing `y` and `self.speed` to something using `linspace`, or even something constant across all the values

3. Change the dimensions 

    * Can you update to move left to right?

    * Or bottom to top? 

    * What natural phenomenom would this kind of movement remind you of?

4. Add in some audio responsiveness

    * Using the `dot.music.amplitude()` from last week, can you make the sketch **also** change based on the value of the music?

5. Stripping it back to the the base concept of `points moving together`, what other animations could you make?