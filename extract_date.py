import cv2
import numpy as np

def isolate_date(image_path, output_path):
    # Read the image
    img = cv2.imread(image_path)
    
    # Convert to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Define range for dark colors (adjust these values based on your findings)
    lower_dark = np.array([10, 120, 35])
    upper_dark = np.array([20, 140, 45])
    
    # Create a mask for dark colors
    mask = cv2.inRange(hsv, lower_dark, upper_dark)
    
    # Rest of the code remains the same...
    # (include the morphological operations, contour finding, etc.)
        
    # Apply morphological operations to clean up the mask
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours by area in descending order
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # Create a new mask for the largest contour (assumed to be the date)
    date_mask = np.zeros(mask.shape, dtype=np.uint8)
    if contours:
        cv2.drawContours(date_mask, [contours[0]], 0, (255), -1)
    
    # Apply the date mask to the original image
    result = cv2.bitwise_and(img, img, mask=date_mask)
    
    # Create a white background
    white_bg = np.ones(img.shape, dtype=np.uint8) * 255
    
    # Combine the result with the white background
    final_result = cv2.bitwise_or(result, white_bg)
    
    # Save the result
    cv2.imwrite(output_path, final_result)

# Usage
input_image = '/home/mohammed/Documents/ImageBackgroundRemover/static/results/JD2007_3.png'
output_image = '/home/mohammed/Pictures/image.jpg'
isolate_date(input_image, output_image)