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
            {"role": "system", "content": "Você é um líder técnico de um projeto de software e está recrutando pessoas e deve fazer um post de instagram para dar publicidade a vaga"},
            {"role": "user", "content": "Uma nova vaga para Engenheiro de DevOps está aberta"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)

image_generator = ImageGenerator()

image_generator.generateImage(
    Prompt = "Um programador de computadores em frente ao seu laptop, incluia a logomarca do Docker e Kubernetes no canto inferior da imagem",
    ImageCount = 2,
    ImageSize = '1024x1024'
)

image_generator.downloadImage(names=[
    "Image1",
    "Image2",
    ]
)