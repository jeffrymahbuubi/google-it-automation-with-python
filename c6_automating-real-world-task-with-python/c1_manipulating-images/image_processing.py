from PIL import Image
import os

source_folder = './images'  # Current directory
destination_folder = '/opt/icons/'

# Ensure the destination directory exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate over all files in the source directory
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    # Check if the file is an image
    try:
        with Image.open(file_path) as image:

            # Convert the image to RGB mode
            image = image.convert('RGB')

            # Rotate and resize
            modified_image = image.rotate(-90).resize((128, 128))

            # Save the modified image to the destination folder in .jpeg format
            dest_file_path = os.path.join(destination_folder, os.path.splitext(file_name)[0] + '.jpeg')
            modified_image.save(dest_file_path, 'JPEG')

    except Exception as e:
        print(f"Error processing file {file_name}: {e}")

print("Processing complete!")
