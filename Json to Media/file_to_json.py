import base64
import json


# Function to convert image to Base64 and save as JSON
def image_to_json(image_path, output_json_path):
    with open(image_path, "rb") as image_file:
        # Encode the image in Base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

        # Create a JSON object
        json_data = {
            "image_name": image_path.split("/")[-1],
            "image_data": encoded_string
        }

        # Save the JSON object to a file
        with open(output_json_path, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)


# Example usage
image_to_json("profile.jpg", "output_image.json")
