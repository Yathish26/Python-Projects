import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print(f"Successfully converted {csv_file_path} to {json_file_path}")

if __name__ == "__main__":
    input_csv_path = "Format.csv"
    output_json_path = "Clean.json"

    csv_to_json(input_csv_path, output_json_path)
