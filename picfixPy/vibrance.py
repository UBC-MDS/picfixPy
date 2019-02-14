def vibrance(input_img, intensity=5, display=False, output_img=''):

    '''
    Increase or decrease the vibrance of an image, given the intensity specificication.

    Input
    ============

    img -- string. Path for an image file in .jpg, .jpeg, .png, .tiff format.
    intensity -- integer/float in range [-10,10]. Specificies intensity of vibrance applied to image.
    display -- bool. If True, output image will display
    output -- string path of output image

    Returns
    ============
    an image file in .jpg, .jpeg, .png, .tiff format with specified vibrance in specified output path

    '''
    output_image = np.ndarray(input_img.shape, dtype = 'uint8')

    for i in range(len(input_img)):
        for j in range(len(input_img[i])):

            r = input_img[i][j][0]
            g = input_img[i][j][1]
            b = input_img[i][j][2]

            hsv = colorsys.rgb_to_hsv(r, g, b)

            h = hsv[0]
            s = hsv[1]
            v = hsv[2]

            # Increasing saturation of desaturated pixels more than saturated pixels:
            s = s * (1 + intensity/10)

            if s > 1.0:
                s = 0.8
            if s < 0.0:
                s = 0.0
            else:
                s = s

            rgb = colorsys.hsv_to_rgb(h, s, v)

            output_image[i][j][0] = rgb[0]
            output_image[i][j][1] = rgb[1]
            output_image[i][j][2] = rgb[2]

    if display == True:
        imshow(output_image)

    if output != '':
        skimage.io.imsave("", output_image)
