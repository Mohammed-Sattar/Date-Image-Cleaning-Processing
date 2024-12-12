"""
detect_crop.py

This script detects and crops the date from an image. It loads an image, converts it 
to grayscale, applies Gaussian blur to reduce noise, and uses Canny edge detection to 
find contours. The largest contour is likely the date, which can be further processed 
for extraction.
"""

import cv2
import numpy as np
import os

# Load the image
image_path = '/home/mohammed/Documents/ImageBackgroundRemover/static/results/JD2007_3.png'  # Replace with your image path
image = cv2.imread(image_path)

# Convert to grayscale for processing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply GaussianBlur to reduce noise
blurred = cv2.GaussianBlur(gray, (15,15), 0)

# Use Canny Edge detection
edges = cv2.Canny(blurred, 5,15)

# Find contours in the edge map
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get the largest contour, which is likely the date
if contours:
    largest_contour = max(contours, key=cv2.contourArea)

    # Get bounding box around the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Add some padding around the bounding box
    padding = 20
    x = max(0, x - padding)
    y = max(0, y - padding)
    w = min(image.shape[1] - x, w + 2 * padding)
    h = min(image.shape[0] - y, h + 2 * padding)

    # Crop the image to the bounding box
    cropped_image = image[y:y+h, x:x+w]

    # Save the cropped image
    output_path = os.path.join('/home/mohammed/Pictures/', 'cropped_date.png')
    cv2.imwrite(output_path, cropped_image)
    print(f"Cropped image saved to {output_path}")
else:
    print("No contours found.")
