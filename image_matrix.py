import os
import glob  # New import to handle file patterns
from skimage import io

img_directory = "/home/mohammed/Pictures/Ajwa/"
for imgPath in glob.glob(os.path.join(img_directory, "*.jpg")):
    print(f"Processing: {imgPath}")
    image = io.imread(imgPath)
    
    # Find values below 150
    below_150 = image[image < 150]
    
    # Print the matrices with values below 150
    print("Pixel values below 150:")
    print(below_150)
    
    break