import os
import json
from pathlib import Path
import requests

# Configuration
API_URL = "http://localhost:8000/convert" 

BASE_DIR = Path(__file__).parent / ".."
INPUT_DIR = BASE_DIR / "definitions/hood_CT_chest"
OUTPUT_DIR = BASE_DIR / "draft_cdes"

# Ensure the output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def process_json_file(file_path: Path):
    # Read the input JSON file
    with open(file_path, "r") as file:
        finding_json = json.load(file)

    # Send the JSON to the FastAPI endpoint
    response = requests.post(API_URL, json=finding_json)

    if response.status_code != 200:
        print(f"Error processing {file_path.name}: {response.text}")
        return

    # Create the output file path in draft_cdes with .cde.json suffix
    output_path = OUTPUT_DIR / f"{file_path.stem}.cde.json"
    
    # Save the converted CDE JSON to the output file
    with open(output_path, "w") as outfile:
        json.dump(response.json(), outfile, indent=4)

    print(f"Processed {file_path.name} and saved to {output_path}")

def main():
    # Ensure the input directory exists
    if not INPUT_DIR.exists():
        print(f"Input directory {INPUT_DIR} does not exist.")
        return

    # Process only .json files in the directory
    for json_file in INPUT_DIR.glob("*.json"):
        process_json_file(json_file)

if __name__ == "__main__":
    main()