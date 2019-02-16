from distutils.core import setup
import numpy as np
from skimage.io import imread, imshow, imsave
import matplotlib as matplotlib
import colorsys

setup(
    name='picfixPy',
    version='0.2',
    description='Add quick vibrance, contast, and sharpen filters to your images',
    author='Miliban Keyim, George J. J. Wu, Mani Kohli',
    author_email = 'milibankeyim@gmail.com, mskcan@gmail.com, georgewujia@gmail.com',
    url = 'https://github.com/UBC-MDS/picfixPy',
    packages=['picfixPy'],
    license='LICENSE.md',
    long_description=open('README.md').read(),
)
