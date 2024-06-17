# Exercise #8
# -----------
#
# Demonstrating how to do template matching in OpenCV.

# Template matching, originally with objects from the image. Typical example
# is counting blood cells
import cv2

use_color = True
image_sauce = "tutorials\data\images\chewing_gum_balls01.jpg"
template_sauce = "tutorials\data\images\cgb_blue.jpg"
 
if use_color:
    """"""
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image

    image_colored = cv2.imread(image_sauce, cv2.IMREAD_COLOR)
    template = cv2.imread(template_sauce, cv2.IMREAD_COLOR)


    # TODO Read shape of the template and original image

    height_image, width_image, channels_image = image_colored.shape 
    height_template, width_template, channels_template = template.shape

else:
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image
    k 

    # TODO Read shape of the template and original image

    # TODO Define template matching methods,
    # See https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the
    # math behind each method

# TODO Loop over all methods in order to compare them
methodes = [cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF_NORMED]


    # TODO (In loop) work on a new image each time
for methode in methodes: 

    img = image_colored.copy()

    # TODO (In loop) do the template matching

    matched_image = cv2.matchTemplate(img, template, methode)

    # TODO (In loop) get the best match location

    match_bin = cv2.threshold(matched_image, 0.9, 1.0, cv2.THRESH_BINARY)

    # mask the original image with the binary 

    img_x_match_bin = cv2.bitwise_and(img, img, mask=match_bin)

    # TODO (In loop) draw rectangle at found location
    

    # TODO (In loop) show original image with found location

    # TODO (In loop) show image with the template matching result for all pixels
    cv2.imshow("Matching reslut", matched_image)
    cv2.imshow("Original Image", img)

    # (in loop) just press any key to show the next image
    cv2.waitKey(0)
    cv2.destroyAllWindows()
