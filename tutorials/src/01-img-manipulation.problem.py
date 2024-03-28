# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

# TODO First step is to import the opencv module which is called 'cv2'
import cv2

# TODO Check the opencv version
print(cv2.__version__)

# TODO Load an image with image reading modes using 'imread'
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.

image_source = "tutorials\data\images\window01.JPG"

image_unchanged = cv2.imread(image_source, cv2.IMREAD_UNCHANGED)

image_greyscale = cv2.imread(image_source, cv2.IMREAD_GRAYSCALE)

image_color = cv2.imread(image_source, cv2.IMREAD_COLOR)

# TODO Resize image with 'resize'

image_resized = cv2.resize(image_color, (500,200))

# TODO Rotate image (but keep it rectangular) with 'rotate'

image_rotated = cv2.rotate(image_color, cv2.ROTATE_90_CLOCKWISE)

# TODO Save image with 'imwrite'

cv2.imwrite("file.png", image_rotated)

# TODO Show the image with 'imshow'
cv2.imshow("My image", image_color)
cv2.waitKey(0)
    