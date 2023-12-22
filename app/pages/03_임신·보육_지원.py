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
PAGE_TITLE = "03장 임신·보육 지원"
ROOT_FOLDER = "./data/DB_work/"
FOLDER_PATH = "./data/DB_work/03_임신·보육_지원"

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
st.sidebar.markdown('### 아이를 낳는 것도 키우는 것도 걱정이시죠?')
st.sidebar.markdown('''
                    - 임신·출산이 경제적으로 부담될 때
                    - 육아와 직장생활을 병행하고 싶을 때
                    - 아이 보육에 도움이 필요할 때
                    - 어린 자녀의 건강관리가 필요할 때
                    - 방과 후 돌봐줄 손길이 필요할 때
                    ''')

with st.expander("찾아보장"):
    st.write("""
        '찾아보장' 서비스는 450여개의 다양한 복지제도를 상황별로 찾아볼 수 있는 서비스 입니다. 
    """)

#
# 서비스화면 관리
#
utility.make_content_card(FOLDER_PATH, PAGE_TITLE)


