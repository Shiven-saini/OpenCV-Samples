
---

**Code Repository =>** https://github.com/Shiven-saini/OpenCV-Samples

![[Pasted image 20240907114640.png]]


**Canny Edge detection** is a popular edge detection algorithm. It was Developed by John F. Canny.

Steps involved in the algorithm :-
- It is a multi-stage algorithm. It goes through various sub steps to detect the edges in final output.
- **Noise Reduction :** Edge detection is highly susceptible to noise in the image. So first of all, the noise in the image is removed using a `cv.GaussianFilter` .
- **Intensity Gradient of the image :** Image is then processed using a Sobel kernel in both horizontal (x-axis) and vertical (y-axis) to get first order derivative (Gx and Gy)
- **Edge Gradient :** It is calculated from first-order derivatives generated in the following formula. Since, now we have two images(sobelx and sobely), we can round it's value to one of four angles representing vertical, horizontal and two diagonal directions.
$$\text{Edge\_Gradient}(G) = \sqrt{G_x^2 + G_y^2}, \quad \text{Angle}(\theta) = \tan^{-1}\left(\frac{G_y}{G_x}\right)$$
- **Hysteresis Thresholding :** This stage decides which are real edges and which are not. We use two threshold values : *minVal* and *maxVal*. Any edges with gradient more than maxVal are sure to be edges and those below minVal are surely non-edges.

![[Pasted image 20240907120259.png]]

Those edges which lies in-between the threshold values are then checked again if they are connected to true edge or not.

## Canny Edge Detection in OpenCV

OpenCV combines all the different methods shown above in a single function `cv.Canny(`

**Method =>** `cv.Canny()`
- First parameter : Source image
- Second parameter :  Lower threshold value
- Third parameter : Upper threshold value

**Source Code :-**

```python
source = cv.imread("samples/lotus.jpg", cv.IMREAD_GRAYSCALE)
edges = cv.Canny(source, 50, 200)

cv.imshow("Original", source)
cv.imshow("Edges", edges)
```

![[Pasted image 20240907121349.png]]

#### References :-
- OpenCV Docs : https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
- Canny Edge Detection Wikipedia : https://en.wikipedia.org/wiki/Canny_edge_detector