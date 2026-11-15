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
# st.logo("Resources/logo.png")

# 初始化聊天信息
if "message" not in st.session_state:
    st.session_state.message = []

# 昵称
if "nike_name" not in st.session_state:
    st.session_state.nike_name = "笨蛋"

# 性格
if "narures" not in st.session_state:
    st.session_state.natures = "可爱"

# 展示聊天信息
for message in st.session_state.message:
    st.chat_message(message["role"]).write(message["content"])

# 系统提示词
system_prompt = "你叫%s，你的性格是%s，你需要严格按照用户问题来回答"

# 左侧侧边栏 --> streamlit里面的上下文管理器
with st.sidebar:
    st.subheader("信息")

    # 昵称输入框
    nike_name = st.text_input("昵称", placeholder="请输入昵称吧~~", value=st.session_state.nike_name)
    if nike_name:
        st.session_state.nike_name = nike_name

    # 性格输入框
    nature = st.text_area("性格", placeholder="请输入性格吧~~", value=st.session_state.natures)
    if nature:
        st.session_state.natures = nature

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
            {"role": "system", "content": system_prompt % (st.session_state.nike_name, st.session_state.natures)},
            *st.session_state.message,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )

    # 输出大模型返回的结果（非流式输出）
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # print("---------大模型回答：", response.choices[0].message.content)

    # 输出大模型返回的结果（流式输出）
    response_message = st.empty()   # 创建一个空的组件，用来展示AI大模型返回的结果

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    st.session_state.message.append({"role": "assistant", "content": full_response})