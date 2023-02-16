from decouple import config

import openai

openai.api_key = config("secret")

response = openai.Image.create(
  prompt="Un conejo con una escopeta",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)