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

#checks if size of the image is compatible with the algorythm and resizes it if needed. 
def resize_on_bad_resolution(image_source):

    img = cv2.imread(image_source, cv2.IMREAD_COLOR)

    height, width, color_channels = img.shape
    
    height_reduction = height - height % 10

    print(height_reduction)
    
    width_reduction = width - width % 10

    img = cv2.resize(img, (width_reduction, height_reduction))

    return img



     
image_source = "tutorials\data\images\smarties01.jpg"

image = cv2.imread(image_source, cv2.IMREAD_COLOR)
#image = cv2.resize(image, (237,500))

image_resized = resize_on_bad_resolution(image_source)

print("width/height", image.shape)
print("width/height", image_resized.shape)

cv2.imshow("My file", image_resized)
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