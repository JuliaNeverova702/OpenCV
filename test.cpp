#include<opencv2/opencv.hpp> 
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include<iostream>

using namespace cv;
using namespace std;

int main()
{
    Mat image1, image2, dst;
    image1 = imread("~/Documents/123.jpg");
    if (!image1.data) { printf("Error loading image1 \n"); return -1; }
    normalize(image1, dst, 255, 230, NORM_MINMAX,-1, noArray());

    namedWindow("Display window1");
    imshow("Display window1", dst);

    namedWindow("Display windo");
    imshow("Display windo", image1);

    waitKey(0);
    return 0;
}