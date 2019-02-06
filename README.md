# PicFixPy


#### DSCI 524 Collaborative Software Development Project  
  
#### Team Members

| Name                | Github.com Username |
| ------------------- | ------------------- |
| Miliban Keyim       | mkeyim              |
| George J. J. Wu     | GeorgeJJW           |
| Mani Kohli          | ksm45               |


#### Project Overview:

PicFix will allows you to quickly touch-up images in an IDE (i.e. Jupyter notebook, rstudio) without powering up a full-scale image processing software(i.e. ADOBE, MS). Be able to quickly apply contrast, vibrance, and a smart sharpen to photos quickly and swiftly! Simple to use, no fuss, we can simply use the following functions. Full blown photo editing libraries and softwares can be heavy weight, we just want to quickly touch up and fix up an image in the IDE without exiting the IDE.

#### Functions:

###### sharpen
Given an image, increase the weight of the edges, (via convolution), returns an image.

###### contrast
Given an image, make dark pixels much darker, and bright pixels slightly darker, returns an image.

###### vibrance
Given an image, increase the overall intensity and saturation by increasing more for colours that were less saturated to begin with, returns an image.

How this project fit into the Python and R ecosystems

#### Python ecosystem

[OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html) provides Python with an immersive package for complex image processing. However, what if you just need a quick, easy solution for basic image enhancement without having to dig into substantial documentation and implementations? Our proposal is to offer a simple alternative, allowing users to have the ability to enhance images quickly without the overhead of heavy library resources.


