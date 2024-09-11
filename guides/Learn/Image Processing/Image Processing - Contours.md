
---

**Code Repository =>** https://github.com/Shiven-saini/OpenCV-Samples

![[Pasted image 20240909204024.png|center|500]]

**Contours** are simply a curve joining all the continuous points, having same color or intensity.
Contours are a useful tool in shape analysis and object detection and recognition.

> [!note]  For better accuracy use binary images.(apply threshold or canny edge detection)

The `cv2.findContours()` function requires the following parameters:

1. **Image**: The source image should be an 8-bit single-channel image, usually a binary image. It's common to apply binary thresholding or Canny edge detection before using this function to ensure accurate contour detection

2.  **Mode**: This parameter specifies the contour retrieval mode. It determines the hierarchy of contours. Some common modes include:
    - `cv2.RETR_EXTERNAL`: Retrieves only the extreme outer contours.
    - `cv2.RETR_LIST`: Retrieves all contours without establishing any hierarchical relationships.
    - `cv2.RETR_CCOMP`: Retrieves all contours and organizes them into a two-level hierarchy.
    - `cv2.RETR_TREE`: Retrieves all contours and reconstructs a full hierarchy of nested contours
    
3. **Method**: This parameter specifies the contour approximation method. It determines how the contour points are stored:
    
    - `cv2.CHAIN_APPROX_NONE`: Stores all the boundary points. This can be memory-intensive.
    - `cv2.CHAIN_APPROX_SIMPLE`: Compresses horizontal, vertical, and diagonal segments and leaves only their end points, which saves memory

Contour is a python list of all the contours found in the image. Each individual contour in the list is a numpy array of coordinates.

![[Pasted image 20240909182730.png]]

## Draw the Contours

**Method =>** `cv.drawContours()`
- First parameter : source
- Second parameter : contours (array)
- Third parameter : index (contour to draw) -1 for each
- Fourth parameter : Color (BGR Tuple)
- Fifth parameter : Thickness (pixels)

> [!note] **To create an empty black canvas :-**
`canvas = np.zeros_like(source)`


## Features of Contours

1. Calculating the centroid of an object
```python
M = cv.moments(contours[0])
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
cv.circle(source_binary, (cx, cy), 1, (255, 0, 0), 1)
```

I calculated Moments of the image using contours and then applied basic physics to calculate it's centroid point.

2. Contour Area

```python
area = cv.contourArea(cnt)
```

3. Contour Perimeter

```python
perimeter = cv.arcLength(cnt, True)
```


There are a lot of other features available to use with OpenCV like finding extreme points, convexity. But our Use-case in robotics generally not require these features at all. Knowing that these features exist is atleast recommended.

#### References :-
- Python OpenCV Docs : https://docs.opencv.org/4.x/d3/d05/tutorial_py_table_of_contents_contours.html
- Contours Wikipedia : https://en.wikipedia.org/wiki/Contour_line
- Contours Medium Article : https://medium.com/featurepreneur/draw-contours-on-an-image-using-opencv-186b67f87c92
- 