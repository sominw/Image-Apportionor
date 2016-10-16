#Image Apportionor

A simple clustering based image processing. In its nascent stages, the algorithm was just a test implementation of the K-Means clustering but ultimately evolved into something much more. The project was done in Summer '16 as a part of the mandatory training project after my second year in undergraduate.

##Running the code
`conda/pip install pil` updates the python image library necessary for image I/O operations.

`graphics.py` - may or may not need this one depedning upon the platform.

Execute `source.py`

##Features
1. Implements K-Means in an elegant and understandable manner.
2. Inputs are entirely user driven.
3. Maximum Compression Ratio achieved: *6*

##Developing the Project
The source code can be directly imported to practically any python IDE (preferably conda) and developers can start right away.
The grounds of this one are primarily based on the K-means clustering and it started with a very naive implementation of the same in MATLAB in which centroid points and their movements were studied. 

The project is implemented entirely in Python with support of the Python Image Library [(PIL Documentaion)](https://pillow.readthedocs.io/en/3.4.x/ "Pillow Doc") and `graphics.py`. Upon executing the script the user is asked for an input image id (from the img directory) and the number of clusters to be defined. (More the cluster centroids, more the compression).

GUI implementation of the same can be done within python (could not do because of time constraints) and I very much encourage devs to to take it up.

##Running
Test Image 1:

![alt text](https://github.com/sominwadhwa/Image-Apportionor/blob/master/Tests/test03.jpg "Test 1") 

Result:  

![alt text](https://github.com/sominwadhwa/Image-Apportionor/blob/master/Tests/result03.jpg "Result 1")

**Number of Centroids**: 16

**Compression Ratio**: 6

##Implementation Notes

In practise, it was observed that if the image is very large, then K-means can take a long time to run. Therefore, it is recommended that images must be resized to managable sizes before running the code.

Maximum Compression Ratio Achieved: **6**

