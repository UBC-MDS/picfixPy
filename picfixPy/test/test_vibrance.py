# This script tests the vibrance() function.

# vibrance(input_img, intensity, output_img) adjusts the vibrance of an image
# Input: input_img: string, path for the input image file
#        intensity: int, intensity of vibrance enhancement, between 0 and 10, defaults to 5.
#        output_img: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
import skimage.io
from picfixPy import vibrance

# generate input image

test_img1 = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                      [[6,66,43], [33,55,63], [22,56,70]],
                      [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')

skimage.io.imsave("../picfixPy/test/test_img1.png", test_img1)

# generate expected output image with intensity = 10

expected_img1 = np.array([[[ 100,  120,  140], [ 120,  140,  110], [ 140,  110,  120]],
                         [[ 140,  180, 250], [ 180, 250,  140], [250,  140,  180]],
                         [[ 160, 220, 240], [220, 240,  160], [240,  160, 220]]], dtype = "uint8")


def test_zero_intensity():
    vibrance("../pixfixPy/test/test_img1.png",
             0,
             "../pixfixPy/test/vibrance.png")

    output_img = skimage.io.imread("../pixfixPy/test/vibrance.png")[:, :, :3]
    assert np.array_equal(output_img, test_img1), "Images should be indentical with 0 intensity."


def test_correct_vibrance():
    vibrance("pixfixPy/test/test_img/vibrance/test_img1.png",
             10,
             "pixfixPy/test/test_img/vibrance/expected_img1.png")
    output_img = skimage.io.imread("pixfixPy/test/test_img/vibrance/testImg1_output.png")[:, :, :3]
    assert np.array_equal(output_img, expected_img1), "The image returned should be identical with 10 intensity."

# test for exception handling

def test_input_string():
    with pytest.raises(AttributeError):
        vibrance(888, 5, "pixfixPy/test/test_img/vibrance/vibrance.png")

def test_valid_intensity():
    with pytest.raises(AttributeError):
        vibrance("pixfixPy/test/test_img/vibrance/test_img1.png",
                 -10.5,
                "pixfixPy/test/test_img/vibrance/vibrance.png")

def test_input_nonimage():
    with pytest.raises(OSError):
        vibrance("pixfixPy/test/test_img/vibrance/test_img1.R",
                 5,
                "pixfixPy/test/test_img/vibrance/vibrance.png")

def test_output_nonimage():
    with pytest.raises(OSError):
        vibrance("pixfixPy/test/test_img/vibrance/test_img1.png",
                 5,
                "pixfixPy/test/test_img/vibrance/vibrance.pdf")

def test_input_exist():
    with pytest.raises(FileExistsError):
        vibrance("pixfixPy/test/test_img/ffxiv/namazu.png",
                 5,
                "pixfixPy/test/test_img/vibrance/vibrance.png")

def test_output_path_valid():
    with pytest.raises(FileNotFoundError):
        vibrance("pixfixPy/test/test_img/vibrance/test_img1.png",
                 5,
                "@( * O * )@")
