import numpy as np

def rgb_to_ycbcr(rgb_image):
    # Calculate the ycbcr values using a given formula
    matrix_factor =  np.array([[.299, -.1687, .5], [.587, -.3313, -.4187], [.114, .5, -.0813]])  
    ycbcr = rgb_image.dot(matrix_factor)
    ycbcr[:,:,[1,2]] += 128
    
    return np.uint8(ycbcr)

def ycbcr_to_rgb(ycbcr_image):
    # Calculate the rgb-values using a given formula
    matrix_factor = np.array([[1., 1., 1.], [0., -.34414, 1.772], [1.402, -.71414, 0.]])
    result = ycbcr_image.astype(np.float)
    result[:,:,[1,2]] -= 128
    result = result.dot(matrix_factor)
    
    # Replace all values smaller than 0 and greater than 255 (can happen due to rounding errors) with 0 and 255
    np.putmask(result, result < 0, 0)
    np.putmask(result, result > 255, 255)
    
    return np.uint8(result)