# Generative AI with ChatGPT
Gen AI with ChatGPT</br>
Gen AI with ChatGPT is how how to generate AI from description by using ChatGPT and Dall-E2.</br>
You can generate movie, image by using ChatGPT, Stable Diffusion like Dall-E2 easily.</br>

# prepare
1. run commands like below in terminal.</br>
git clone https://github.com/mac999/gen_ai_gpt</br>
cd gen_ai_gpt</br>
pip install -r requirements.txt</br>
2. create API key from [OpenAI platform website](https://platform.openai.com/account/api-keys)</br>
3. open gen_ai_gpt.py and assign the API key to OPENAI_API_KEY at TODO source code line by using editor.</br>
```
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
...
```

# run
python gen_ai_gpt.py --query="달의 위를 두발로 걷고 있는 우주복 입은 치즈태비 고양이를 묘사해줘." --style="realistic lighting, ultra-detailed, 8K, photorealism" --output="./image.png"</br>
</br>
result</br>
prompt=cat on moon surface in space, tabby cat face, [your input]</br>
<img width="200px" src="https://github.com/mac999/gen_ai_gpt/blob/main/image2.png"/>
<img width="200px" src="https://github.com/mac999/gen_ai_gpt/blob/main/image1.png"/>
<img width="200px" src="https://github.com/mac999/gen_ai_gpt/blob/main/image.png"/>
<img width="200px" src="https://github.com/mac999/gen_ai_gpt/blob/main/image3.png"/></br>
<img width="800px" src="https://github.com/mac999/gen_ai_gpt/blob/main/prompt.png"/>
