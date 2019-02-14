def sharpen(input_img, intensity=5, output_img=''):
    
    '''
    Sharpens an image, given the intensity specificication
    
    Input
    ============
    input_img -- string of path for an image file in .png format
    intensity -- integer in range [0,10] to specificy intensity of sharpening applied to the image,
                 defaults to 5.
    output_img -- string path for sharpened .png image
    
    Returns
    ============
    an sharpened image file in .png format in specified output path
    
    Example
    ============
    sharpen("../img/image.png", 2, "../img/sharpened_image.png")
    '''