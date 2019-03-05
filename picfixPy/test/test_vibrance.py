# This script tests the vibrance() function.

# vibrance(input_img, intensity, output_img) adjusts the vibrance of an image
# Input: input_img: string, path for the input image file
#        intensity: int, intensity of vibrance enhancement, between -10 and 10, defaults to 5.
#        display -- bool. If True, output will be displayed. Defaults to False.
#        output_img: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
from skimage.io import imread, imsave, imshow
from picfixPy.vibrance import vibrance

# generate input image

test_img1 = np.array([[[ 4, 77,245], [44,44,32] ,[60,70,80]],
                      [[6,66,43], [33,55,63], [22,56,70]],
                      [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')


imsave("picfixPy/test/test_img/vibrance/test_img1.png", test_img1)

# generate expected output image with intensity = 10

expected_img1 = np.array([[[  0,  74, 245], [ 43,  44,  19], [ 40,  60,  80]],
                          [[  0,  66,  40], [  2,  47,  63], [  0,  49,  70]],
                          [[  0,  54,  66], [ 52,  77,   8], [ 21,  45,   0]]], dtype = "uint8")
                        

# generate expected output image with intensity = -10, should be greyscale

expected_img2 = np.array([[[245, 245, 245], [ 44,  44,  44], [ 80,  80,  80]],
                          [[ 66,  66,  66], [ 63,  63,  63], [ 70,  70,  70]],
                          [[ 66,  66,  66], [ 77,  77,  77], [ 45,  45,  45]]], dtype= "uint8")

# test for implementation correctness

def test_high_vibrance():
    vibrance("picfixPy/test/test_img/vibrance/test_img1.png",
             10,
             False,
             "picfixPy/test/test_img/vibrance/expected_img1.png")
    output_img = imread("picfixPy/test/test_img/vibrance/expected_img1.png")[:, :, :3]
    assert np.array_equal(output_img, expected_img1), "The image returned should be identical with 10 intensity."

def test_low_vibrance(): #should be grey
    vibrance("picfixPy/test/test_img/vibrance/test_img1.png",
             -10,
             False,
             "picfixPy/test/test_img/vibrance/expected_img1.png")
    output_img = imread("picfixPy/test/test_img/vibrance/expected_img1.png")[:, :, :3]
    assert np.array_equal(output_img, expected_img2), "The image returned should be in greyscale and identical with -10 intensity."

# test for exception handling

def test_input_string():
    with pytest.raises(AttributeError):
        vibrance(888, 5, False, "picfixPy/test/test_img/vibrance/vibrance.png")

def test_valid_intensity():
    with pytest.raises(ValueError):
        vibrance("picfixPy/test/test_img/vibrance/test_img1.png",
                 -10.5,
                 False,
                "picfixPy/test/test_img/vibrance/vibrance.png")

def test_input_exist():
    with pytest.raises(FileNotFoundError):
        vibrance("picfixPy/test/test_img/ffxiv/namazu.png",
                 5,
                 False,
                "picfixPy/test/test_img/vibrance/vibrance.png")

def test_input_nonimage():
    with pytest.raises(OSError):
        vibrance("picfixPy/test/test_img/vibrance/test_img1.java",
                 5,
                 False,
                "picfixPy/test/test_img/vibrance/vibrance.png")

def test_display_image():
    try:
        vibrance("picfixPy/test/test_img/vibrance/test_img1.png",
                 5,
                 True)
    except Exception: # pragma: no cover
        raise pytest.fail("Cannot display image, something went wrong.")

def test_output_nonimage():
    with pytest.raises(ValueError):
        vibrance("picfixPy/test/test_img/vibrance/test_img1.png",
                 5,
                 False,
                 "picfixPy/test/test_img/vibrance/test_img2.java")

def test_output_path_valid():
    with pytest.raises(FileNotFoundError):
        vibrance("picfixPy/test/test_img/vibrance/test_img1.png",
                 5,
                 False,
                "beasttribe/namazu/dailies.png")
