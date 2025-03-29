from PIL import Image
import numpy as np
def decodeimage(imagename):
#import pylance
# Open the image using Pillow
    image = Image.open(imagename)

# Convert the image to RGB (if it's not already in RGB mode)
    image_rgb = image.convert("RGB")

# Convert the image to a numpy array (matrix)
    image_matrix = np.array(image_rgb)

# Now image_matrix is a NumPy array where each element represents the RGB values    
    #print(image_matrix)
    #print(image_matrix.shape)  # Prints the dimensions of the image (height, width, 3)
    for i in range(image_matrix.shape[0]):
        for j in range(image_matrix.shape[1]):
            image_matrix[i][j][1] = 0
            image_matrix[i][j][2] = 0
    return(image_matrix)