# Week 5 Audio and Perception

## Revisiting For Loops

### One piece of code, applied over a whole list

When we want to analyse audio files, with **44100 values a second** we dont want to have to write code to change each sample by hand. Writing code to address every sample individually would be time consuming and pointless!

That's too much!

However, if we want to do something over time and **not hand write new code every step**, we can use a control structure common in lots of coding, and especially useful in **time based media**

- Audio

- Video

- Games

### In Code

Here is an example of a `for loop` that iterates over a `List` representing the samples from an audio file. Each time round the loop, the sample value is stored in the variable `sample`. Here we conduct some analysis by passing it to the hypthetical `analyse()` function.

```python
soundfile = librosa.load("my_audio.wav")
for sample in soundfile:
    analyse(sample)
```

If we didnt use a `for loop` we would have to do each sample by hand in code. It would be a massive program!

```python
soundfile = librosa.load("my_audio.wav")
analyse(soundfile[0])
analyse(soundfile[1])
analyse(soundfile[2])
analyse(soundfile[3])
.....
analyse(soundfile[n])

```

We can do multiple actions on each loop. We can tell which part of the loop we are ay by paying attention to the indentation.

```python
soundfile = librosa.load("my_audio.wav")
for sample in soundfile:
    data = analyse(sample)
    other_data = more_analysis(sample)
    if data > other_data:
        trigger_event()

```

## Windows (or Buffers)

Unfortunately, looking at an individual sample, or changes sample to sample, **often doesn't tell us much**. Semantically interesting events tend to happen over much **longer periods**.

So we can slice our audio into short **windows or frames**, then compute statistics based on a much longer time frame. It means we are more likely to have enough information to capture something meaningful happening, and we're not having to deal with so much information.

Here, we grab the first 1024 samples and get the **mean amplitude**

```python
window_size = 1024
buffer = audio_data[0:window_size]
mean = (buffer**2).mean()
print(mean)
```

### Generating Buffers

We're going to want to do the same for the whole audio file! In order to go through all the buffers with minimal code, we can use a `for loop`.

Here, we use a built in method (`librosa.util.frame()`) to generate the buffers first. We then use a `for loop` to iterate over this collection of frames. Each time we go round the loop a subsequent window of audio is stored in the `buffer` variable.

It returns a matrix (2D array) that is `window_size x num_buffers`, but we want to iterate over each buffer one by one. We take the `transpose()` of the matrix to [swap the rows and columns](https://www.mathsisfun.com/definitions/transpose-matrix-.html).

```python
window_size = 1024
windows = librosa.util.frame(audio_data, frame_length=window_size, hop_length=window_size)
windows = windows.transpose()
amps = []
for buffer in windows:
    mean = (buffer**2).mean()
    amps.append(mean)
```

We can see how this might be used to draw a waveform here.

```python
#week5-offline-waveform.py
def setup(self):
    audio, sr = librosa.load("audio/keys4.wav")

    window_size = 2048
    windows = librosa.util.frame(audio, frame_length=window_size, hop_length=window_size)
    windows = windows.transpose()
    amps = []
    for buffer in windows:
        mean = (buffer**2).mean()
        amps.append(mean)

    self.waveform_layer = dot.get_layer()
    for i, val in enumerate(amps):
        #Where to draw horizontally (time)?
        x = int(i*dot.width/len(windows))
        #How much height?
        h = int(val*dot.height)*10
        #Centre vertically
        y = dot.height//2 - h//2
        line(self.waveform_layer, (x, y), (x, y + h), dot.red, 2)
    dot.music.start_sample_stream(audio, sr=sr)

def draw(self):
    dot.background(dot.black)
    #Draw playhead (col=None for waveform e.g. dont draw)
    dot.draw_waveform(dot.canvas, col = None, with_playhead = True)
    #Draw semi-transparent waveform (0.8 alpha)
    dot.draw_layer(self.waveform_layer, 0.8)
```

There are also a couple of new `Python` and `Dorothy` things to see here.

#### `enumerate()`

For when we want to iterate over a `List` and we want

1. The item as we go

2. The index of that item

And in this case, we need the `item` (how load is the track) and the `index` (at what point in time is it?).

```python
for i, val in enumerate(amps):
```

#### `dot.get_layer()` and `dot.draw_layer()`

Sometimes we might not want to draw directly to the `dot.canvas`. Here, we want to render the waveform once using the audio information. then redraw it every frame to account for the moving playhead.

We can avoid calculating the drawing positions everytime by using `dot.get_layer()` to first get an empty layer (basically a new canvas), draw to this in the `setup()` function and save.

We then `dot.draw_layer(self.waveform_layer, 0.8)` in the `draw()` function, with the second argument being an alpha value for transparency.

## Spectral Information

There are limitations of amplitude analysis. One of the major issues here is that there are changes in audio that **might** be important, but that aren’t necessarily reflected in the amplitude values very strongly. One example is pitch.

A musical melody might have lots of **different pitches** in it, but they might **not look any different in terms of amplitude** (unless they naturally have gaps between them). So, importantly, what kind of information is this, and how can we go about finding it in the signal? Beyond this:

- What different frequencies are present?
- What are the timbral qualities of the sound?
- Where are the main percussive events?
- What's the tempo?
- Where are the beats?
- What instruments are playing?

### FFTs

There are lots of ways of trying to extract frequency information from an audio buffer. The most important method is known as the **Fourier Transform**.

For a small window of time, we are able to get the strength of different frequencies present between various ranges, or bins.

The number of bins we get, and how much frequency they each cover, is a factor of the size of the window we analyse. As such, we must make a choice between resolution in the time domain (smaller windows allow us to spot shorter changes in the input signal), and resolution in the frequency domain (smaller bands allow us to be more specific about which frequencies are present).

## Audio Analysis in Dorothy

As you play music in `Dorothy`, some audio analysis is happening under the hood in realtime as we listen. Everytime we call the functions from the `draw()` loop, we get the current values.

### Amplitude

We have already seen this function which provides the current volume / amplitude at any given time. This returns a float number

```python
dot.music.amplitude()
```

### FFT

Similarly, there is a function to return the current FFT Magnitudes. This returns a list of numbers (each relating to the strength of a given frequency).

```python
# week5-online-fft.py
def setup(self):
    file_path = "audio/gospel.wav"
    dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)

def draw(self):
    dot.background(dot.black)
    for bin_num, bin_val in enumerate(dot.music.fft()[:256]):
        pt1 = (bin_num*5, dot.height)
        pt2 = (bin_num*5, dot.height-int(bin_val*200))
        line(dot.canvas, pt1, pt2, (0,255,0), 2)
```

### Timing and Beats

If we have loaded in an audio file, it is first beat tracked. We can then call the function `is_beat()` in the `draw()` loop and it will tell us if a beat is occuring during this frame so we can trigger something in the visuals.

```python
# week5-online-beats.py
def setup(self):
    file_path = "audio/disco.wav"
    dot.music.start_file_stream(file_path, fft_size=512)
    self.show_beat = 0

def draw(self):
    col = dot.black
    if dot.music.is_beat():
        self.show_beat = 10

    if self.show_beat > 0:
        col = dot.white

    dot.background(col)
    self.show_beat -= 1
```

### Custom Analysis

You can use the `on_new_frame()` callback on the `audio_device` to get whatever audio buffer is playing at the moment and then use other functions from `librosa`.

Here is an example getting the `chroma`. This gives us a magnitude for each pitch class (A -> G) so it is good for harmonic information

```python
# week5-online-chroma.py
def setup(self):

    audio = sine_step()

    id = dot.music.start_sample_stream(audio, sr=22050, buffer_size = 2048)
    self.chroma = np.zeros(12)
    #Called everytime the audio engine returns a buffer
    def on_new_frame(buffer=np.zeros(2048)):
        print(buffer.shape)
        self.chroma = librosa.feature.chroma_stft(y=buffer, n_fft=512).mean(axis=1)

    dot.music.audio_outputs[id].on_new_frame = on_new_frame

def draw(self):
    dot.background(dot.white)
    for i,c in enumerate(self.chroma):
        x = (dot.width//12)*i
        y = int(dot.height - (dot.height*c))
        line(dot.canvas, (x, dot.height), (x, y), dot.red, 10)
```

## Exploration

Possible things to explore this week are below. You can try most either reactively to the most recent information (e.g. using `dot.music.amplitude()` and `dot.music.fft()`), or visualise the whole track at once (see the `week5-offline-fft.py` and `week5-offline-waveform.py`).

1. Explore how the amplitude of a track or live audio can influence the movement and growth of visual elements on the screen. Think about how shapes or lines might expand, contract, or change position in relation to changes in volume.

   - `dot.music.amplitude()` is useful here
   - Can be continuously reactive, or events can happen when the amplitude crosses a threshold (using an `if` statement)

2. From an FFT, experiment with how different frequency bands can control various aspects of the visualisation, such as colour, shape, or texture. You might assign certain colours to specific frequency ranges or create a system where high and low frequencies generate contrasting visual elements.

   - `dot.music.fft()` is useful here. Iterate over the this list using a `for` loop.

3. Create a visual system that responds to beats or rhythmic patterns in music. Focus on how repetition, symmetry, or geometric patterns can emerge in response to the tempo or percussive elements. You could explore how different beats might trigger different types of visuals or how patterns shift as the music becomes more complex.

   - `dot.music.beats` holds a `List` of all the samples locations of the predicted beats
   - `dot.music.is_beat()` can be called in the `draw()` loop to see if a beat has happened during this frame.

4. Visualise a full track by designing shapes or forms that represent different musical sections or elements. For instance, you could map out the structure of a song using a series of evolving shapes that change based on the progression of the music. Think about how the arrangement of the track – from intro to climax – might translate into visual transformations over time.

   - `dot.music.audio_outputs[0].y` holds all the samples for the currently loaded track
