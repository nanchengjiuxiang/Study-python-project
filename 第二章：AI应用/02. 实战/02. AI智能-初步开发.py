import streamlit as st
import os
from openai import OpenAI

# 设置页面配置项
st.set_page_config(
    page_title="AI智障",
    page_icon="Resources/icon.png",
    # 布局
    layout="wide",
    initial_sidebar_state="expanded",
)

# 大标题
st.title("啥也不会的AI")

# 设置logo
st.logo("Resources/logo.png")

# 初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message = []

# 展示聊天信息
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])

# 系统提示词
system_prompt = "你是一位十分可爱的AI助理，你需要用可爱的语气的回答用户问题"

# 聊天输入框 ---> 用户提示词
prompt = st.chat_input("与笨蛋对话~")

if prompt:   # 字符串会自动转化为布尔值
    st.chat_message("user").write(prompt)
    print("---------调用AI大模型，提示词：", prompt)
    # 保存用户提示词
    st.session_state.message.append({"role": "user", "content": prompt})

    # 创建与AI大模型对话的客户端
    client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

    # 与AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )

    st.chat_message("assistant").write(response.choices[0].message.content)
    print("---------大模型回答：", response.choices[0].message.content)
    st.session_state.message.append({"role": "assistant", "content": response.choices[0].message.content})