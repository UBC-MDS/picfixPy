# This script tests the contrast() function.

# contrast(input_img, intensity, output_img) adjusts the contrast of an image
# Input: input_img: string, path for the input image file
#        intensity: int, intensity of contrast enhancement, between 0 and 10, defaults to 5.
#        output_img: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
import skimage.io
from picfixPy import contrast

# generate input image

test_img1 = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                      [[6,66,43], [33,55,63], [22,56,70]],
                      [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')

# generate output image when intensity is 5

expected_img1 = np.array([[[4,77,245], [44,44,32] ,[60,70,80]],
                         [[6,66,43], [33,55,63], [22,56,70]],
                         [[4,55,66], [65,77,43], [33,45,22]]], dtype = 'uint8')

# test for implementation correctness

def test_zero_intensity():
    contrast("pixfixPy/test/test_img/contrast/test_img1.png", 
             0,
             "pixfixPy/test/test_img/contrast/contrast.png")
    output_img = skimage.io.imread("pixfixPy/test/test_img/contrast/contrast.png")[:, :, :3]
    assert np.array_equal(output_img, test_img1), "Images should be indentical with 0 intensity."

def test_correct_contrast():
    contrast("pixfixPy/test/test_img/contrast/test_img1.png", 
             5,
             "pixfixPy/test/test_img/contrast/expected_img1.png")
    output_img = skimage.io.imread("pixfixPy/test/test_img/contrast/testImg1_output.png")[:, :, :3]
    assert np.array_equal(output_img, expected_img1), "The image returned should be identical with 0 intensity."    

# test for exception handling

def test_input_string():
    with pytest.raises(AttributeError):
        contrast(888, 5, "pixfixPy/test/test_img/contrast/contrast.png")

def test_valid_intensity():
    with pytest.raises(AttributeError):
        contrast("pixfixPy/test/test_img/contrast/test_img1.png", 
                 -10.5, 
                "pixfixPy/test/test_img/contrast/contrast.png")

def test_input_nonimage():
    with pytest.raises(OSError):
        contrast("pixfixPy/test/test_img/contrast/test_img1.R", 
                 5, 
                "pixfixPy/test/test_img/contrast/contrast.png")

def test_output_nonimage():
    with pytest.raises(OSError):
        contrast("pixfixPy/test/test_img/contrast/test_img1.png", 
                 5, 
                "pixfixPy/test/test_img/contrast/contrast.pdf")

def test_input_exist():
    with pytest.raises(FileExistsError):
        contrast("pixfixPy/test/test_img/ffxiv/namazu.png", 
                 5, 
                "pixfixPy/test/test_img/contrast/contrast.png")

def test_output_path_valid():
    with pytest.raises(FileNotFoundError):
        contrast("pixfixPy/test/test_img/contrast/test_img1.png", 
                 5, 
                "@( * O * )@")    