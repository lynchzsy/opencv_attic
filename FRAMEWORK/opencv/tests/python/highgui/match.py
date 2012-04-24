"""
This script will compare tho images and decides with a threshold
if these to images are "equal enough"
"""

# import the necessary things for OpenCV
import python
from python.cv import *
from python.highgui import *
import frames
import sys
import os

PREFIX=os.environ["top_srcdir"]+"/tests/python/testdata/images/"

# returns True/False if match/non-match
def match( image, index, thres ):

# load image from comparison set
	QCIFcompare=cvLoadImage(PREFIX+frames.QCIF[index])

	if QCIFcompare is None:
		print "Couldn't open image "+PREFIX+frames.QCIF[index]+" for comparison!"
		sys.exit(1)

# resize comparison image to input image dimensions
	size=cvSize(image.width,image.height)
	compare=cvCreateImage(size,IPL_DEPTH_8U,image.nChannels)
	cvResize(QCIFcompare,compare)

# compare images
	diff=cvNorm( image, compare, CV_RELATIVE_L2 )
#	print "mean("+repr(index)+" = "+repr(diff)
	
	del QCIFcompare
	del compare

	if diff<thres:
		return True
	else:
		return False

