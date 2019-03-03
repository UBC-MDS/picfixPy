# dependencies
import numpy as np
import colorsys
from skimage.io import imread, imshow, imsave

def vibrance(input_img, intensity=5, display=False, output_img=''):

    '''
    Increase or decrease the vibrance of an image, given the intensity specificication.
    Works by increasing the overall colour intensity and saturation of the image, more so
    for colours that are less saturated. 
    
    Input
    ============
    img -- string. Path for an image file.
    intensity -- integer/float in range [-10,10]. Specificies intensity of vibrance applied to image.
    display -- bool. If True, output image will display
    output -- string path of output image
    
    Returns
    ============
    an image file with specified vibrance in specified output path
    '''
    
    try: 
        img = imread(input_img).astype(int)
    
    except AttributeError:
        print("Please use a string to specify the file path for an input image.")
        raise
    
    except FileNotFoundError:
        print("Cannot find image file.")
        raise

    except OSError:
        print("Please provide a valid image file.")
        raise
            
    # validate intensity level
    if (intensity < -10 or intensity > 10):
        raise ValueError("Intensity level must be between -10 and 10.")
    
    image = imread(input_img)
    
    H = image.shape[0]
    W = image.shape[1]
    D = image.shape[2]
    
    # load input image
    vibrance_image = np.ndarray((H,W,D), dtype = 'uint8')

    # lift pixel value restrictions between 0 and 255 temporarily
    for i in range(len(image)):
        for j in range(len(image[i])):

            r = image[i][j][0]
            g = image[i][j][1]
            b = image[i][j][2]

            hsv = colorsys.rgb_to_hsv(r, g, b)

            h = hsv[0]
            s = hsv[1]
            v = hsv[2]

            # Increasing saturation of desaturated pixels more than saturated pixels:                
            s = s * (1 + intensity/10)
            
            if s > 1.0:
                s = 1.0 
            else:
                s = s

            rgb = colorsys.hsv_to_rgb(h, s, v)

            vibrance_image[i][j][0] = rgb[0]
            vibrance_image[i][j][1] = rgb[1]
            vibrance_image[i][j][2] = rgb[2]

    if display == True:
        imshow(vibrance_image)

    if (output_img != ''):
        try: 
            imsave(output_img, vibrance_image)
        
        except FileNotFoundError:
            print("The file path for the output image is not valid.")
            raise

        except ValueError:
            print("Please specify a valid output image type.")
            raise
