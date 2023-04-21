import os
from dotenv import load_dotenv
import openai
import requests
from ImageGenerator import ImageGenerator
from insta import InstaPostManager


load_dotenv('.env')

openai.organization = "org-yS6tGvPIqZsH0naiRkgkLFQQ"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "Professor de Ciência da Computação"},
            {"role": "user", "content": "Crie um post de instagram bem humorado dizendo que é um teste do estagiário tentando usar o ChatGPT com Instagram, finalize dizendo que em breve contaremos como fazer isso"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

image_generator = ImageGenerator()

image_generator.generateImage(
    Prompt = "Um fundo em gradiente de azul para branco, com um robô na frente e um balão de fala com a palavra TESTE",
    ImageCount = 2,    
    ImageSize = '1024x1024'
)

image_generator.downloadImage(names=[
    "Image1",
    "Image2",
    ]
)

print(image_generator.image_url[0])

insta_post_manager = InstaPostManager()

response = insta_post_manager.post_image(result, image_generator.image_url[0], os.getenv('INSTAGRAM_PAGE_ID'), os.getenv('INSTAGRAM_ACCESS_TOKEN'))
print(response)

response2 = insta_post_manager.publish_container(response['id'], os.getenv('INSTAGRAM_PAGE_ID'),os.getenv('INSTAGRAM_ACCESS_TOKEN'))
print(response2)