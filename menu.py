import streamlit as st

def show_menu():
	with st.sidebar:
		st.title("导航菜单")
		st.page_link("app.py",label="首页")
		st.page_link("pages/read.py",label="查阅")
		st.page_link("pages/edit.py",label="编辑")
		st.page_link("pages/ai.py",label="AI助手")