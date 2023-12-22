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
PAGE_TITLE = "10장 기타 위기별·상황별 지원"
ROOT_FOLDER = "./data/DB_work/"
FOLDER_PATH = "./data/DB_work/10_기타_위기별·상황별_지원"

st.set_page_config(page_title=PAGE_TITLE, page_icon="📈", layout="wide", menu_items={
        'About': "찾아 보장 서비스"}) # 페이지 세팅 이게 먼저 나와줘야하는듯..

# set css
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
st.sidebar.markdown('### 특수한 상황이나 어려운 입장이신가요?')
st.sidebar.markdown('''
                    - 가족이 특별한 상황에 처했을 때
                    - 일을 하다가 업무상 사고를 당했을 때
                    - 재정적인 도움이 필요할 때
                    - 농어업인이거나 농어촌에 거주하고 있을 때
                    - 남을 돕다가 다치거나 사망했을 때
                    - 북한이탈주민이 지원을 필요로 할 때
                    - 기타 특수한 상황이나 입장에 처했을 때
                    - 1인 가구 지원이 필요할 때
                    - 더욱 다양한 서비스를 원할 때
                    ''')

with st.expander("찾아보장"):
    st.write("""
        '찾아보장' 서비스는 450여개의 다양한 복지제도를 상황별로 찾아볼 수 있는 서비스 입니다. 
    """)

#
# 서비스화면 관리
#
utility.make_content_card(FOLDER_PATH, PAGE_TITLE)


