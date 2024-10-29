import json
import os

def split_json_file(input_file, num_chunks=5):
    # Read the input JSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)  # Load the JSON data

    # Ensure data is a list
    if not isinstance(data, list):
        raise ValueError("The input JSON should be an array (list) of items.")

    # Calculate the size of each chunk
    total_items = len(data)
    items_per_chunk = total_items // num_chunks
    remainder = total_items % num_chunks

    # Split the data and write to new JSON files
    start_index = 0
    for chunk_number in range(num_chunks):
        # Calculate the end index for the current chunk
        end_index = start_index + items_per_chunk + (1 if chunk_number < remainder else 0)

        # Create the chunk file directly in the root directory
        chunk_filename = f"chunk_{chunk_number + 1}.json"

        # Write the chunk data to a new JSON file
        with open(chunk_filename, 'w', encoding='utf-8') as chunk_file:
            json.dump(data[start_index:end_index], chunk_file, ensure_ascii=False, indent=4)
        print(f"Created {chunk_filename} with {end_index - start_index} items.")

        # Update the start index for the next chunk
        start_index = end_index

if __name__ == "__main__":
    input_file_path = "Data.json"  # Replace with your JSON file path
    split_json_file(input_file_path)
