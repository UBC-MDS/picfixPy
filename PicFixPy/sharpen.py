def sharpen(imput_img, intensity, output_img):
    
    '''
    Sharpens an image, given the intensity specificication
    
    Input
    ============
    img -- string of path for an image file in .png or .jpeg format
    intensity -- integer in the range [0,10] to specificy intensity of sharpness applied to the image
    output -- string path of sharpened output image 
    
    Returns
    ============
    an image file in .png or .jpeg format with specified sharpness in specified output path
    
    Example
    ============
    sharpen("../img/image.png", 1.2, "../img/sharpened_image.png")
    
    '''