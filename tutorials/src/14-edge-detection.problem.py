# Tutorial #14
# ------------
#
# Compute the edges of an image with the Canny edge detection. Adjust the parameters using sliders.

import numpy as np
import cv2


def show_images_side_by_side(img_A, img_B):
    """Helper function to draw two images side by side"""
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))
    return

def update_and_show():

    result = 

# TODO: Define callback function
def update_canny_t1(value): 
    """Callback function for silders"""

    # Read slider positions
    threshol01 = value
    # Blur the image

    # Run Canny edge detection with thresholds set by sliders

    # Show the resulting images in one window using the show_images_side_by_side function

# TODO Load example image as grayscale

image = cv2.imread("tutorials\data\images\sift_table02.jpg", cv2.IMREAD_GRAYSCALE)

# Resize if needed

image = cv2.resize(image, dsize= None, fx= 0.5, fy= 0.5, interpolation= cv2.INTER_LINEAR)

# Clone if needed

# TODO Initial Canny edge detection result creation

result = cv2.Canny(image, threshold01, threshold02)

# TODO Create window with sliders
# Define a window name
window_name = "Canny edge detection demo"
# TODO Show the resulting images in one window

cv2.namedWindow(window_name)

show_images_side_by_side(image, result)

# TODO Create trackbars (sliders) for the window and define one callback function

cv2.createTrackbar("T1", window_name, 90, 255, update_canny_t1())
cv2.createTrackbar("T2", window_name, 100, 255, update_canny_t2())

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
