# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# we need to keep in mind aspect ratio so the image does not look skewed
# or distorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a width of 150 pixels

dim = (2 * image.shape[1], int(image.shape[0] * 2))

# perform the actual resizing of the image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Resized (Width)", resized)

(b, g, r) = resized[367, 170]
print("Pixel at (170, 367) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
cv2.waitKey(0)
