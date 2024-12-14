# Image Background Remover

## Overview
The Image Background Remover is a program designed to remove backgrounds from images using advanced techniques such as deep learning and image processing. This code was specifically used for cleaning, removing the background and processing date images. It was used during the Medina Hackathon 2023 for enhancing our dataset. The application leverages a pre-trained U2NET model for effective background removal and includes various scripts for processing images, renaming files, and analyzing pixel values.

## File Descriptions
### __init__.py
This module initializes the Image Background Remover package. It imports necessary libraries, loads the pre-trained U2NET model, and defines the removeBg function to process images by removing their backgrounds.

### app.py
The main application script that serves as the entry point for the background removal process. This file orchestrates the overall functionality of the application.

### config.py
Handles the configuration settings for the application. It loads configurations from a JSON file located at /etc/config.json and provides access to the SECRET_KEY for secure operations.

### data_loader.py
Defines classes for loading and transforming image datasets, including RescaleT, RandomCrop, ToTensor, and SalObjDataset. These classes preprocess images for the background removal model, ensuring they are in the correct format and size.

### detect_crop.py
Detects and crops dates from images. It loads an image, converts it to grayscale, applies Gaussian blur, and uses Canny edge detection to find contours, isolating the largest contour as the date.

### extract_date.py
Isolates the date from an image using color masking techniques. It reads an image, converts it to the HSV color space, and creates a mask for dark colors, applying morphological operations and contour finding techniques.

### heic_rename.py
Renames all HEIC files in a specified directory to a standardized format. It retrieves all HEIC files, sorts them, and renames them sequentially for easier management.

### heic_to_jpg.py
Converts HEIC files to JPG format. It reads all HEIC files in a specified directory, loads them using the pyheif library, and saves them as JPG images for compatibility with various image processing libraries.

### hsv_value.py
Analyzes the HSV values of an image to identify dark areas. It reads an image, converts it to the HSV color space, and creates a mask for dark regions, useful for isolating specific features.

### image_matrix.py
Processes images to find and print pixel values below a specified threshold. It loads images from a directory, applies a condition to extract pixel values, and saves the results to a text file for analysis.

### canny_edge.ipynb
After using the app.py to remove the background of an image, this Jupyter Notebook further enhances and removes residual unwanted parts of the image.
The process employs the Canny edge detection algorithm and watershed segmentation for edge detection and noise removal in images. It starts by converting the input image from RGBA to grayscale, followed by applying the Canny algorithm to identify edges. Detected edges are filled using binary hole filling techniques, and an elevation map is created with the Sobel filter to analyze the image gradient. Morphological dilation enhances features, and markers are generated for watershed segmentation to distinguish background and foreground. The watershed algorithm segments the image, filling any holes to create a binary mask. Labeled regions are overlaid on the original image, and the segmentation mask is dilated to isolate areas of interest. Contour analysis determines pixel intensity percentages, setting areas to white in the output image if they meet the specified condition, with the final processed output displayed.

### histogram_visualizer.ipynb
A Jupyter Notebook used for visualizing image histograms, allowing me to analyze the distribution of pixel values in images. I used it to find the optimal threshold for separating the date from the background.

## Usage
To use the Image Background Remover, ensure that you have the necessary dependencies installed. You must also the model.pth file saved in the `saved_models/u2net/` directory. To know more about this visit the original repository. Then run the app.py script. You can also explore the Jupyter Notebooks for detailed demonstrations of specific functionalities.

## Acknowledgements
This project utilizes the pretrained U2NET model for background removal. The code for background removal is based on the [Image-Background-Remover-Python](https://github.com/hassancs91/Image-Background-Remover-Python) repository. For more details on how the model was implemented, please refer to the original repository.

## Installation
1. Clone the repository: `git clone https://github.com/Mohammed-Abdulrahman/ImageBackgroundRemover.git`
2. Navigate to the cloned directory: `cd ImageBackgroundRemover`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the app.py script: `python app.py`

## License
This project is licensed under the MIT License. See the LICENSE file for details.
