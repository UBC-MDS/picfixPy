# dependencies
import numpy as np
import skimage.io
import sys

def contrast(input_img, intensity=5, display=False, output_img=''):
    
    '''
    Adjust the contrast of an image, given the intensity specificication
    
    Input
    ============
    input_img -- string of path for an image file in .png format
    intensity -- integer in range [0,10] to specificy intensity of contrast enhancement applied to the image,
                 defaults to 5.
    display -- bool. If True, output will be displayed. Defaults to False.
    output_img -- string path for output .png image with adjusted contrast 
    
    Returns
    ============
    an image file in .png format with adjusted contrast in specified output path
    
    Example
    ============
    contrast("../img/image.png", 5, display=False, "../img/contrast_image.png")
    '''

    # load input image
    # lift pixel value restrictions between 0 and 255 temporarily
    try: 
        img = skimage.io.imread(input_img).astype(int)
    
    except AttributeError:
        print("Please use a string to specify the file path for an input image.")
        raise
    
    except OSError:
        print("Please provide the path to an image file.")
        raise
    
    except FileExistsError:
        print("Cannot find image file.")
            
    except Exception as error:
        print("Cannot load image, something went wrong :(")
        print(error)
        raise

    # validate intensity level
    if (intensity < 0 or intensity > 10):
        raise ValueError("Intensity level must be between 0 and 10.")

    # map user specified intensity to a desired level of contrast (C)
    # note that intensity is between the range 0 and 10
    # and that contrast level (C) is between the range 0 and 128
    # attribution: https://stackoverflow.com/questions/345187/math-mapping-numbers
    C = intensity / 10 * 128

    # obtain contrast correction factor (F) from the desired contrast level (C)
    # attribution: https://bit.ly/2EObG6B
    F = (259 * (C + 255)) / (255 * (259 - C))

    # perform contrast enhancement to image
    enhanced_img = F * (img - 128) + 128

    # restrict values to being an integer between 0 and 255 for each pixel
    def restrict(x):
        x = round(x, 0)
        if x > 255:
            return 255
        elif x < 0:
            return 0
        else:
            return x
    
    np_restrict = np.vectorize(restrict)
    enhanced_img = np_restrict(enhanced_img).astype(int)

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

        

