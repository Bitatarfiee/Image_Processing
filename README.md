# Image_Processing
Help functions and codes in image data

# files
## Image_Filter_Gaussian_SobelY_SobelX.py
What do the three filters (Gaussian, SobelX, SobelY) do to the original image?\
Gaussian filter is used for denoising, Here we can see that by applying gaissian filter to the image, the image is smoother than the original image.\
Sobel X & sobel Y are spatial filters for edge detection in horizontal and vertical directions. Here, we can better see the edge and features of the image on the horizontal axis in the second image, and in the third image, the edge and features on the vertical axis.

### libes 
from scipy import signal
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt


## Image_Matplotlib.py: Plotting images
Image visualization with matplotlib
- making subplot  
- 

### libes
import matplotlib.pyplot as plt


## public_imagedataset_cifar10.py:
Load Public data for image analysis and getting test image 

Images used in this code are from CIFAR 10.
CIFAR 10: The CIFAR-10 dataset contains 60,000 32x32 color images in 10 different classes. The classes represent airplanes, cars, birds, cats, deer, dogs, frogs, horses, ships, and trucks. There are 6,000 images in each class. 
CIFAR-10 dataset: https://en.wikipedia.org/wiki/CIFAR-10

### libes
from scipy import misc
image = misc.ascent()
from keras.datasets import cifar10
import numpy as np


## Image_Preprocessing.py:
- convert image from uint8 to unit16 to float32
- Change range of pixel values to [-1,1]
- One hot encoding

### libes 
from tensorflow.keras.utils import to_categorical

