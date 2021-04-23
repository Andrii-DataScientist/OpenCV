# USAGE
# python arithmetic.py --image grand_canyon.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

M = np.ones(image.shape, dtype = "uint8") * 75
added = cv2.add(image, M)
cv2.imshow("Added", added)
(b, g, r) = added[152, 61]
print("Pixel at (61, 152) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
cv2.waitKey(0)


