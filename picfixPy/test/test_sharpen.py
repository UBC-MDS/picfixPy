# This script tests the sharpen() function.

# sharpen(input_img, intensity, display, output_img) Sharpens an image with given intensity specification
# Input: input_img -- string of path for an image file.
#        intensity -- integer in range [0,10] to specificy intensity of sharpening applied to the image, defaults to 5.
#        display -- bool. If True, output will be displayed. Defaults to False.
#        output_img -- string path for output of the corresponding image with adjusted sharpening
# Output: an image file with adjusted sharpness in specified output path

import numpy as np
import pytest
import skimage.io
from picfixPy.sharpen import sharpen

# generate input image

test_img1 = np.array([[[6,6,6], [6,6,6], [6,6,6]],
                      [[14,14,12], [13,13,11], [12,12,10]],
                      [[7,7,7], [7,7,7], [7,7,7]]], dtype = 'uint8')

skimage.io.imsave("picfixPy/test/test_img/sharpen/test_img1.png", test_img1)

# generate expected output image when intensity is 5

expected_img1 = np.array([[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                          [[35, 35, 28], [29, 29, 22], [24, 24, 17]],
                          [[0, 0, 3], [1, 1, 3], [1, 1, 4]]], dtype = "uint8")

def test_zero_intensity():
    sharpen("picfixPy/test/test_img/sharpen/test_img1.png", 
             0,
             False,
             "picfixPy/test/test_img/sharpen/sharpen.png")
    output_img = skimage.io.imread("picfixPy/test/test_img/sharpen/sharpen.png")[:, :, :3]
    assert np.array_equal(output_img, test_img1), "Images should be indentical with 0 intensity."

def test_correct_sharpen():
    sharpen("picfixPy/test/test_img/sharpen/test_img1.png", 
             5,
             False,
             "picfixPy/test/test_img/sharpen/expected_img1.png")
    output_img = skimage.io.imread("picfixPy/test/test_img/sharpen/expected_img1.png")[:, :, :3]
    assert np.array_equal(output_img, expected_img1), "The image should be correctly sharpened with intensity of 5."

# test for exception handling

def test_input_string():
    with pytest.raises(AttributeError):
        sharpen(888, 5, False, "picfixPy/test/test_img/sharpen/sharpen.png")

def test_valid_intensity():
    with pytest.raises(ValueError):
        sharpen("picfixPy/test/test_img/sharpen/test_img1.png", 
                -10.5, 
                False,
                "picfixPy/test/test_img/sharpen/sharpen.png")

def test_input_nonimage():
    with pytest.raises(OSError):
        sharpen("picfixPy/test/test_img/sharpen/test_img1.R", 
                5, 
                False,
                "picfixPy/test/test_img/sharpen/sharpen.png")

def test_input_exist():
    with pytest.raises(FileNotFoundError):
        sharpen("picfixPy/test/test_img/ffxiv/namazu.png", 
                5, 
                "picfixPy/test/test_img/sharpen/sharpen.png")

def test_output_path_valid():
    with pytest.raises(FileNotFoundError):
        sharpen("picfixPy/test/test_img/sharpen/test_img1.png", 
                5, 
                False,
                "beasttribe/namazu/dailies.png")    
