# USAGE
# python flipping.py --image florida_trip.png

# import the necessary packages
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

rotated = imutils.rotate(flipped, 45)
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

# flip the image vertically
flipped1 = cv2.flip(rotated, 0)
cv2.imshow("Flipped Vertically", flipped1)
(b, g, r) = flipped1[189, 441]
print("Pixel at (441, 189) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
cv2.waitKey(0)

