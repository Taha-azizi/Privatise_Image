#test
import cv2

# Importing tk to open and save our image file
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
#test
#print(filename)

#creating the image variable
img =cv2.imread(filename)

# pretty straight forward from here used https://medium.com/python-in-plain-english/convert-a-photo-to-pencil-sketch-using-python-in-12-lines-of-code-4346426256d4
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
inverted_gray_image = 255 - gray_image
blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0) 
inverted_blurred_img = 255 - blurred_img
pencil_sketch_IMG = cv2.divide(gray_image, inverted_blurred_img, scale = 256.0)
#Show the original image
cv2.imshow('Original Image', img)
#Show the new image pencil sketch
cv2.imshow('Pencil Sketch', pencil_sketch_IMG)
#Display the window infinitely until any keypress
cv2.waitKey(0)