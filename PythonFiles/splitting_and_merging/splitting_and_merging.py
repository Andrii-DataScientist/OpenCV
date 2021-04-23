# USAGE
# python splitting_and_merging.py --image florida_trip_small.png

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load the image and grab each channel: Red, Green, and Blue. It's
# important to note that OpenCV stores an image as NumPy array with
# its channels in reverse order! When we call cv2.split, we are
# actually getting the channels as Blue, Green, Red!
image = cv2.imread(args["image"])
(B, G, R) = cv2.split(image)

(b, g, r) = image[94, 180]
print("Pixel at (180, 94) - Red: {r}".format(r=r))


(b, g, r) = image[78, 13]
print("Pixel at (13, 78) - Blue: {b}".format(b=b))


(b, g, r) = image[5, 80]
print("Pixel at (80, 5) - Green: {g}".format(g=g))

