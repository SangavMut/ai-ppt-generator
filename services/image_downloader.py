import requests
import os
from PIL import Image

class ImageDownloader:
    def __init__(self):
        self.api_key = os.getenv('PEXEL_API_KEY')
        if not self.api_key:
            raise ValueError("Pexels API key is required. Set PEXEL_API_KEY environment variable.")
        self.url = "https://api.pexels.com/v1/search"

    def download_image(self, query, save_path="temp_image.jpg"):
        """Download a relevant image from Pexels based on the query"""
        try:
            headers = {'Authorization': self.api_key}
            params = {'query': query, 'per_page': 1, 'orientation': 'landscape'}
            response = requests.get(self.url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()
            if not data.get('photos'):
                raise ValueError(f"No images found for query: {query}")

            image_url = data['photos'][0]['src']['original']
            img_response = requests.get(image_url)
            img_response.raise_for_status()

            with open(save_path, 'wb') as f:
                f.write(img_response.content)

            return save_path

        except Exception as e:
            print(f"Error downloading image: {e}")
            return self.create_placeholder_image(save_path)

    def create_placeholder_image(self, save_path):
        """Create a placeholder image if download fails"""
        try:
            img = Image.new('RGB', (800, 600), color='#4A90E2')
            img.save(save_path)
            return save_path
        except Exception as e:
            print(f"Error creating placeholder image: {e}")
            return None
