
---
## Fundamentals

**Digital image processing** is about processing image or other related visual data using a digital computer. It uses algorithms or machine learning to enhance or extract meaningful information from the image source.

![[attachments/Pasted image 20240830200337.png]]

### What is an Image ?

In terms of mathematics,

- An image is defined as two-dimensional function $F(x, y)$, where $x$ and $y$ are spatial coordinates.
- The amplitude of $F(x, y)$ at any pair of coordinates is called the *intensity* of the image at that point.
- A *digital image* consists of finite number of these elements, these smallest unit of elements are called **pixels**.


![[attachments/Pasted image 20240830183640.png]]


### What is Pixel ?

![[attachments/Pasted image 20240830200205.png]]

The word *pixel*, is a fusion word for picture element. It is the smallest unit of a digital image that can be manipulated. A single image consists of several thousands of millions of individual pixels. Pixel is the smallest hardware component on screen, that can display a color. The magnitude of **pixels per inch (PPI)** is directly related to better visual details.
Each pixel has a characteristic of color and brightness.

**Resolution:** It refers to the number of pixels in a digital image or the number of pixels hardware screen can represent.

**color depth:** Also known as *bit-depth*, indicates how many bits are used to represent the color of a pixel. Common standards are 8-bit, 16-bit and 24-bit. More bit depths, allows a pixel to represent a higher range of colors.

**Aspect Ratio:** It refers to the ratio of an image's width to it's height. 1920/1080 = 16/9. Common aspect ratios include 4:3, 16:9 and 1:1 (Square Ratio)

Some commonly used *resolution* standards are as per following :-
- 1280x720 : HD Screen
- 1920x1080: FHD Screen (Full HD)
- 2560x1440: QHD Screen (Quad HD)
- 3840x2160p: 4K UHD Screen (Ultra HD), 4K prefix comes from the fact that the approximate no. of horizontal pixels is around 4,000 (3840p)

### Types of images

1. **Binary Image ( or 1-bit image):** consists only two pixel values 0 or 1. 0 for black and 1 for white. Also known as **Monochrome.**
2. **Black and white image:** consists solely of black and white colors.
3. **Grayscale image ( or 8-bit image):** consists of different shades of grey ( 256 (2^8) to be precise). 0 stands for black, 127 for gray and 255 for white. Can be represented using only 1-byte, hence the name.
4. **RGB(565) Format ( or 16-bit image):** abbreviation for Red(5-bits), Green(6-bits) and Blue(5-bits). 6-bits for Green color is due to the fact that human eyes are more sensitive to different shades of Green, hence more precision and accuracy is desired.

----
## Color Space
Different systems are adopted from time to time to better display different color combinations, to make it as close to true visual representation of the object.

Some of the most frequently used ones are :-
### RGB Color Space

RGB color model blends different possible values of Red, Green and blue together to form an array of colors. In this model, Red, Green and Blue are considered as fundamental color sets and using their different permutations can realize multiple colors possible. Each color can accept a range of values from 0 to 255, but ultimately depends on the color-depth. i.e. how many bits are used to represent a color. More the bits, more colors can be represented.

We can commonly find rgb value represented in Hex Codes like `#FFFFFF` for white and `#000000` for black.  This color model has also been given a nickname of *true color image*, owing to it's abilities to represent natural color as accurate as possible.

An RGB is essentially an $M*N*3$ array, in which 3 different 2-D arrays are stacked on top of each other. (R -> G -> B)

![[rgb-color|1000]]
#### Advantages of rgb Color model

- It is a computationally practical system.
- It is considered as a base color space for many applications.
- It is an industry standard.
- No special transformations are required to display data on the system.

### HSV Color space

An HSV model is by far the most accurate model of how humans perceive colors. Biologically, human perceive colors differently than what rgb offers.

The H stands for *Hue*, S stands for *Saturation* and V stands for *Value.*

![[color_cone|1000]]


- **Hue:** The hue represents the color. The hue value ranges from 0 to 360 degrees. It is divided in 6 sections each representing different base color.

| Angle (in degrees) | Color   |
| ------------------ | ------- |
| 0 - 60             | Red     |
| 60 - 120           | Yellow  |
| 120 - 180          | Green   |
| 180 - 240          | Cyan    |
| 240 - 300          | Blue    |
| 300 - 360          | Magenta |
|                    |         |

- **Saturation:** The saturation value tells us how much of the respective color must be added. A 100% saturation means pure color is added, while 0% on the other hand means no color is added, resulting in grayscale.

- **Value:** It represents the brightness concerning the saturation of colors. A value of 0 represents total darkness, while the value of 100 indicates full brightness.

#### Advantages of HSV over rgb Color Model :-

- HSV is designed to mimic how human perceives and interpret colors naturally.
- HSV separates the color information (Hue and Saturation) from the brightness(Value), making it way more optimized for image processing.
- Frequently used in Histogram equalization.
