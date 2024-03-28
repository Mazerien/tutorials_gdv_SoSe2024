import cv2
import numpy as np

class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class ImageSection:
    def __init__(self, original_postition, new_position): 
        self.original_postiion = original_postition
        self.new_postition = new_position
     
image_source = "tutorials\data\images\smarties01.jpg"

image = cv2.imread(image_source, cv2.IMREAD_COLOR)
image = cv2.resize(image, (500,500))

print("width/height", image.shape)

cv2.imshow("My file", image)
cv2.waitKey(0)

x_position = 0
y_position = 0
section_size = 500 / 20
section_number = 500 / 25
height, width, color_channels = image.shape

for y in range(height):

    for x in range(width):

        saved_pixel = Pixel(x_position + x, y_position + y)
        image[x_position + x][y_position + y] = image[x_position + section_size + x][y_position + section_size + y]
        image[x_position + section_size + x][y_position + section_size + y] = image[saved_pixel.x][saved_pixel.y]

cv2.imshow("Changed file", image)
cv2.waitKey(0)