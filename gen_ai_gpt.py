# programmer: taewook kang
# date: 2023.3.30
# reference
#   https://openai.com/pricing
#   https://platform.openai.com
#   https://developers.kakao.com

import openai
from PyKakao import Karlo

# create text using chatgpt
# https://platform.openai.com/account/usage

# prompt 1
OPENAI_API_KEY = ""
openai.api_key = OPENAI_API_KEY

model = "gpt-3.5-turbo"

query = "우주복을 입고 있는 고양이가 어떤 모습일지 묘사해줘."
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant who is good at detailing."
    },
    {
        "role": "user",
        "content": query
    }
]

response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer = response['choices'][0]['message']['content']
print(answer)

# prompt 2
messages.append(
    {
        "role": "assistant",
        "content": answer
    },
)

messages.append(
    {
        "role": "user", 
        "content": "위 내용을 바탕으로 외형적인 모습을 더 자세히 상상해서 묘사해줘."
    }
)

response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer2 = response['choices'][0]['message']['content']
print(answer2)

# prompt 3
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant who is good at translating."
    },
    {
        "role": "assistant",
        "content": answer2
    }
]

messages.append(
    {
        "role": "user", 
        "content": "영어로 번역해주세요."
    }
)

response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer3 = response['choices'][0]['message']['content']
print(answer3)

# prompt 4
messages = [
    {
        "role": "system",
        "content": "You are an assistant who is good at creating prompts for image creation."
    },
    {
        "role": "assistant",
        "content": answer3
    }
]

messages.append(
    {
        "role": "user", 
        "content": "Condense up to 6 outward description to focus on nouns and adjectives separated by ,"
    }
)

response = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer4 = response['choices'][0]['message']['content']
print(answer4)

# prompt 5
params = ", realistic lighting, ultra-detailed, 8K, photorealism"
prompt = f"cat on moon surface in space, tabby cat face, {answer4}{params}"
print(prompt)

# create image using kakao
# https://developers.kakao.com/console/app/891102
KAKAO_API_KEY = "" # RESTFUL API KEY
karlo = Karlo(service_key = KAKAO_API_KEY)
img_dict = karlo.text_to_image(prompt, 1)

img_str = img_dict.get("images")[0].get('image')
img = karlo.string_to_image(base64_string = img_str, mode = 'RGBA')
img.save("./image1.png")

# create image using Dall-E
import requests
from PIL import Image
from io import BytesIO

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="512x512"
)
image_url = response['data'][0]['url']
res = requests.get(image_url)
img = Image.open(BytesIO(res.content))
img.save("./image2.png")
