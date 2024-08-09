import base64
import json


# Function to convert JSON back to image
def json_to_image(json_path, output_image_path):
    # Load the JSON file
    with open(json_path, 'r') as json_file:
        json_data = json.load(json_file)

    # Decode the Base64 string to binary image data
    image_data = base64.b64decode(json_data['image_data'])

    # Save the binary data to an image file
    with open(output_image_path, 'wb') as image_file:
        image_file.write(image_data)


# Example usage
json_to_image("output_image.json", "reconstructed_image.png")
