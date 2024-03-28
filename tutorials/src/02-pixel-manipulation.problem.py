# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# TODO Loading images in grey and color

image_color = cv2.imread("tutorials\data\images\smarties01.jpg", cv2.IMREAD_COLOR)

image_greyscale = cv2.imread("tutorials\data\images\smarties01.jpg", cv2.IMREAD_GRAYSCALE)

# TODO Do some print out about the loaded data using type, dtype and shape

print("image_greyscale:")
print(type(image_greyscale))
print(image_greyscale.shape)
print(image_greyscale.dtype)
print("image_color:")
print(type(image_color))
print(image_color.shape)
print(image_color.dtype)

# TODO Continue with the grayscale image

# TODO Extract the size or resolution of the image

height, width = image_greyscale.shape
print("width = ", width)
print("height = ", height)
# TODO Resize image

image_grey_resized = cv2.resize(image_greyscale, (8, 4))

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# TODO Print first row

print(image_grey_resized[0, :])

# TODO Print first column

print(image_grey_resized[:, 0])

# TODO Continue with the color image

# TODO Set an area of the image to black

image_color_resized_black_area = cv2.resize(image_color, (400, 400))

image_color_resized_black_area[150:165, :] = (0, 0, 0)

cv2.imshow("My file", image_color_resized_black_area)
cv2.waitKey(0)

# TODO Show the image and wait until key pressed

# TODO Find all used colors in the image

# TODO Copy one part of an image into another one

# TODO Save image to a file

# TODO Show the image again

# TODO Show the original image (copy demo)
