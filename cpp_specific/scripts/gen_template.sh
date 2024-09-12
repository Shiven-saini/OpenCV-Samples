#!/bin/bash

# Check if a parameter is passed
if [ -z "$1" ]; then
    echo "Error: No parameter provided."
    echo "Usage: $0 project-name"
    exit 1
fi

# Check if project already exists.
if [ -d $1 ]; then
    echo "Error : Project $1 already exists!"
    exit 1
fi

# Create a new project directory
project_name=$1
mkdir $project_name
cd $project_name

# Generate CMakeLists.txt
echo 'Generating CMakeLists.txt file....'
cat <<EOL > CMakeLists.txt
cmake_minimum_required(VERSION 3.0)
project($project_name)
find_package(OpenCV REQUIRED)
include_directories(\${OpenCV_INCLUDE_DIRS})
add_executable(main main.cpp)
target_link_libraries(main \${OpenCV_LIBS})
EOL
echo 'Generating CMakeLists file Done!'

# Adding boilerplate code.
echo 'Generating boiler-plate code....'
cat <<EOL > main.cpp
#include <opencv2/opencv.hpp>
// #include <opencv2/imgproc/imgproc.hpp>
// #include <opencv2/highgui/highgui.hpp>
// #include <opencv2/video/video.hpp>
// #include <opencv2/objdetect/objdect.hpp>
// #include <opencv2/ml/ml.hpp>
// #include <opencv2/calib3d/calib3d.hpp>

using namespace cv;

int main() {

    return 0;
}
EOL
echo 'Generating Boiler-plate code Done!'

echo 'Adding git ignore file ....'
cat <<EOL > .gitignore
build/
EOL
echo 'All Operations Done!'