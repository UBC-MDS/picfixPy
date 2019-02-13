def vibrance(input_img, intensity=5, output_img=''):
    
    '''
    Adjust the vibrance of an image, given the intensity specificication

    Input
    ============
    input_img -- string of path for an image file in .png format
    intensity -- integer in range [0,10] to specificy intensity of vibrance enhancement applied to the image,
                 defaults to 5.
    output_img -- string path for output .png image with adjusted vibrance

    Returns
    ============
    an image file in .png format with specified vibrance in specified output path

    Example
    ============
    vibrance("../img/image.png", 2, "../img/vibrance_image.png")
    '''
