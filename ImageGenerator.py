import os
import requests
import openai
from dotenv import load_dotenv
from PIL import Image

class ImageGenerator:
    def __init__(self) -> str:
        self.image_url: str
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.APIKey = openai.api_key
        self.name = None

    def generateImage(self, Prompt, ImageCount, ImageSize):
        try:
            self.APIKey
            response = openai.Image.create(
            prompt = Prompt,
            n = ImageCount,
            size = ImageSize,
            )
            self.image_url = response['data']
            
            self.image_url = [image["url"] for image in self.image_url]
            print(self.image_url)
            return self.image_url
        except openai.error.OpenAIError as e:
            print(e.http_status)
            print(e.error)

    def downloadImage(self, names)-> None:
        try:
            self.name = names
            for url in self.image_url:
                image = requests.get(url)
            for name in self.name:
                with open("{}.png".format(name), "wb") as f:
                    f.write(image.content)
        except:
            print("An error occured")
            return self.name
        
    def imageVariations(self, ImageName, VariationCount, ImageSize):
        response = openai.Image.create_variation(
            image = open("{}.png".format(ImageName), "rb"),
            n = VariationCount,
            size = ImageSize
            )

        self.image_url = response['data']

        self.image_url = [image["url"] for image in self.image_url]
        print(self.image_url)
        return self.image_url