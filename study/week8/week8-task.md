# Working with Linear Transformations Over Time

### Simple Example 

[Basic Example](week8-transformations.py)

In ``Dorothy``, to work with linear transformations we follow this approach 

1. Get a new canvas (``dot.get_layer()``)

2. Draw to it 

3. Apply transformations (``dot.transform()``)

4. Put back onto main canvas (``dot.draw_layer(new_canvas)``)

#### Task 1

Experiment with the Basic Example above. 

* Try both the ``scale`` and ``rotate`` transformations. 

* Can you combine them by into one transformation by matrix multiplication?

* Try different ``origins``. How do the transformations differ when the origin is in the top left (``0``, `0`), or in the center (``dot.width//2``, ``dot.height//2``)?
  

### Exploring Origins And Multiple Transformations

[Rotate All Example](week8-rotation-whole-canvas.py)

[Rotate Individually Example](week8-rotation-in-grid.py)

Here we have two similar but **importantly different** examples. The first shows us draw a grid of squares onto **one canvas** and rotate around the centre point. 

The second shows each square in the grid being drawn onto its **own new canvas**. We then move the origin to the centre of that square and rotate. This means each square rotates individually about its centre, and opposed to all together around the sketches centre.  

[Radial Faces Example](week8-radial-faces.py)

Here we draw the face in the sample place (100,100) each time, but then rotate each canvas by a different amount (with an origin in the centre). This creates a fun radial animation

#### Task 2
Examine the code and make sure you understand the difference between the two sketches. 

## Explorations

Experiment with using linear transformations

1. Can you integrate linear transformations into one of your earlier projects?

2. What happens when you move around the origin of the transformation?

3. Can you create patterns by offsetting rotations or transformations of different elements in the screen?

4. Can you make the transformations responsive to user input (mouse?) or audio?