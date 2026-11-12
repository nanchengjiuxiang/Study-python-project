import streamlit as st

# 设置标题
st.title("一级标题")
st.header("二级标题")
st.subheader("标题")

# 段落展示
st.write("段落就是 HTML 里的元素，在 streamlit 里使用 st.write('内容') 的方式去书写。")

# 图片展示
st.image("Resources/image.jpg")

# 表格展示
date = {"姓名": ["张三", "李四", "王五"],
        "学号": ["001", "002", "003"],}
st.table(date)

# 分割线
st.divider()

# 普通输入框
name = st.text_input("姓名:")
if name:
    st.write(f"你的姓名为{name}")

# 密码输入框
password = st.text_input("密码", type="password")
if password:
    st.write(f"你的密码为{password}")

# 数字输入框
age = st.number_input("年龄:")
if age:
    st.write(f"你的年龄为{age}")

# 多行文本输入框
st.text_area("输入多行内容:")

# 复选框
checked = st.checkbox("同意以上条款")
if checked:
    st.write("同意")
else:
    st.write("不同意")

# 单选框
is_right = st.radio("密码正确吗？", ["正确", "错误"], index=1)
if is_right:
    st.write(f"密码是{is_right}的")

# 单选下拉框
subject = st.selectbox(
    "意向学科",
    [
        "AI大模型开发",
        "AI智能应用开发",
        "AI运维",
        "AI嵌入式+机器人开发",
        "AI测试"
    ]
)