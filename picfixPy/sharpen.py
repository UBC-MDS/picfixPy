# dependencies
import numpy as np
import skimage.io


def sharpen(input_img, intensity=5, display=False, output_img=''):
    
    '''
    Sharpens an image with given intensity specificication
    
    
    Input
    ============
    input_img -- string of path for an image file in .png format
    intensity -- integer in range [0,10] to specificy intensity of sharpening applied to the image,
                 defaults to 5.
    display -- bool. If True, output will be displayed. Defaults to False.
    output_img -- string path for output .png image with adjusted sharpening 
    
    Returns
    ============
    an image file in .png format with adjusted sharpening intensity in specified output path
    
    Example
    ============
    sharpen("../img/image.png", 5, display=False, "../img/sharpened_image.png")
    '''

    # load input image
    # lift pixel value restrictions between 0 and 255 temporarily
    try: 
        input_img = skimage.io.imread(input_img).astype(int)
    
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
        
    # validate intensity level
    if (intensity < 0 or intensity > 10):
        raise ValueError("Intensity level must be between 0 and 10.")
        
        
    # blurring of image
    # approximation of Gaussian blur 3x3 kernel
    kernel = np.array([[1.0,2.0,1.0], [2.0,4.0,2.0], [1.0,2.0,1.0]])
    kernel = kernel / np.sum(kernel)
    
    image_array = []
    for y in range(3):
        temp_array = np.copy(input_img)
        temp_array = np.roll(temp_array, y - 1, axis=0)
        for x in range(3):
            temp_array_X = np.copy(temp_array)
            temp_array_X = np.roll(temp_array_X, x - 1, axis=1)*kernel[y,x]
            image_array.append(temp_array_X)

    image_array = np.array(image_array)
    image_array_sum = np.sum(image_array, axis=0)
    
    
    # sharpening of image
    threshold = 0
    
    blurred = image_array_sum
    sharpened = float(intensity + 1) * input_img - float(intensity) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(input_image - blurred) < threshold
        np.copyto(sharpened, input_image, where=low_contrast_mask)
    #return sharpened
    
    
    # display or save sharpened image
    if (display == True):
        skimage.io.imshow(sharpened)
    
    if (output_img != ''):
        try: 
            skimage.io.imsave(output_img, sharpened, check_contrast=False)
        
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
  