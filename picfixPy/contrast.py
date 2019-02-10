def contrast(input_img, intensity=5, output_img):
    
    '''
    Adjust the contrast of an image, given the intensity specificication
    
    Input
    ============
    input_img -- string of path for an image file in .png format
    intensity -- integer in range [0,10] to specificy intensity of contrast enhancement applied to the image,
                 defaults to 5.
    output_img -- string path for output .png image with adjusted contrast 
    
    Returns
    ============
    an image file in .png format with adjusted contrast in specified output path
    
    Example
    ============
    contrast("../img/image.png", 2, "../img/contrast_image.png")
    '''