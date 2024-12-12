"""
image_matrix.py

This module processes images to find and print pixel values below a specified threshold. 
It loads images from a directory, applies a condition to extract pixel values, and 
saves the results to a text file. This functionality is useful for analyzing image 
data and understanding pixel distributions.
"""


import os
from skimage import io
import numpy as np

def save_image_matrix_to_txt(image_path, output_txt_path):
    # Read the image
    image = io.imread(image_path)
    
    # Open the output text file
    with open(output_txt_path, 'w') as f:
        # Loop through each row of the image matrix
        for row in image:
            # Format each pixel in the row as [R G B] or [R G B A] depending on the image format
            formatted_row = '    '.join([f"[{pix[0]} {pix[1]} {pix[2]}]" if len(pix) == 3 
                                         else f"[{pix[0]} {pix[1]} {pix[2]} {pix[3]}]" for pix in row])
            
            # Write the formatted row to the file
            f.write(formatted_row + '\n')
    
    print(f"Matrix values saved to {output_txt_path}")

# Example usage
image_path = '/home/mohammed/Documents/ImageBackgroundRemover/static/results/JD2007_3.png'  # Input image path
output_txt_path = '/home/mohammed/Pictures/output.txt'  # Path to save the matrix values in .txt file

save_image_matrix_to_txt(image_path, output_txt_path)
