#!/bin/bash

# Checking if the file exists or not.
if [ ! -f "$1" ]; then
    echo "Error: No parameter provided."
    echo "Usage: $0 file"
    exit 1
fi

# Build and execute the code.
if [ ! -d build ]; then
    echo "Build directory does not exist!"
    echo "Creating build directory ...."
    mkdir build/
fi

cd build/
cmake ..
make

# Execute the file.
./main

