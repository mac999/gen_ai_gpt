# title: Gen AI with GPT and Dall-E2
# programmer: taewook kang
# date: 2023.3.30
# reference
#   https://openai.com/pricing
#   https://platform.openai.com
#   https://platform.openai.com/account/usage
#
import sys, os, re, argparse, json
from yaml import parse

import openai
OPENAI_API_KEY = "" # TODO. ADD OPENAI API KEY

def gen_ai_prompt(query):
    try:
        # description in detail from query 
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
        desc = response['choices'][0]['message']['content']
        print(desc)

        # summary for AI image generation
        messages.append(
            {
                "role": "assistant",
                "content": desc
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
        summary = response['choices'][0]['message']['content']
        print(summary)

        # english translation
        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant who is good at translating."
            },
            {
                "role": "assistant",
                "content": summary
            }
        ]

        messages.append(
            {
                "role": "user", 
                "content": "영어로 번역해줘."
            }
        )

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        eng = response['choices'][0]['message']['content']
        print(eng)

        # eng = gen_image_description(model, eng)
        return eng
    except Exception as e:
        print(e)
    return ""

def gen_image_description(model, prompt):
    # image creation prompt
    messages = [
        {
            "role": "system",
            "content": "You are an assistant who is good at creating prompts for image creation."
        },
        {
            "role": "assistant",
            "content": prompt
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
    answer = response['choices'][0]['message']['content']
    print(answer)
    return answer

# create image using Dall-E
def create_ai_image(input, style, image_size, fname):
    import requests
    from PIL import Image
    from io import BytesIO

    input = input + ', ' + style
    response = openai.Image.create(
            prompt=input,
            n=1,
            size=image_size
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
        parser.add_argument('--image_size', type=str, default="512x512", required=False)
        args = parser.parse_args()

        query = args.query
        prompt = gen_ai_prompt(query)
        create_ai_image(prompt, args.style, args.image_size, args.output)
            
    except Exception as e:
        print(e)
        pass
    

if __name__ == "__main__":
    main()
