# This script tests the contrast() function.

# contrast(input_img, intensity, output_img) adjusts the contrast of an image
# Input: input_img: string, path for the input image file
#        intensity: int, intensity of contrast enhancement, between 0 and 10, defaults to 5.
#        display: bool, display the enhanced image in an IDE, defaults to False.
#        output_img: string, path for the output image file
# Output: an image file at the specified output path

import numpy as np
import pytest
import skimage.io
from picfixPy.contrast import contrast

# generate input image

test_img1 = np.array([[[1,55,255], [2,55,255] ,[3,100,5]],
                      [[1,55,255], [2,55,255], [3,100,5]],
                      [[1,55,255], [2,55,255], [3,100,5]]], dtype = 'uint8')

skimage.io.imsave("picfixPy/test/test_img/contrast/test_img1.png", 
                  test_img1, check_contrast=False)

# generate output image when intensity is 5

expected_img1 = np.array([[[0,7,255], [0,7,255] ,[0,81,0]],
                         [[0,7,255], [0,7,255], [0,81,0]],
                         [[0,7,255], [0,7,255], [0,81,0]]], dtype='uint8')

# test for implementation correctness

def test_zero_intensity():
    contrast("picfixPy/test/test_img/contrast/test_img1.png", 
             0,
             False,
             "picfixPy/test/test_img/contrast/contrast.png")
    output_img = skimage.io.imread("picfixPy/test/test_img/contrast/contrast.png")
    assert np.array_equal(output_img, test_img1), "Images should be indentical with 0 intensity."

def test_correct_contrast():
    contrast("picfixPy/test/test_img/contrast/test_img1.png", 
             5,
             False,
             "picfixPy/test/test_img/contrast/expected_img1.png")
    output_img = skimage.io.imread("picfixPy/test/test_img/contrast/expected_img1.png")
    assert np.array_equal(output_img, expected_img1), "The image should be with adjusted contrast with an intensity of 5."    

# test for exception handling

def test_input_string():
    with pytest.raises(AttributeError):
        contrast(888, 5, False, "picfixPy/test/test_img/contrast/contrast.png")

def test_valid_intensity():
    with pytest.raises(ValueError):
        contrast("picfixPy/test/test_img/contrast/test_img1.png", 
                 -10.5, 
                 False,
                 "picfixPy/test/test_img/contrast/contrast.png")

def test_input_exist():
    with pytest.raises(FileNotFoundError):
        contrast("picfixPy/test/test_img/ffxiv/namazu.png", 
                 5, 
                 False,
                 "picfixPy/test/test_img/contrast/contrast.png")

def test_input_nonimage():
    with pytest.raises(OSError):
        contrast("picfixPy/test/test_img/contrast/test_img1.java", 
                 5, 
                 False,
                 "picfixPy/test/test_img/contrast/contrast.png")

def test_display_image():
    try:
        contrast("picfixPy/test/test_img/contrast/test_img1.png", 
                 5, 
                 True)
    except Exception: # pragma: no cover
        raise pytest.fail("Cannot display image, something went wrong.")  

def test_output_nonimage():
    with pytest.raises(ValueError):
        contrast("picfixPy/test/test_img/contrast/test_img1.png", 
                 5, 
                 False,
                 "picfixPy/test/test_img/contrast/test_img2.java")


def test_output_path_valid():
    with pytest.raises(FileNotFoundError):
        contrast("picfixPy/test/test_img/contrast/test_img1.png", 
                 5, 
                 False,
                 "beasttribe/namazu/dailies.png")    