import os
import pyheif
from PIL import Image

def convert_heic_to_jpg(directory):
    # Get a list of all .heic files in the directory
    heic_files = [f for f in os.listdir(directory) if f.lower().endswith('.heic')]
    
    # Loop through each .heic file and convert it to .jpg
    for filename in heic_files:
        # Load the HEIC file
        heif_file = pyheif.read(os.path.join(directory, filename))
        
        # Convert HEIC to an image object
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data, 
            "raw", 
            heif_file.mode, 
            heif_file.stride
        )
        
        # Define new filename with .jpg extension
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        new_file_path = os.path.join(directory, new_filename)
        
        # Save the image as a .jpg file
        image.save(new_file_path, "JPEG")
        print(f"Converted {filename} to {new_filename}")

    print(f"Converted {len(heic_files)} .heic files to .jpg in the folder {directory}.")

# Specify the folder where the .heic files are located
folder_path = "/home/mohammed/Downloads/Telegram Desktop/13/13/"  # Change this to your folder path

convert_heic_to_jpg(folder_path)
