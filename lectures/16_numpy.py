# ******************************************Numpy**************************************************

# This lecture introduces the most famous numerical python package Numpy.

# Numpy is the most basic and a powerful package for working with data in python.

# At the core, numpy provides the excellent ndarray objects, short for n-dimensional arrays.
# A numpy array is a grid of values, all of the same type, and is indexed by a tuple of
# non negative integers. The number of dimensions is the rank of the array;
# the shape of an array is a tuple of integers giving the size of the array along each dimension.


# There are several important differences between NumPy arrays and the standard Python sequences:

# - NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically).
# Changing the size of an ndarray will create a new array and delete the original.

# - The elements in a NumPy array are all required to be of the same data type, and thus will be
# the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects,
# thereby allowing for arrays of different sized elements.

# - NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of
# data. Typically, such operations are executed more efficiently and with less code than is
# possible using Python’s built-in sequences.

# - A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays;
# though these typically support Python-sequence input, they convert such input to NumPy arrays
# prior to processing, and they often output NumPy arrays. In other words, in order to efficiently
# use much (perhaps even most) of today’s scientific/mathematical Python-based software, just
# knowing how to use Python’s built-in sequence types is insufficient - one also needs to know how
# to use NumPy arrays.

# Behind the scenes most of code is executed by pre-compiled C code.

import cv2
import numpy as np

# when we read an image with opencv we get a numpy array object
image = cv2.imread('data/numpy.jpeg')
print(type(image))
print(image.shape)

# You can access a pixel value by its row and column coordinates. For BGR image, it returns an
# array of Blue, Green, Red values. For grayscale image, just corresponding intensity is returned.

# The key difference between an array and a list is, arrays are designed to handle
# vectorized operations while a python list is not. That means, if you apply a function
# it is performed on every item in the array, rather than on the whole array object.

list_1 = [0, 1, 2, 3]
array_1_d = np.array(list_1)

# Let’s suppose you want to add the number 2 to every item in the list.
# The intuitive way to do it is something like this:

# list_1 + 2  # produces an error

# That was not possible with a list. But you can do that on a ndarray.
# Add 2 to each element of array. This kind of performance is call vectorized performance, which is
# the main advantage of numpy.

print(array_1_d + 2)

# Another characteristic is that, once a numpy array is created, you cannot increase its size.
# To do so, you will have to create a new array. But such a behavior of extending the size
# is natural in a list.

# You may also specify the datatype by setting the dtype argument.
# Some of the most commonly used numpy dtypes are: 'float', 'int', 'bool', 'str' and 'object'.
# To control the memory allocations you may choose to use one of
# ‘float32’, ‘float64’, ‘int8’, ‘int16’ or ‘int32’.

list_2 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
array_2_d_float = np.array(list_2, dtype='float')
print(array_2_d_float)

# You can also convert it to a different datatype using the astype method.

# Convert to int then to str datatype.
print(array_2_d_float.astype('int').astype('str'))

# A numpy array must have all items to be of the same data type, unlike lists.
# This is another significant difference. However, if you are uncertain about what datatype
# your array will hold or if you want to hold characters and numbers in the same array,
# you can set the dtype as 'object'.

array_1_d_object = np.array([1, 'a'], dtype='object')

# You can always convert an array back to a python list using tolist().
print(array_1_d_object.tolist())

# How to inspect the size and shape of a numpy array?
# Create a 2d array with 3 rows and 4 columns.

list_3 = [[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]]
arr = np.array(list_3, dtype='float')
print('Shape: ', arr.shape)
print('Datatype: ', arr.dtype)
print('Size: ', arr.size)
print('Num dimensions ', arr.ndim)

# How to reverse the rows and the whole array?

# Reverse only the row positions
print(arr[::-1])

# Reverse the row and column positions
print(arr[::-1, ::-1])

# How to compute mean, min, max on the ndarray?
print('Mean value is: ', arr.mean())
print('Max value is: ', arr.max())
print('Min value is: ', arr.min())

# if you want to compute the minimum values row wise or column wise, use the axis.

print('Columns minimum: ', np.min(arr, axis=0))
print('Row minimum', np.min(arr, axis=1))

# Reshaping and Flattening Multidimensional arrays.

# Reshaping is changing the arrangement of items so that shape of the array changes while
# maintaining the same number of dimensions. Flattening, however, will convert a multi-dimensional
# array to a flat 1d array. And not any other shape.

print(arr.reshape(4, 3))

# There are 2 popular ways to implement flattening. That is using the flatten() method and the
# other using the ravel() method. The difference between ravel and flatten is, the new array
# created using ravel is actually a reference to the parent array. So, any changes to the new array
# will affect the parent as well. But is memory efficient since it does not create a copy.

print(arr.flatten())

# Changing the flattened array does not change parent.
b1 = arr.flatten()
b1[0] = 100
print(arr)

# Changing the raveled array changes the parent also.
b2 = arr.ravel()
b2[0] = 101
print(arr)

# How to create sequences, repetitions and random numbers using numpy?

# The np.arange function comes handy to create customised number sequences as ndarray.
# This function is very similar to range function.

print(np.arange(5))  # lower limit is 0 by default
print(np.arange(0, 10))  # 0 to 9
print(np.arange(0, 10, 2))  # 0 to 9 step of 2
print(np.arange(10, 0, -1))  # 10 to 1, decreasing order

# Create an array of exactly 10 numbers between 1 and 50:
np.linspace(start=1, stop=50, num=50, dtype='int')

# The np.zeros and np.ones functions lets you create arrays of desired shape where all the items
# are either 0’s or 1’s.

print(np.zeros((2, 2)))
print(np.ones((2, 2)))

# How to create repeating sequences?
sequence = [1, 2, 3]

# Repeat whole sequence 2 times.
print(f'Tile: {np.tile(sequence, 2)}')

# Repeat each element of sequence 2 times.
print(f'Repeat: {np.repeat(sequence, 2)}')

# How to generate random numbers?

# Random numbers between [0,1) of shape 2,2
print(np.random.rand(2, 2))

# One random number between [0, 1) (Uniform distribution)
print(np.random.random())

# Random numbers between [0,1) of shape 2,2
print(np.random.random(size=(2, 2)))

# Normal distribution with mean=0 and variance=1 of shape 2,2
print(np.random.randn(2, 2))

# Random integers between [0, 10) of shape 2,2
print(np.random.randint(0, 10, size=(2, 2)))

# Pick 10 items from a given list, with equal probability
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))

#  Pick 10 items from a given list with a predefined probability 'p'
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10, p=[0.3, 0.1, 0.1, 0.4, 0.1]))

# How to get the unique items and the counts?
arr_rand = np.random.randint(0, 10, size=10)
print(arr_rand)

uniques, counts = np.unique(arr_rand, return_counts=True)
print('Unique items :', uniques)
print('Counts: ', counts)

# Copies and Views

# Different array objects can share the same data.
# The view method creates a new array object that looks at the same data.

a = np.arange(12)
print(a)
b = a  # no new object is created
print(f'b is a: {b is a}')  # a and b are two names for the same ndarray object
b.shape = 3, 4  # changes the shape of a also
print(a.shape)

# View
a = np.arange(12)
b = a.view()
print(f'b is a: {b is a}')
print(f'b base is a: {b.base is a}')
b.shape = 3, 4
print(a.shape)  # does not change the shape of a
b[0, 0] = -99999
print(a)  # changes a

# Slicing an array returns a view of it:
a = np.arange(12)
b = a[:]
print(f'b is a: {b is a}')
print(f'b base is a: {b.base is a}')

# For making copy we should use array.copy(), which makes a complete copy of the array.
a = np.arange(12)
print(a)
b = a.copy()  # new object is created
print(f'b is a: {b is a}')
b.shape = 3, 4  # does not change the shape of a
print(a.shape)

# ********************************Indexing, Slicing and Iterating**********************************

# One-dimensional arrays can be indexed, sliced and iterated over, much like lists and other Python
# sequences:

# [Start index (included): Stop index (excluded): Step]


arr = np.arange(10) ** 3
print(arr[2])
print(arr[2:5])
arr[:6:2] = 1000  # from start to position 6, exclusive, set every 2nd element to -1000
print(arr[::-1])

# Multidimensional arrays can have one index per axis. These indices are given in a tuple separated
# by commas:

m_array = np.random.randint(1, 100, size=(5, 4, 3))
print(m_array)
print(m_array.shape)

# This is a 3D array, which has 3 layers and each layer is matrix with 5 rows and 4 columns.

print(m_array[2, 3, 0])  # selecting first layer element which is located at 2 row and 3 column
print(m_array[:5, 1])  # each row in the second column of array for all layers
print(m_array[1:3, :])  # each column in the second and third row of array

# When fewer indices are provided than the number of axes, the missing indices are considered
# complete slices:

print(m_array[-1])  # the last row for all layers

# Iterating over multidimensional arrays is done with respect to the first axis:
print('\n iterating over rows of first layer: \n')
for row in m_array[:, :, 0]:
    print('\n', row)

# However, if one wants to perform an operation on each element in the array,
# one can use the flat attribute which is an iterator over all the elements of the array:
print('\n iterating over first layer rows elements: \n')
for element in m_array[:, :, 0].flat:
    print(element)

# We can separate a 3-column 2D dataset into input and output data as follows:

data = np.array([[11, 22, 33],
                 [44, 55, 66],
                 [77, 88, 99]])

x, y = data[:, :-1], data[:, -1]
print(x, y)

# *********************************Fancy indexing and Boolean Logic********************************

# NumPy offers more indexing facilities than regular Python sequences.
# In addition to indexing by integers and slices as we saw before, arrays can be indexed by
# arrays of integers and arrays of booleans.

arr = np.arange(12) ** 2  # the first 12 square numbers
indexes = np.array([1, 1, 3, 8, 5])  # an array of indices
print(arr[indexes])

two_dimensional_indexes = np.array([[3, 4], [9, 7]])
print(arr[two_dimensional_indexes])  # the same shape as two_dimensional_indexes

# Fancy indexing also works in multiple dimensions. Consider the following array:
arr = np.arange(12).reshape((3, 4))

# Like with standard indexing, the first index refers to the row, and the second to the column:
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
print(arr[row, col])

# Notice that the first value in the result is arr[0, 2], the second is arr[1, 1]
# and the third is arr[2, 3].

# We can combine fancy and simple indices:
print(arr[2, [2, 0, 1]])

# We can also combine fancy indexing with slicing:
print(arr[1:, [2, 0, 1]])

# Just as fancy indexing can be used to access parts of an array, it can also be used to
# modify parts of an array.
arr = np.arange(10)
indexes = np.array([2, 1, 8, 4])
arr[indexes] = 99
print(arr)

# When we index arrays with arrays of (integer) indices we are providing
# the list of indices to pick. With boolean indices the approach is different; we explicitly
# choose which items in the array we want and which ones we don’t.
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr < 3)
print(arr > 3)
print(arr <= 3)
print(arr >= 3)
print(arr != 3)
print(arr == 3)

arr = np.random.randint(10, size=(3, 4))
print(arr < 6)

arr = np.arange(12).reshape(3, 4)
bool_indexing = arr > 4  # is a boolean with arr's shape
print(bool_indexing)
print(arr[bool_indexing])

# To count the number of True entries in a Boolean array, np.count_nonzero is useful:
print(np.count_nonzero(arr < 6))

# *******************************Simple Image Processing with Numpy********************************

import matplotlib.pyplot as plt

image = cv2.imread('data/rgb.png')
print(type(image))
print(image.shape)
print(image.dtype)


# Please note when you read a RGB image with OpenCV your image channels is switched: BGR

def bgr_to_rgb(im):
    """Converts BGR to RGB."""
    tmp = np.empty(im.shape, dtype=np.uint8)
    tmp[..., 0] = im[..., 2]
    tmp[..., 1] = im[..., 1]
    tmp[..., 2] = im[..., 0]
    return tmp


image = bgr_to_rgb(image)
print(image.shape)


def plot_image(im, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = im.shape[0]
    x = im.shape[1]
    w = (y / x) * h
    plt.figure(figsize=(w, h))
    plt.imshow(im, interpolation="none", **kwargs)

    plt.axis('off')
    plt.show()


# plotting an image
plot_image(image)

# plotting image channels
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

for i, ax, channel in zip(range(3), axs, ('red', 'green', 'blue')):
    ax.set_title(' '.join([channel, 'channel']))
    ax.imshow(image[:, :, i])
    ax.set_axis_off()
plt.show()


def to_grayscale(im, weights=(0.299, 0.587, 0.114)):
    """
    Transforms a RGB image to a greyscale image by taking the weighted mean of the RGB values.
    """
    gray_im = im[:, :, 0] * weights[0] + im[:, :, 1] * weights[1] + im[:, :, 2] * weights[2]
    return (gray_im).astype(np.uint8)


#
# def to_grayscale(im, weights=(0.299, 0.587, 0.114)):
#     """
#     Transforms a colour image to a greyscale image by taking the weighted mean of the RGB values.
#     """
#     return np.dot(im, weights)


gray_image = to_grayscale(image)
plot_image(gray_image)
cv2.imwrite('data/gray_image.png', gray_image)


def simple_threshold(im, threshold=128):
    return ((im > threshold) * 255).astype("uint8")


thresholds = [100, 120, 128, 138, 150]

fig, axs = plt.subplots(nrows=1, ncols=len(thresholds), figsize=(20, 5))

for t, ax in zip(thresholds, axs):
    ax.imshow(simple_threshold(gray_image, t), cmap='Greys')
    ax.set_title("Threshold: {}".format(t), fontsize=20)
    ax.set_axis_off()
plt.show()
