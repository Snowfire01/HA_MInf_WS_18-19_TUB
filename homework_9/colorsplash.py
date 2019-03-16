import numpy as np
from PIL import Image

#############################################################
## Color conversion formulas are extracted from homework 8 ##
#############################################################################################################################
                                                                                                                            #
def rgb_to_ycbcr(rgb_image):                                                                                                #
    # Calculate the ycbcr values using a given formula                                                                      #
    matrix_factor =  np.array([[.299, -.1687, .5], [.587, -.3313, -.4187], [.114, .5, -.0813]])                             #
    ycbcr = rgb_image.dot(matrix_factor)                                                                                    #   
    ycbcr[:,:,[1,2]] += 128                                                                                                 #
                                                                                                                            #
    return np.uint8(ycbcr)                                                                                                  #
                                                                                                                            #
def ycbcr_to_rgb(ycbcr_image):                                                                                              #
    # Calculate the rgb-values using a given formula                                                                        #
    matrix_factor = np.array([[1., 1., 1.], [0., -.34414, 1.772], [1.402, -.71414, 0.]])                                    #
    result = ycbcr_image.astype(np.float)                                                                                   #    
    result[:,:,[1,2]] -= 128                                                                                                #
    result = result.dot(matrix_factor)                                                                                      # 
                                                                                                                            #
    # Replace all values smaller than 0 and greater than 255 (can happen due to rounding errors) with 0 and 255             #
    np.putmask(result, result < 0, 0)                                                                                       #
    np.putmask(result, result > 255, 255)                                                                                   #
                                                                                                                            #
    return np.uint8(result)                                                                                                 #
                                                                                                                            #
#############################################################################################################################
## Color conversion formulas are extracted from homework 8 ##
#############################################################

def apply_color_splash(image, filter_mode):
    image_data = np.asarray(image, dtype=np.uint8)
    
    ycbcr_image = rgb_to_ycbcr(image_data)
    cb_image = ycbcr_image[:, :, 1]
    cr_image = ycbcr_image[:, :, 2]

    if filter_mode == "v":
        cb_image[cb_image < 128] = 128
        cr_image[cr_image < 128] = 128
    elif filter_mode == "b":
        cb_image[cb_image < 128] = 128
        cr_image[cr_image > 128] = 128
    elif filter_mode == "g":
        cb_image[cb_image > 128] = 128
        cr_image[cr_image > 128] = 128
    elif filter_mode == "rg":
        cb_image[cb_image > 128] = 128
        cr_image[cr_image < 128] = 128

    
    rgb_image = ycbcr_to_rgb(ycbcr_image)
    
    return rgb_image.astype(np.uint8)