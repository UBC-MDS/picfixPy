# This script tests the sharpen() function.

# sharpen(input_path, output_path) sharpens image based on given intensity
# Input: input_path: string, path for the input image file
#        output_path: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
import skimage.io
from PicFixPy import sharpen

# testImg1: image is same after 0 intensity
testImg1 = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                      [[6,66,43], [33,55,63], [22,56,70]],
                      [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')


# testImg1_output: expected image, should be identical
testImg1_output = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                            [[6,66,43], [33,55,63], [22,56,70]],
                            [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')

def test_sharpen1():
    sharpen("PixFixPy/test/test_img/sharpen/testImg1.png", 0 ,
             "PixFixPy/test/test_img/sharpen/testImg1_output.png")
    output = skimage.io.imread("PixFixPy/test/test_img/sharpen/testImg1_output.png")[:, :, :3]
    assert np.array_equal(testImg1, output), "The image returned should have identical sharpness with 0 intensity."


# test 2: test if 5 intensity returns a sharper image than the original, it should.
# testImg2: image
testImg3 = np.array([[[ 10,  20,  40], [ 20,  40,  10], [ 40,  10,  20]],
                      [[ 40,  80, 160], [ 80, 160,  40], [160,  40,  80]],
                      [[ 60, 120, 240], [120, 240,  60], [240,  60, 120]]], dtype = "uint8")

# testImg2_output: expected sharper image than original
testImg2_output = np.array([[[ 50,  60,  90], [ 120,  140,  70], [ 80,  60,  90]],
                            [[ 90,  120, 200], [ 180, 200,  100], [200,  80,  100]],
                            [[ 110, 180, 200], [180, 200,  130], [200,  100, 190]]], dtype = "uint8")

def test_sharpen2():
    sharpen("PixFixPy/test/test_img/sharpen/testImg2.png", 5 ,
             "PixFixPy/test/test_img/sharpen/testImg3_output.png")
    output = skimage.io.imread("PixFixPy/test/test_img/sharpen/testImg2_output.png")[:, :, :3]
    assert np.array_equal(output, test_img2), "5 intensity should make this image sharper."


# test 3: test if 10 intensity returns a very sharp image, it should.
# testImg3: image
testImg3 = np.array([[[ 10,  20,  40], [ 20,  40,  10], [ 40,  10,  20]],
                      [[ 40,  80, 160], [ 80, 160,  40], [160,  40,  80]],
                      [[ 60, 120, 240], [120, 240,  60], [240,  60, 120]]], dtype = "uint8")

# testImg3_output: expected very sharp image
testImg3_output = np.array([[[ 100,  120,  140], [ 120,  140,  110], [ 140,  110,  120]],
                            [[ 140,  180, 250], [ 180, 250,  140], [250,  140,  180]],
                            [[ 160, 220, 240], [220, 240,  160], [240,  160, 220]]], dtype = "uint8")

def test_sharpen3():
    sharpen("PixFixPy/test/test_img/sharpen/testImg3.png", 10 ,
             "PixFixPy/test/test_img/sharpen/testImg3_output.png")
    output = skimage.io.imread("PixFixPy/test/test_img/sharpen/testImg2_output.png")[:, :, :3]
    assert np.array_equal(output, test_img3), "10 intensity should make this a very sharp image."
