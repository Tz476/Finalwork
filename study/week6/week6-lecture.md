# STEM for Creatives Week 6 - Images

### Pixels

As we saw with audio, when we break media down on computers, they are just multi-dimensional arrays. Whilst audio is often 1-dimensional (or more for multi-channel audio), images have more components to them.

Whilst digital audio is made up of **samples**, digital images are made up of **pixels**. When we are dealing with black and white images (often known as **grayscale**), each image is a **2D array**, which each dimension relating to

- row (height)
- column (width)

If we store the pixels of a grayscale image in an array named `I`, then the grayscale value (e.g., 0 for black) of pixel in row `i` and column `j` is stored in`I[i,j]` . Each item in this array represents a pixel and its number tells us where on the scale of black (low) to white (high) it is. We can use different types of numbers to represent each pixel but often the scale is 0 - 255.

### PIL (Python Imaging Library)

We can use PIL to import and display images, and then turn them into **NumPy** arrays. And we know how to do things with them!

```python
#This is actually a colour image, so we make it grayscale to begin with (convert('L'))
im = np.array(Image.open('week6/images/space.jpg').convert('L'))
```

```python
#How big is it?
h = im.shape[0]
w = im.shape[1]
print(w, h)
```

We can also use PIL to turn an array into an image:

```python
# Create a new image 10x10 pixels with random RGB values
a = np.random.randint(0, 255, (10, 10, 3), dtype=np.uint8)
Image.fromarray(a).show()
```

### Colour (RGB)

Sure grayscale is good, but have you tried colour? In the RGB representation an image is made up of three channels

- **R**ed
- **G**reen
- **B**lue

So in a way its actually like 3 images, that combine together to make the full colour output. We can get all colours from combinations of these three base colours.

### Colour Channels

So how does effect our NumPy array? We end up with a **3D array**, whose dimensions map to

- row (height)
- column (width)
- color (channel)

## Making a Photo Mosaic

Next we will build up some code you to create a photomosaic.

A chosen image will get reconstructed using a seperate dataset of images that you specify. These images are used for the tiles in the photomosaic, and they are selected based on image with the closest mean colour to the target pixel.

The code here is a modified version of code from this repository: https://github.com/MstrFunkBass/facemo

### Step 1 Downsampling

First we need to downsample the source image so it has less pixels. As our plan is swap each source pixel for a matching image from the dataset, it is in our interest to have less of them!

To do this, we will just skip pixels at regular intervals. This does lose some information, but is really efficient and turns out to work fine for our purposes.

#### Skip indexing

`array(start,end,step)`

Here we use the code `source[::skip,::skip]` to say "Get me all of the pixels, skipping at a given interval.

Play with the `skip` variable to see the effects of different down sampling. The display in the notebook is not quite accurate however. As we downsample, we are making smaller images (less pixels). To display we have sclaed back up to the original size.

```python
#week6-downsample.py
skip = 20
downsampled = rgb_image[::skip,::skip]
print(f"skipping leaves us with {downsampled.shape}, we can resize back to original size")
downsampled = Image.fromarray(downsampled).resize((w,h), Image.NEAREST)
```

### Step 2 Getting a dataset

We have some code which walks through a file and finds and the images, scales them all to the same size (and smaller) and stores them in a dataset.

This is a dataset of [images of animals from kaggle](https://www.kaggle.com/datasets/iamsouravbanerjee/animal-image-dataset-90-different-animals) that have been resized into thumbnails (for faster download and processing). The full dataset should contain 5400 images.

```python
dataset = dot.get_images("week6/data/animal_thumbnails/land_mammals")
print(f"the dataset has 4 dimensions: {dataset.shape} (images x width x height x channels)")
```

### Step 3 Find Average Colour Of Each Image

To help us find which image from the dataset should replace each pixel in the source, we are going to find out what the **average red, green and blue** values are for each image. We need to do this for each channel to maintain the colour information. We will then use this to match to the **red, green and blue** values of each pixel in the downsampled source image.

#### `np.apply_over_axes()`

We we will us a `numpy` function called `apply_over_axes()` to apply our `np.mean` function to only certain channels of our 4d array.

If we did `np.mean()` to the whole dataset, we'd just get one value!

We can get the average of all the images in our dataset by applying it to the `first axis [0]`

```python
#week6-mean-dataset.py
mean_image =  np.apply_over_axes(np.mean, dataset, [0])
```

But what we actually want is to apply it to the second and third axes. This averages the pixel information over the `width` and `height`, but maintains the separation of `images` and `channels`.

We end up with an array that is `images x 1 x 1 x channels`. We can use `np.squeeze` to remove those two in the middle.

```python
#week6-mean-colours.py
mean_image =  np.apply_over_axes(np.mean, dataset, [1,2])
```

### Step 4 Match Images to Pixels

Next we have to do the matching! We will use `binary tree search` to do this efficiently, no need to know how this works in detail for now.

We build a `tree` from the `mean_rgb_dataset`, and then `query()` with each pixel from the source to get the `k` closest matches. We then randomly pick one and save the index of the matched image for building the mosaic in the next step.

#### Nested `for loops`

Last week we saw how to use `for loops` to iterate over a `1D list` (e.g. an audio file). This enabled us to write one piece of code that got applied to each window of audio in turn.

Images can be seen as `2D lists`, so we can actually use 2 `for loops` to write code to address each pixel in turn! One `for loop` is `nested` inside the other.

The code below first starts on the top row, then the second `for loop` loops over each column. When it has done each column in the first row, the second loop is over and the first loop then moves onto the second row. We then move through each column again, until we have done all the rows.

```python
for row in range(w):
    for col in range(h):
        pixel = mosaic_template[row, col]
```

```python
#week6-mosaic.py
#Build the search tree
tree = spatial.KDTree(mean_rgb_dataset)

#Variables to store which image is assigned to which pixel
mosaic_template = np.swapaxes(mosaic_template,0,1)
w,h = mosaic_template.shape[0:2]
matched_images = np.zeros((w,h), dtype=np.uint32)
#Go through each pixel and find the closest matching thumbnail image by mean colour and assign the index into the 2D array
k = 40
for row in range(w):
    for col in range(h):
        pixel = mosaic_template[row, col]
        #Get the match
        match = tree.query(pixel, k=k)
        pick = random.randint(0, k-1)
        matched_images[row, col] = match[1][pick]
```

### Step 5 Build the Mosaic

Now we need to stitch all those matched images together into our mosaic. Again a `nested for loop` is useful to work through our `2D data` (again, the pixels of the source image).

For each pixel, we retrieve the index of the match from `matched_images`. We then get the original thumbnail and `paste()` it into the right grid square on our `mosaic`.

```python
#week6-mosaic.py
#Go through each pixel in the array of thumbnail<>pixel indexes and then assign all the pixels of the thumbnail into the final array
for i in range(w):
    for j in range(h):
        matched_image = dataset[matched_images[i, j],:,:,:]
        #Coordinates to place the thumbnail
        x, y = i*thumbnail_size[0], j*thumbnail_size[1]
```

# What to do next?

You can use `week6-mosaic.py` or `week6-mosaic-write-file.py` to make some of your own photo mosaics. You can adjust the following variables to customise. If your target image is a high resolution you may want to increase the downsample rate

When using `Dorothy` in `week6-mosaic.py`, you are limited by the size of the screen. When you write to file (`week6-mosaic-write-file.py`) then your file can be as big as you want (saved as `mosaic.png`)! This may be the way to go for large source images, larger thumbnail sizes, or low downsample rates. If you are running `week6-mosaic.py` and you only see the small portion of your image, try writing to file, its probably ending up off screen!

```python
src_image_path = "path/to/yourimage"
dataset_path = "path/to/yourdataset"
thumbnail_size = (w,h)
downsample_amount = 20
```

Experiment with this code and adjust some of the parameters to see how it affects the creation of the mosaic. You can re-run the same functions with different parameters and paths to files without having to write any new code!

- **Step 1**: adjust the thumbnail size and downsample rate. _Warning_ if you make the downsample rate too small or the thumbnail size too big you may be waiting a very long time for it to create! -- You may have to kill the code and restart the code if this happens.

- **Step 2**: Look at the folder structure for the dataset of animal images. Can you make a mosaic with a subset of this data. **Tip** try changing the subset of animals you are using in the original dataset. Can you create a mosaic only out of images of one kind of animal?

- **Step 3**: Find a new target image to be reconstructed with the animals dataset.

- **Step 4**: Find a new dataset of images to use for using as the thumbnail tiles in the mosaic.

### How to find / create a new image dataset:

- [kaggle.com](http://kaggle.com): which contains lots of [image datasets](https://www.kaggle.com/datasets?search=image)

- Pinterest or instagram — you can download sets of images easily using the [pindown chrome extension](https://chrome.google.com/webstore/detail/pindown/flieckppkcgagklbnnhnkkeladdghogp?hl=en)

- [UAL’s digital collections](https://digitalcollections.arts.ac.uk/collections/)

- [Some other image libraries available to UAL students](https://arts.ac.libguides.com/az.php?t=13317)

- [The internet archive](https://archive.org/) — you can use these [helper python scripts](https://github.com/terrybroad/internet-archive-downloader)

- You can [extract the frames from a video](https://youtu.be/ck11jOVYlIw) using the [super-useful software ffmpeg](https://ffmpeg.org/)
