import streamlit as st
from menu import show_menu
import json
import os

def select_book():
	"""选择一个笔记本"""
	with open("books/books.json","r",encoding="utf-8") as bj:
		st.session_state.bj = json.load(bj)

	books = []
	for i in st.session_state.bj:
		books.append(i["book"])

	st.session_state.book = st.selectbox("请选择笔记本",books)

def select_page():
	"""选择一页"""
	pages = []
	for i in st.session_state.bj:
		if i["book"] == st.session_state.book:
			try:
				pages = i["pages"]
			except:
				pages = None

	#为了避免出现无法打开一个新建笔记本的情况
	if pages:
	#用一个字典建立文件名和标题的关系
		headers = {}
		for i in pages:
			with open(f"books/pages/{i}","r",encoding="utf-8") as p:
				header = p.readline().strip().lstrip("## ")
				headers[i] = header

		#选择一个标题
		header_selected = st.selectbox("请选择文章",headers.values())

		for page,header in headers.items():
			if header_selected == header:
				st.session_state.page = page
def main():
	show_menu()

	with st.sidebar:
		#初始化变量
		
		if "book" not in st.session_state:
			st.session_state.book = None

		st.session_state.page = None

		select_book()
		#读取里面的文章
		if st.session_state.book:
			select_page()

	if st.session_state.page:
		st.header(f"您目前正在查阅的是{st.session_state.book}")
		with open(f"books/pages/{st.session_state.page}","r",encoding="utf-8") as p:
			st.write(p.read())
	else:
		st.header("这是我的电子笔记本")

if __name__ == "__main__":
	main()