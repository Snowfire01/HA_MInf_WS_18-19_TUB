%matplotlib inline
%config InlineBackend.figure_format = 'retina'  

from PIL import Image 
import numpy as np
import matplotlib.pyplot as plt
import os.path

import Color_Splash as cs

# Let user input a file path and load the file into memory with PIL if the path is valid
source_img_path = input("Please enter the path to the image file (.jpg) you want to apply the filter to: ")

while not (os.path.isfile(source_img_path) and source_img_path.endswith(".jpg")):    
    if not os.path.isfile(source_img_path):
        source_img_path = input("The path you specified is invalid. Please check your input and file location and enter a new path: ")
    elif not source_img_path.endswith(".jpg"):
        source_img_path = input("The specified file has an invalid format. It needs to be a .jpg-file! Please choose another:  ")

image_file = Image.open(source_img_path) 
image_file.load() 

# Let user select the filter mode (with input validation)
filter_mode = input("Please select one of the following filter modes: violet (v), blue (b), green (g), red-green(rg): ")

while not filter_mode in ["v", "b", "g", "rg"]:
       filter_mode = input("That's not a valid filter mode. Please choose one out of v, b, g and rg: ")
        
# Call the filter library and do the magic
image_splash = cs.apply_color_splash(image_file, filter_mode)

# Plot image
plt.axis('off')
plt.imshow(image_splash)