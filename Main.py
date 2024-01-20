import requests
from bs4 import BeautifulSoup
import os
import requests.exceptions
import os.path
from urllib.parse import urljoin

def download_first_photo(url, save_directory):
    try:
        # Ensure that the save directory exists
        os.makedirs(save_directory, exist_ok=True)

        # Add User-Agent header to the request
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Initial request to the URL
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print('Error: Failed to retrieve data from the URL. Reason:', str(e))
            return

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the HTML element that contains the gallery link
        gallery_link = soup.find('a', {'class': 'gallery-link'})
        
        if not gallery_link:
            raise Exception('Error: Gallery link not found.')

        gallery_url = urljoin(url, gallery_link['href'])

        # Gallery request
        try:
            gallery_response = requests.get(gallery_url, headers=headers)
            gallery_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print('Error: Failed to retrieve the gallery data. Reason:', str(e))
            return

        # Parse the gallery HTML content using BeautifulSoup
        gallery_soup = BeautifulSoup(gallery_response.content, 'html.parser')

        # Find the first image element in the gallery
        image_element = gallery_soup.find('img')
        
        if not image_element:
            raise Exception('Error: Image element not found in the gallery.')

        image_url = urljoin(gallery_url, image_element['src'])

        # Request to download the first photo
        try:
            image_response = requests.get(image_url, headers=headers)
            image_response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print('Error: Failed to download the first photo. Reason:', str(e))
            return

        # Save the image to a file with exception handling
        try:
            with open(os.path.join(save_directory, 'first_photo.jpg'), 'wb') as f:
                f.write(image_response.content)
            print('Downloaded the first photo.')
        except Exception as e:
            print('Error: Failed to save the image. Reason:', str(e))
    except requests.exceptions.RequestException as e:
        print('Error: Unable to retrieve data from the URL. Reason:', str(e))

# Example usage
url = 'https://www.example.com/category'
save_directory = 'path/to/save/directory'
download_first_photo(url, save_directory)
