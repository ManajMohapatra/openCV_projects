import cv2
import glob
import traceback
import os
import numpy as np

# folder location where image stored
imageFolder = "..\\resources\\images\\"

# All supported image file formats (list of extensions)
fileFormats = ['png','jpg']

def sobel(img):
	# edge detection using sobel  kernel
	sobelX	= cv2.Sobel(img,cv2.CV_8U,0,1)	#detects horizontal edges
	sobelY	= cv2.Sobel(img,cv2.CV_8U,1,0)	#detects vertical edges

	# combine both edges
	return cv2.bitwise_or(sobelX,sobelY)	#does a bitwise OR of each pixel

def sketch(frame):	
	# Gaussian blur to remove noise
	# kernel size is 3*3 and standard deviation 0
	frame = cv2.GaussianBlur(frame,(3,3),0)
	
	# Converting to negative image by subtracting from 255 (max value)
	invImg	= 255-frame
	
	#Detect edges from the input image and its negative
	edgImg	= sobel(frame)
	edgInvImg	= sobel(invImg)
	edgImg	= cv2.addWeighted(edgImg,1,edgInvImg,1,0)	# alpha 1, beta 1, gamma 0
	
	#Invert the image back
	invEdgImg = 255-edgImg
	return invEdgImg

if __name__ == '__main__':
	try:
		# list of all image file relative path
		imageFiles = []
		for extension in fileFormats:
			imageFiles += glob.glob(imageFolder + "*." + extension)

		# raise an exception if images not found
		if(not imageFiles):
			raise Exception("File not found. Please keep some image files inside resourses\images folder")

		for imgFile in imageFiles:
			# read in gray scale format
			img = cv2.imread(imgFile,0)
			imgSketch = sketch(img)

			# keep gray scale and sketch image side by side
			finalImage = np.concatenate((img, imgSketch), axis = 1)

			# get file name of image and show in a new window
			fileName = os.path.basename(imgFile)
			cv2.imshow(fileName, finalImage)

		# wait for any keypress before closing all windows
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	except Exception:
		traceback.print_exc()