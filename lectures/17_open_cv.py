# ****************************************OpenCV***************************************************

# This lecture is introduces OpenCV (Open Source Computer Vision Library), which is an open source
# computer vision and machine learning software library. OpenCV was built to provide a common
# infrastructure for computer vision applications and to accelerate the use of machine perception
# in the commercial products.

# OpenCV is written in C++ and its primary interface is in C++, but it still retains a less
# comprehensive though extensive older C interface. There are bindings in Python, Java and
# MATLAB/OCTAVE.

# OpenCV-Python is the Python API of OpenCV. It combines the best qualities of OpenCV C++ API and
# Python language.


# Compared to other languages like C/C++, Python is slower. But another important feature of Python
# is that it can be easily extended with C/C++. This feature helps us to write computationally
# intensive codes in C/C++ and create a Python wrapper for it so that we can use these wrappers as
# Python modules. This gives us two advantages: first, our code is as fast as original C/C++ code
# (since it is the actual C++ code working in background) and second, it is very easy to code in
# Python. This is how OpenCV-Python works, it is a Python wrapper around original C++
# implementation.
#
# And the support of Numpy makes the task more easier, which is a highly optimized library for
# numerical operations. All the OpenCV array structures are converted to-and-from Numpy arrays. So
# whatever operations you can do in Numpy, you can combine it with OpenCV, which increases number
# of weapons in your arsenal.

# So OpenCV-Python is an appropriate tool for fast prototyping of computer vision problems.
from typing import List, Tuple

import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_image(im, h=8, title='', **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y / x) * h
    plt.figure(figsize=(w, h))
    plt.imshow(im, interpolation="none", **kwargs)

    plt.axis('off')
    plt.title(title)
    plt.show()


# when we read an image with opencv we get a numpy array object
image = cv2.imread('data/rgb.png')
print(type(image))
print(image.shape)

# *********************************Part 1: Basic Operations****************************************


# Changing Colorspaces
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(np.all(rgb[..., 0] == image[..., 2]))
print(np.all(rgb[..., 1] == image[..., 1]))
print(np.all(rgb[..., 2] == image[..., 0]))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(gray.shape)
plot_image(gray, title='Gray')

# Image Thresholding


# cv2.threshold - first argument is the source image, which should be a grayscale image,
#                 second argument is the threshold value which is used to classify the pixel values
#                 third argument is the maxVal which represents the value to be given if pixel value
#                 is more than (sometimes less than) the threshold value

# OpenCV provides different styles of thresholding and it is decided by the fourth parameter of
# the function. Different types are:

# - cv2.THRESH_BINARY
# - cv2.THRESH_BINARY_INV
# - cv2.THRESH_TRUNC
# - cv2.THRESH_TOZERO
# - cv2.THRESH_TOZERO_INV


_, thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
_, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
_, thresh3 = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)
_, thresh4 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)
_, thresh5 = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [gray, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# Adaptive Thresholding

# When we using simple thresholding, then we are fixing global threshold value for thw whole image.
# But it may not be good in all the conditions where image has different lighting conditions in
# different areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate
# the threshold for a small regions of the image. So we get different thresholds for different
# regions of the same image and it gives us better results for images with varying illumination.

# Adaptive Method - It decides how thresholding value is calculated.
# - cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.

# - cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values
#                                    where weights are a gaussian window.


_, th1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [gray, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

# Scaling

# Scaling is just resizing of the image. OpenCV comes with a function cv2.resize() for this
# purpose. The size of the image can be specified manually, or you can specify the scaling factor.
# Different interpolation methods are used. Preferable interpolation methods are cv2.INTER_AREA
# for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. By default,
# interpolation method used is cv2.INTER_LINEAR for all resizing purposes.

res = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
print(f'original image shape: {image.shape}')
print(f'changed image shape: {res.shape}')

# 2D Convolution

# OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image.

kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(image, -1, kernel)

plt.subplot(121)
plt.imshow(image)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.imshow(dst)
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.show()

# Image Blurring

# Image blurring is achieved by convolving the image with a low-pass filter kernel. It is useful
# for removing noise. It actually removes high frequency content (e.g: noise, edges) from the image
# resulting in edges being blurred when this is filter is applied. (Well, there are blurring
# techniques which do not blur edges). OpenCV provides mainly four types of blurring techniques.

# 1 - Averaging

blur = cv2.blur(image, (5, 5))

plt.subplot(121)
plt.imshow(image)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.imshow(blur)
plt.title('Blurred')
plt.xticks([]), plt.yticks([])

plt.show()

# 2 - Gaussian Filtering

blur = cv2.GaussianBlur(image, (5, 5), sigmaX=0)

# 3 - Median Filtering

median = cv2.medianBlur(image, 5)

# Morphological Transformations

kernel = np.ones((5, 5), np.uint8)

# 1 - Erosion

erosion = cv2.erode(gray, kernel, iterations=1)
plot_image(erosion, title='Erosion')

# 2 - Dilation

dilation = cv2.dilate(gray, kernel, iterations=1)
plot_image(dilation, title='Dilation')

# 3 - Opening

opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
plot_image(opening, title='Opening')

# 4 - Closing

closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
plot_image(closing, title='Closing')

# Canny Edge Detection

edges = cv2.Canny(gray, 100, 200)
plot_image(edges, title='Detected Edges')


# TODO: Look at other tutorials using the following link:
# TODO: https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html


# *******************************Part 2: Image Segmentation****************************************

# In this part of lecture I will demonstrate how we can use image processing for detecting text
# zones on image.

def contours_to_segments(contours: List[np.ndarray],
                         x_margin: int = 0,
                         y_margin: int = 0) -> List[Tuple]:
    """Derive bounding boxes of contours."""
    segments = list(map(cv2.boundingRect, contours))
    return [
        (max(0, r[0] - x_margin), max(0, r[1] - y_margin), r[2] + x_margin, r[3] + y_margin)
        for r in segments]


def draw_segments(im: np.ndarray,
                  segments: List[Tuple],
                  color: Tuple = (255, 0, 0),
                  line_width: int = 3,
                  output_path: str = None):
    """Draws segments on image."""

    image = im.copy()
    for segment in segments:
        x, y, w, h = segment
        cv2.rectangle(image, (x, y), (x + w, y + h), color, line_width)

    plot_image(image)

    if output_path:
        cv2.imwrite(output_path, image)


image = cv2.imread('data/text_image.jpg')
plot_image(image, title='Text image')

# converting to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Otsu binarization
_, binary = cv2.threshold(np.invert(gray), 0, 255, 0 | 8)

plot_image(binary, title='Binary image')

# Morphological close
kernel_h = np.ones((2, 4), np.uint8)
temp_img = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_h, iterations=2)

# Morphological dilate
kernel_v = np.ones((1, 5), np.uint8)
line_img = cv2.dilate(temp_img, kernel_v, iterations=5)

# finding contours
_, contours, _ = cv2.findContours(line_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# changing contours  to segments
segments = contours_to_segments(contours, x_margin=1, y_margin=5)

# drawing segments
draw_segments(image, segments, output_path='data/segmented_text_image.png')