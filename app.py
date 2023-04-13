import os
from dotenv import load_dotenv
import openai
from ImageGenerator import ImageGenerator


load_dotenv('.env')

openai.organization = "org-yS6tGvPIqZsH0naiRkgkLFQQ"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "Você é um professor de ciência da computação da UNOESC Videira criando uma postagem de instagram para engajar pessoas"},
            {"role": "user", "content": "Como é ser um profissional de TI?"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

image_generator = ImageGenerator()

image_generator.generateImage(
    Prompt = "Um profissional da área de TI com experiência trabalhando em um datacenter",
    ImageCount = 2,
    ImageSize = '1024x1024'
)

image_generator.downloadImage(names=[
    "Image1",
    "Image2",
    ]
)