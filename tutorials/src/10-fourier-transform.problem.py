# Tutorial #10
# ------------
#
# Doing the Fourier Transform for images and back. This code is based on the stackoverflow answer from Fred Weinhaus:
# https://stackoverflow.com/a/59995542

import cv2
import numpy as np

# Global helper variables
window_width = 640
window_height = 480

# TODO Implement the function get_frequencies(image):

def get_frequencies(image):
    # Convert image to floats and do dft saving as complex output

    image_32F = np.float32(image)

    freqencies = cv2.dft(image_32F, flags= cv2.DFT_COMPLEX_OUTPUT)
   
    # Apply shift of origin from upper left corner to center of image

    frequencies_shift = np.fft.fftshift(freqencies)

    # Extract magnitude and phase images

    magnitude, phase = cv2.cartToPolar(frequencies_shift[:,:,0], frequencies_shift[:,:,1])

    # Get spectrum for viewing only

    spectrum =np.log(magnitude) / 30

    normalised_spectrum = cv2.normalize(spectrum, spectrum, 0.0, 1.0, cv2.NORM_MINMAX) 

    # Return the resulting image (as well as the magnitude and phase for the inverse)
    return normalised_spectrum, magnitude, phase

# TODO Implement the function create_from_spectrum():

def create_from_spectrum(magnitude, phase):
    # Convert magnitude and phase into cartesian real and imaginary components

    # magnitude =cv2.pow(magnitude, 1.1)

    real, imaginary = cv2.polarToCart(magnitude, phase)

    # Combine cartesian components into one complex image

    back = cv2.merge([real, imaginary])

    # Shift origin from center to upper left corner

    back_shifted = np.fft.ifftshift(back)

    # Do idft saving as complex output

    image_back = cv2.idft(back_shifted)

    # Combine complex components into original image again

    image_back = cv2.magnitude(image_back[:,:,0], image_back[:,:,1])

    #   Re-normalize to 8-bits
    min, max = np.amin(image_back, (0,1)), np.amax(image_back, (0,1))
    print(min, max)
    image_back = cv2.normalize(image_back, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    return image_back



# We use a main function this time: see https://realpython.com/python-main-function/ why it makes sense
def main():
    # Load an image, compute frequency domain image from it and display both or vice versa
    image_name = "./tutorials/data/images/chewing_gum_balls01.jpg"

    # Load the image.
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (window_width, window_height))

    # Show the original image
    # Note that window parameters have no effect on MacOS
    title_original = "Original image"
    cv2.namedWindow(title_original, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_original, window_width, window_height)
    cv2.imshow(title_original, image)

    result, manitude, phase = get_frequencies(image)
    result = np.zeros((window_height, window_width), np.uint8)

    # Show the resulting image
    # Note that window parameters have no effect on MacOS
    title_result = "Frequencies image"
    cv2.namedWindow(title_result, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_result, window_width, window_height)
    cv2.imshow(title_result, result)

    back = create_from_spectrum(manitude, phase)
    back = np.zeros((window_height, window_width), np.uint8)

    # And compute image back from frequencies
    # Note that window parameters have no effect on MacOS
    title_back = "Reconstructed image"
    cv2.namedWindow(title_back, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_back, window_width, window_height)
    cv2.imshow(title_back, back)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()


# Starting the main function
if __name__ == "__main__":
    main()
