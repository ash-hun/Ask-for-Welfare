import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import unicodedata
import random
import time
import math

import utility
import re

### SET PAGE TITLE
PAGE_TITLE = "01장 생계 지원"
ROOT_FOLDER = "./data/DB_work/"
FOLDER_PATH = "./data/DB_work/01_생계_지원"

st.set_page_config(page_title=PAGE_TITLE, page_icon="📈", layout="wide", menu_items={
        'About': "찾아 보장 서비스"}) # 페이지 세팅 이게 먼저 나와줘야하는듯..

## set css
with open('./css.css', 'r', encoding='utf-8') as file:
    css = file.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
utility.add_logo()


#
# 사이드바 관리
#
st.sidebar.header(PAGE_TITLE)
# image = Image.open('img/logo.png')
# st.sidebar.image(image)
st.sidebar.markdown('### 생활에 어려움을 겪고 계신가요?')
st.sidebar.markdown('''
                    - 생계를 유지하기가 힘들 때
                    - 생활에 갑작스러운 위기가 닥쳤을 때
                    - 주택문제로 어려움을 겪을 때
                    - 재정적인 도움이 필요할 때
                    - 재정적인 도움이 필요할 때
                    - 일상의 불편함, 부족함을 해소하고 싶을 때
                    ''')

with st.expander("찾아보장"):
    st.write("""
        '찾아보장' 서비스는 450여개의 다양한 복지제도를 상황별로 찾아볼 수 있는 서비스 입니다. 
    """)

#
# 서비스화면 관리
#
utility.make_content_card(FOLDER_PATH, PAGE_TITLE)


# https://discuss.streamlit.io/t/html-and-css-not-rendering-as-expected-in-streamlit-markdown/35124/16