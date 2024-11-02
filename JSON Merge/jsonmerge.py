import os
import json

def merge_json_files(directory):
    merged_data = []
    
    if not os.path.isdir(directory):
        print("Directory does not exist.")
        return
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        merged_data.extend(data)  # Add items from lists
                    else:
                        merged_data.append(data)  # Add single JSON objects
            except json.JSONDecodeError:
                print(f"Warning: {filename} is not a valid JSON file.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    output_file = os.path.join(directory, 'Set.json')
    try:
        with open(output_file, 'w') as json_output:
            json.dump(merged_data, json_output, indent=4)
        print(f"All JSON files merged into {output_file}")
    except Exception as e:
        print(f"Error writing to Set.json: {e}")

directory = input("Enter the directory containing JSON files to merge: ")
merge_json_files(directory)
