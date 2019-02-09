# This script tests the vibrance() function.

# vibrance(input_path, output_path) converts a color image into greyscale
# Input: input_path: string, path for the input image file
#        output_path: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
import skimage.io
from PicFixPy import vibrance

# testImg1: color image is same after 0 intensity
testImg1 = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                      [[6,66,43], [33,55,63], [22,56,70]],
                      [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')


# testImg1_output: expected image, should be identical
testImg1_output = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                      [[6,66,43], [33,55,63], [22,56,70]],
                      [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')

def test_vibrance1():
    vibrance("PixFixPy/test/test_img/vibrance/testImg1.png", 0 ,
             "PixFixPy/test/test_img/vibrance/testImg1_output.png")
    output = skimage.io.imread("PixFixPy/test/test_img/vibrance/testImg1_output.png")[:, :, :3]
    assert np.array_equal(testImg1, output), "The image returned should be identical with 0 intensity."


# test 2: test if -10 intensity returns a greyscale image, it should.
# testImg2: color image
testImg2 = np.array([[[ 10,  20,  40], [ 20,  40,  10], [ 40,  10,  20]],
                      [[ 40,  80, 160], [ 80, 160,  40], [160,  40,  80]],
                      [[ 60, 120, 240], [120, 240,  60], [240,  60, 120]]], dtype = "uint8")

# testImg1_output: expected greyscale image
testImg2_output = np.array([[[ 19,  19,  19], [ 31,  31,  31], [ 20,  20,  20]],
                         [[ 77,  77,  77], [123, 123, 123], [ 80,  80,  80]],
                         [[115, 115, 115], [184, 184, 184], [121, 121, 121]]], dtype = "uint8")

def test_vibrance2():
    vibrance("PixFixPy/test/test_img/vibrance/testImg2.png", -10 ,
             "PixFixPy/test/test_img/vibrance/testImg2_output.png")
    output = skimage.io.imread("PixFixPy/test/test_img/vibrance/testImg2_output.png")[:, :, :3]
    assert np.array_equal(output, test_img2), "-10 intensity should make this a greyscale image."


# test 3: test if 10 intensity returns a very vibrant/saturated image, it should.
# testImg3: color image
testImg3 = np.array([[[ 10,  20,  40], [ 20,  40,  10], [ 40,  10,  20]],
                      [[ 40,  80, 160], [ 80, 160,  40], [160,  40,  80]],
                      [[ 60, 120, 240], [120, 240,  60], [240,  60, 120]]], dtype = "uint8")

# testImg3_output: expected saturated/vibrant image
testImg3_output = np.array([[[ 100,  120,  140], [ 120,  140,  110], [ 140,  110,  120]],
                      [[ 140,  180, 250], [ 180, 250,  140], [250,  140,  180]],
                      [[ 160, 220, 240], [220, 240,  160], [240,  160, 220]]], dtype = "uint8")

def test_vibrance3():
    vibrance("PixFixPy/test/test_img/vibrance/testImg3.png", 10 ,
             "PixFixPy/test/test_img/vibrance/testImg3_output.png")
    output = skimage.io.imread("PixFixPy/test/test_img/vibrance/testImg3_output.png")[:, :, :3]
    assert np.array_equal(output, test_img2), "10 intensity should make this a very saturated image."
