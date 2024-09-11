
---
OpenCV library is natively build in C++ and hence more performative on C++ platform than python. Due to better integration of ROS2 with C++ and also performance demands, Developing OpenCV for C++ might be desired.

## Installation

### To install directly from the Official Repositories

- **On Ubuntu**
```bash
sudo apt install libopencv-dev
```

- **On Arch Linux**
```bash
sudo pacman -Sy opencv vtk hdf5 qt5-base cmake make ffmpeg gtkglext ffmpeg libjpeg-turbo libtiff
```

## To build from Source

1. Install pre-requisites : 

- **On Ubuntu**
```bash
sudo apt install build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
```

- **On Arch Linux**
```bash
sudo pacman -S base-devel 
```

> [!warning] Please note that packages in the official repositories might not be up-to-date.

2. Download OpenCV Source Code : 
```bash
git clone https://github.com/opencv/opencv.git
cd opencv
```

4. Build from source using `cmake` & `make` :
```bash
mkdir build && cd build
cmake ..
make -j$(nproc)       # To enable multi-core compilation
sudo make install     # Install the compiled libraries onto system.
```

5. Update Library Path :
```bash
sudo ldconfig
```

6. Verify Installation :
```bash
pkg-config --modversion opencv4
```


## Build system for OpenCV C++ Development

- Create a `CMakeLists.txt` file
```bash

```