from distutils.core import setup

setup(
    name='picfixPy',
    version='0.2',
    description='Add quick vibrance, contast, and sharpen filters to your images',
    author='Miliban Keyim, George J. J. Wu, Mani Kohli',
    author_email = 'milibankeyim@gmail.com, mskcan@gmail.com, georgewujia@gmail.com',
    url = 'https://github.com/UBC-MDS/picfixPy',
    packages=['picfixpy',],
    license='LICENSE.md',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "numpy",
        "matplotlib",
        'scikit-image',
        'colorsys'
        "pytest",

],
)
