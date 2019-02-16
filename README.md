# picfixPy
#### A DSCI-524 collaborative software development project  

### Project Overview

Image enhancement is typically done with a full-scale editing software such as Adobe Photoshop or GIMP, but what if we just want to quickly touch up an image during prototyping in a programming environment?

`picfixPy` allows users to quickly enhance images in an integrated development environment (IDE) (e.g. Jupyter notebook, PyCharm) without powering up an image editing software. Users can quickly adjust the sharpness, contrast, and vibrance of .png images, by simply calling the corresponding functions. This package currently offers three essential image enhancement functions, and we hope to implement additional features in the near future.

### To install
 
```
pip install git+https://github.com/UBC-MDS/picfixPy.git
```

### To upgrade

```
pip install --upgrade git+https://github.com/UBC-MDS/picfixPy.git
```

### To use

#### sharpen(): enhance the sharpness of your image

```
from picfixPy.sharpen import sharpen
sharpen('input.png', 4, False, 'sharpen_output.png')
```

Arguments:

- input_img: path to an input image
- intensity: level of sharpness enhancement, between 0 and 10, defaults to 5.
- display: print image to console if `True`, defaults to `False`.
- output_img: path to save the output image

![](/picfixPy/test/test_img/sharpen_output.png)   

#### contrast(): enhance the contrast of your image

```
from picfixPy.contrast import contrast
contrast('input.png', 4, False, 'contrast_output.png')
```

Arguments:

- input_img: path to an input image
- intensity: level of contrast enhancement, between 0 and 10, defaults to 5.
- display: print image to console if `True`, defaults to `False`.
- output_img: path to save the output image

![](/picfixPy/test/test_img/contrast_output.png)  

#### vibrance(): enhance the colour vibrance of your image  

```
from picfixPy.vibrance import vibrance
vibrance('input.png', 4, False, 'vibrance_output.png')
```

Arguments:

- input_img: path to an input image
- intensity: level of vibrance enhancement, between -10 and 10, defaults to 5.
- display: print image to console if `True`, defaults to `False`.
- output_img: path to save the output image

![](/picfixPy/test/test_img/vibrance_output.png)  

### Supported image types

- .jpg 
- .png
- .tiff

### Dependencies

- numpy
- matplotlib
- scikit-image
- colorsys

### Fitting into the Python ecosystem

[OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) provides Python with an immersive package for complex image processing. However, even for basic image enhancements, users typically still have to dig into a substantial amount of documentation and implementation details. This project offers a simple alternative, allowing users to have the ability to enhance images quickly during prototyping without the overhead of heavy library resources.

### Team Members

| Name                | Github handle |
| ------------------- | ------------------- |
| Miliban Keyim       | [mkeyim](https://github.com/mkeyim) |
| George J. J. Wu     | [GeorgeJJW](https://github.com/GeorgeJJw) |
| Mani Kohli          | [ksm45](https://github.com/ksm45) |
