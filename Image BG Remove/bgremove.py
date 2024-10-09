from rembg import remove
from PIL import Image
import os

# Define the image file name
input_image = 'roboto.jpg'  # Replace with your image file name
output_image = 'output_image.png'

# Check if the image exists in the root directory
if not os.path.exists(input_image):
    print(f"Error: {input_image} not found in the root directory.")
else:
    # Open the image
    with open(input_image, 'rb') as img_file:
        input_data = img_file.read()

    # Remove the background
    output_data = remove(input_data)

    # Save the result to the root directory
    with open(output_image, 'wb') as out_file:
        out_file.write(output_data)

    print(f"Background removed successfully and saved as {output_image}.")
