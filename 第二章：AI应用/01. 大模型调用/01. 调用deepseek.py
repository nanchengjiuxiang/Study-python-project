import os
from openai import OpenAI

# 创建与AI大模型对话的客户端
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 与AI大模型进行交互
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个很厉害的AI助理，你要以正常的口吻回答用户的问题"},
        {"role": "user", "content": "你是谁？"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

print(response.choices[0].message.content)