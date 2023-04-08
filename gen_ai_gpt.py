# programmer: taewook kang
# date: 2023.3.30
# reference
#   https://openai.com/pricing
#   https://platform.openai.com
#   https://developers.kakao.com
import sys, os, re, argparse, readline, json, glob, shutil
from yaml import parse

import openai
OPENAI_API_KEY = "" # ADD OPENAI API KEY

def gen_ai_prompt(query):
    # create text using chatgpt
    # https://platform.openai.com/account/usage

    # prompt 1
    openai.api_key = OPENAI_API_KEY

    model = "gpt-3.5-turbo"
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
            "content": "위 내용을 바탕으로 글을 한문장으로 요약해줘."
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

    return answer3

    '''
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
            "content": "Condense up to 7 outward description to focus on nouns and adjectives separated by ,"
        }
    )

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    answer4 = response['choices'][0]['message']['content']
    print(answer4)
    return answer4
    '''

# create image using Dall-E
def create_ai_image(input, style, fname):
    import requests
    from PIL import Image
    from io import BytesIO

    input = input + ', ' + style
    response = openai.Image.create(
            prompt=input,
            n=1,
            size="512x512"
        )
    image_url = response['data'][0]['url']
    res = requests.get(image_url)
    img = Image.open(BytesIO(res.content))
    img.save(fname)

def main():
    # load argument 
    try:        
        parser = argparse.ArgumentParser()
        parser.add_argument('--query', type=str, default="달의 위를 두발로 걷고 있는 우주복 입은 치즈태비 고양이를 묘사해줘.", required=False)
        parser.add_argument('--style', type=str, default='realistic lighting, ultra-detailed, 8K, photorealism', required=False)
        parser.add_argument('--output', type=str, default='./image.png', required=False)
        args = parser.parse_args()

        query = args.query
        prompt = gen_ai_prompt(query)
        create_ai_image(prompt, args.style, args.output)
            
    except Exception as e:
        print(e)
        pass
    

if __name__ == "__main__":
    main()
