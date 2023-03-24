import openai
import os

openai.api_key = "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"

# 只需要在python里设置代理即可
os.environ["http_proxy"] = "http://127.0.0.1:33210"
os.environ["https_proxy"] = "http://127.0.0.1:33210"

# if nothing is typed, this content will be sent
messages = [
    {"role": "system", "content": "What can you do as an AI."},
]

while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    length = 0
    for msg in messages:
        length += len(msg['content'])
    while length > 4000:
        messages.pop(0)
    print("现在的字节长度为：", length)

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}\n")
    messages.append({"role": "assistant", "content": reply})