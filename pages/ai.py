import streamlit as st
from openai import OpenAI
import json
from menu import show_menu

def main():
    show_menu()
    st.session_state.client = OpenAI(api_key=st.secrets["deepseek_api_key"], base_url="https://api.deepseek.com")

    with open("history/history.json","r",encoding="utf-8") as h:
        history = json.load(h)

    for i in history:
        with st.chat_message(i["role"]):
            st.markdown(i["content"])

    user_input = st.chat_input("请输入文本")
    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
            history.append({"role":"user","content":user_input})

        response = st.session_state.client.chat.completions.create(
            model="deepseek-chat",
            messages=history,
            stream=True
            )
        with st.chat_message("assistant"):
            history.append({"role":"assistant","content":st.write_stream(response)})

        with open("history/history.json","w",encoding='utf-8') as h:
            json.dump(history,h)
if __name__ == "__main__":
    main()


