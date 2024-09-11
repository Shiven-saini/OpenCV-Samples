#include <opencv2/opencv.hpp>
using namespace cv;

int main() {
    Mat source = imread("/home/shiven/coding/ubuntu_logo.jpeg");

    imshow("Ubuntu Logo", source);
    waitKey(0);
    return 0;
}
