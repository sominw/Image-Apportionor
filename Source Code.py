# -*- coding: utf-8 -*-
"""
Source Code for Image Apportionor

@author: sominwadhwa

Note: Originally created in Anaconda/spyder (Python 2.7). Do the required modifications
if running on a different enviroment.

Pre-requisites: Pillow/PIL or an equivalent image processing library.
				
				graphics.py (Included with the project files)
				
				Anaconda: An open data science platform from Continuum Analytics 

"""

#!/usr/bin/python
from PIL import Image, ImageStat
import numpy
import sys

"""
	The algorithm determines if the centroids have converged to their global minimum or not.
	If the initialized version is the same as the new version of centroids then there is no need to proceed 
	any further.

	Also, please make a note that the centroids here are being randomly initialized and therefore it make 
	take different number of iterations to converge even for the same image.
"""

def converged(centroids, prev_centroids):
	if len(prev_centroids) == 0:
		return False


	if len(centroids) <= 5:
		a = 1
	elif len(centroids) <= 10:
		a = 2
	else:
		a = 4

	for i in range(0, len(centroids)):
		cent = centroids[i]
		prev_cent = prev_centroids[i]

		if ((int(prev_cent[0]) - a) <= cent[0] <= (int(prev_cent[0]) + a)) and ((int(prev_cent[1]) - a) <= cent[1] <= (int(prev_cent[1]) + a)) and ((int(prev_cent[2]) - a) <= cent[2] <= (int(prev_cent[2]) + a)):
			continue
		else:
			return False

	return True #Convergence Reached




#The following two functions implements the step one of the K-Means Algorithm
def getMin(pix, centroids):
	minDist = 99999
	minIndex = 0

	for i in range(0, len(centroids)):
		d = numpy.sqrt(int((centroids[i][0] - pix[0]))**2 + int((centroids[i][1] - pix[1]))**2 + int((centroids[i][2] - pix[2]))**2)
		if d < minDist:
			minDist = d
			minIndex = i

	return minIndex #Returns the index value of the closest centroid



def assignpixs(centroids):
	clusters = {}

	for x in range(0, img_width):
		for y in range(0, img_height):
			p = px[x, y]
			minIndex = getMin(px[x, y], centroids)

			try:
				clusters[minIndex].append(p)
			except KeyError:
				clusters[minIndex] = [p]

	return clusters #Returns the array of clusters


#The following function implements the step two of the K-Means Algorithm
def adjustCentroids(centroids, clusters):
	new_centroids = []
	keys = sorted(clusters.keys())
	#print(keys)

	for k in keys:
		n = numpy.mean(clusters[k], axis=0)
		new = (int(n[0]), int(n[1]), int(n[2]))
		print(str(k) + ": " + str(new))
		new_centroids.append(new)

	return new_centroids #Returns the new position of centroids


#The following function does all the required initializations for the K-Means algorithm
'''

Dear maintainer: 
Once you are done trying to 'optimize' this routine,
and have realized what a terrible mistake that was,
please increment the following counter as a warning
to the next guy:
total_hours_wasted_here = 42

'''
def startKmeans(someK):
	centroids = []
	prev_centroids = []
	j = 1
	rgb_range = ImageStat.Stat(im).extrema #Min/max values for each band in the image.

	#Initializes someK number of centroids for the clustering algorithm to begin
	for k in range(0, someK):

		cent = px[numpy.random.randint(0, img_width), numpy.random.randint(0, img_height)]
		centroids.append(cent)
	

	print("\nRandom Initialization Complete. The following iterations show the assignments as they are done: ")
	print("\n")

	while not converged(centroids, prev_centroids) and j <= 20:
		print("\nIteration #" + str(j))
		j += 1

		prev_centroids = centroids 								#Assigning old centroids as the new ones
		clusters = assignpixs(centroids) 						#Pixel Assignment
		centroids = adjustCentroids(prev_centroids, clusters) 	#Re-Center the current version of centroids


	print("-------------------------")
	print("Convergence Reached! Final Centroid Positions: \n ")
	print(centroids)
	return centroids     #K-Means Algorithm ends here




#The following method will generate the resultant image using the graphics library
def drawWindow(result):
	img = Image.new('RGB', (img_width, img_height), "white")
	p = img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]):
			RGB_value = result[getMin(px[x, y], result)]
			p[x, y] = RGB_value

	img.show()



#This is where the execution starts:
#Please refer to the image ids as specified in the designated 'img' folder 
#before beginning here.

num_input = str(input("Enter Image ID: "))
k_input = int(input("Enter the number of clusters: "))
img = "img/test" + num_input.zfill(2) + ".jpg" 
#Loads the image into a matrix form
im = Image.open(img)
img_width, img_height = im.size
px = im.load()

res = startKmeans(k_input)
drawWindow(res)
