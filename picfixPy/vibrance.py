# dependencies
import numpy as np
import matplotlib as plt
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

    # HSV conversion from RGB array
    hsv = plt.colors.rgb_to_hsv(image) * np.array([1, 1 + (intensity / 10), 1])

    # Restrict
    def restrict(x):
        if x > 1:
            x = 1.0
            return x
        else:
            return x

    np_restrict = np.vectorize(restrict)
    saturation = hsv[:, :, 1]
    hsv[:, :, 1] = np_restrict(saturation) #Make sure saturation does not exceed 1.0

    #convert back to RGB
    vibrance_image  = plt.colors.hsv_to_rgb(hsv).astype('uint8')

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
