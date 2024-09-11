
---
OpenCV library is natively build in C++ and hence more performative on C++ platform than python. Due to better integration of ROS2 with C++ and also performance demands, Developing OpenCV for C++ might be desired.

## Installation

### **On Ubuntu :**

1. Install minimal prerequisites : `# apt install cmake g++ ninja meson wget unzip`
2. Download GitHub sources : 
```bash
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
```

3. Extract the resources :
```bash
unzip opencv.zip
unzip opencv_contrib.zip

mkdir -p build && cd build
```

4. Build from source code using cmake :
```bash
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x

cmake --build .
```

5. A