# This script tests the sharpen() function.

# sharpen(input_img, intensity, output_img) adjusts the sharpness of an image
# Input: input_img: string, path for the input image file
#        intensity: int, intensity of sharpness enhancement, between 0 and 10, defaults to 5.
#        output_img: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
import skimage.io
from PicFixPy import sharpen

# generate input image

test_img1 = np.array([[[ 10,  20,  40], [ 20,  40,  10], [ 40,  10,  20]],
                      [[ 40,  80, 160], [ 80, 160,  40], [160,  40,  80]],
                      [[ 60, 120, 240], [120, 240,  60], [240,  60, 120]]], dtype = "uint8")

skimage.io.imsave("pixfixPy/test/test_img/sharpen/test_img1.png", test_img1)

# generate expected output image when intensity is 10

expected_img1 = np.array([[[ 100,  120,  140], [ 120,  140,  110], [ 140,  110,  120]],
                          [[ 140,  180, 250], [ 180, 250,  140], [250,  140,  180]],
                          [[ 160, 220, 240], [220, 240,  160], [240,  160, 220]]], dtype = "uint8")

def test_zero_intensity():
    sharpen("pixfixPy/test/test_img/sharpen/test_img1.png", 
             0,
             "pixfixPy/test/test_img/sharpen/sharpen.png")
    output_img = skimage.io.imread("pixfixPy/test/test_img/sharpen/sharpen.png")[:, :, :3]
    assert np.array_equal(output_img, test_img1), "Images should be indentical with 0 intensity."

def test_correct_sharpen():
    sharpen("pixfixPy/test/test_img/sharpen/test_img1.png", 
             5,
             "pixfixPy/test/test_img/sharpen/expected_img1.png")
    output_img = skimage.io.imread("pixfixPy/test/test_img/sharpen/testImg1_output.png")[:, :, :3]
    assert np.array_equal(output_img, expected_img1), "The image returned should be identical with 0 intensity."

# test for exception handling

def test_input_string():
    with pytest.raises(AttributeError):
        sharpen(888, 5, "pixfixPy/test/test_img/sharpen/sharpen.png")

def test_valid_intensity():
    with pytest.raises(AttributeError):
        sharpen("pixfixPy/test/test_img/sharpen/test_img1.png", 
                 -10.5, 
                "pixfixPy/test/test_img/sharpen/sharpen.png")

def test_input_nonimage():
    with pytest.raises(OSError):
        sharpen("pixfixPy/test/test_img/sharpen/test_img1.R", 
                 5, 
                "pixfixPy/test/test_img/sharpen/sharpen.png")

def test_output_nonimage():
    with pytest.raises(OSError):
        sharpen("pixfixPy/test/test_img/sharpen/test_img1.png", 
                 5, 
                "pixfixPy/test/test_img/sharpen/sharpen.pdf")

def test_input_exist():
    with pytest.raises(FileExistsError):
        sharpen("pixfixPy/test/test_img/ffxiv/namazu.png", 
                 5, 
                "pixfixPy/test/test_img/sharpen/sharpen.png")

def test_output_path_valid():
    with pytest.raises(FileNotFoundError):
        sharpen("pixfixPy/test/test_img/sharpen/test_img1.png", 
                 5, 
                "@( * O * )@")    