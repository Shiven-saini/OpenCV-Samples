
---

**GitHub Repository =>** https://github.com/Shiven-saini/OpenCV-Samples

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
cmake_minimum_required(VERSION 3.0)
project(PROJECT_NAME)
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(main main.cpp)
target_link_libraries(main ${OpenCV_LIBS})
```

- Build and Compile
```bash
mkdir build
cd build
cmake ..
make
```

- Execute the generated binary
```bash
./main
```


## Better Way : To Compile and run an OpenCV project

I have written two bash scripts to automate the tasks of building and running the program. You can use these scripts by downloading scripts from my GitHub Repo.

**Initial Setup (One time) =>**
  
  - Download the scripts using `curl` :

  ```bash
  sudo curl -L -o /usr/bin/gen_template https://raw.githubusercontent.com/Shiven-saini/OpenCV-Samples/main/cpp_specific/scripts/gen_template.sh

sudo curl -L -o /usr/bin/run https://raw.githubusercontent.com/Shiven-saini/OpenCV-Samples/main/cpp_specific/scripts/run.sh
```

> [!warning] Location of the Scripts on GitHub Repo may change in future. So check out the repository before going ahead.

- Add execute permission using `chmod` : 

```bash
sudo chmod +x /usr/bin/gen_template /usr/bin/run
```

**Usage =>**

- To Generate a OpenCV C++ Template :
```bash
gen_template PROJECT_NAME
```

- To build and execute the binary :
```bash
run main.cpp
```

> [!tip] gen_template script generates CMakeLists file for OpenCV and also build a .gitignore file for you.

## Example : Display Image in OpenCV C++

- Create project using `gen_template` script :
```bash
gen_template display_image
```

- Add Source Code in the `main.cpp` file :
```cpp
#include <opencv2/opencv.hpp>
using namespace cv;

int main() {
    Mat source = imread("/home/shiven/coding/ubuntu_logo.jpeg");
    imshow("Ubuntu Logo", source);
    waitKey(0);
    
    return 0;
}
```

- Build and execute the file using `run` script :
```bash
run main.cpp
```

---
