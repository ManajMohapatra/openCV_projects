# Pencil sketch of an image

### Objective
Display pencil sketch image of given image.

### Tools and libraries required
1. python 3.7.6
2. numpy 1.20.3
3. opencv-python 4.5.2.52

### Guidelines for use
1. All the images should be kept inside resources\images folder
2. To install required python libraries: `pip install -r requirements.txt`
2. To run the program: `python src\main.py`

### Description
1. Read input image in gray scale format
2. Remove any noise using Gaussian filter of kernel size 3x3
3. Create negative image (255 - pixel value)
4. Detect edge of both image and negative image using Sobel
	* Calculate horizontal and vertical edges and then return bitwise OR operation of both
5. Merge these two edge images
    * These two images reinforces some edges and complements some edges
    * Alternatively, these two images can be blended with different weights
6. Invert the blended image to get black sketch on white background
7. Show the image and wait for a keystroke to close the display

### Reference
1. [Github](https://github.com/TMuthuganesan/pencilSketch)
2. [Book](https://www.goodreads.com/book/show/24563887-practical-python-and-opencv)
