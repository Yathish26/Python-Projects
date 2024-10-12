import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_website_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all the text from the webpage
        page_text = soup.get_text(separator=' ', strip=True)
        
        # Prepare a dictionary to save the data
        data = {
            "url": url,
            "text": page_text
        }

        # Define the filename and save path
        filename = 'website_text.json'
        save_path = os.path.join(os.getcwd(), filename)
        
        # Save the extracted text in a JSON file
        with open(save_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Text data has been saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")

if __name__ == "__main__":
    # Prompt user to enter a website URL
    website_url = input("Enter the website URL: ")
    fetch_website_text(website_url)
