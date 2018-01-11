import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())
 
# load the image
image = cv2.imread(args["image"])

# define the list of boundaries
'''boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]'''
boundaries = [([17, 15, 100], [50, 56, 200])]

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    print(mask.shape)   #mides matriu
    print(len(mask))
    print(len(mask[0]))
    
    min_left = 9999
    max_right = 0
    for i in range(len(mask)):
        for j in range(len(mask[0])):
            if (mask[i,j] > 0):
                if j < min_left:
                    min_left = j
                if j > max_right:
                    max_right = j

    print("Min left "+str(min_left))
    print("Max right "+str(max_right))

    # show the images
    cv2.imwrite("output.jpg", output)
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
    
#python pixel.py --image color_detection_2.png
