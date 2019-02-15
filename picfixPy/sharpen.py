def sharpen(input_img, intensity=5, output_img=''):
    
    '''
    Sharpens an image, given the intensity specificication
    
    
    Input
    ============
    input_img -- string of path for an image file in .png format
    intensity -- integer in range [0,10] to specificy intensity of sharpening applied to the image,
                 defaults to 5.
    display -- bool. If True, output will be displayed. Defaults to False.
    output_img -- string path for output .png image with adjusted sharpening 
    
    Returns
    ============
    an image file in .png format with adjusted sharpening level in specified output path
    
    Example
    ============
    sharpen("../img/image.png", 5, display=False, "../img/sharpened_image.png")
    '''

    # load input image
    # lift pixel value restrictions between 0 and 255 temporarily
    try: 
        img = skimage.io.imread(input_img).astype(int)
    
    except AttributeError:
        print("Please use a string to specify the file path for an input image.")
        raise
    
    except OSError:
        print("Please provide an image file.")
        raise
    
    except FileNotFoundError:
        print("Cannot find image file.")
            
    except Exception as error:
        print("Cannot load image, something went wrong :(")
        print(error)
        raise
        
    
    
    
    
    # display or save enhanced image
    if (display == True):
        skimage.io.imshow(enhanced_img)
    
    if (output_img != ''):
        try: 
            skimage.io.imsave(output_img, enhanced_img, check_contrast=False)
        
        except OSError:
            print("Please output an image.")
            raise
        
        except FileNotFoundError:
            print("The file path for the output image is not valid.")
            raise

        except Exception as error:
            print("Cannot save image to file, something went wrong :(")
            print(error)
            raise
  