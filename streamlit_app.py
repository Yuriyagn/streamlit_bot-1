# -*- ecoding: utf-8 -*-
# @ModuleName: streamlit_app
# @Author: wk
# @Email: 306178200@qq.com
# @Time: 2024/1/8 14:46
# First
import openai
import streamlit as st
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    # 申明openai_key
    openai.api_key = openai_api_key
    # 将user的输入添加到session里面
    st.session_state.messages.append({"role": "user", "content": prompt})
    # 将user的输入展示到页面的对话框中
    st.chat_message("user").write(prompt)
    # 调用openai的接口，获取chatgpt的回复
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    # 将openai的回复添加到session里面
    st.session_state.messages.append(msg)
    # 将openai的回复展示到对话框里面
    st.chat_message("assistant").write(msg.content)