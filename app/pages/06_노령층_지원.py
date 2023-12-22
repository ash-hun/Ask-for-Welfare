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
PAGE_TITLE = "06장 노령층 지원"
ROOT_FOLDER = "./data/DB_work/"
FOLDER_PATH = "./data/DB_work/06_노령층_지원"

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
st.sidebar.markdown('### 어르신들, 생활이며 건강이며 걱정이 많으시죠?')
st.sidebar.markdown('''
                    - 안정적인 노후생활 지원이 필요할 때
                    - 어르신들이 일자리를 원할 때
                    - 사회참여나 문화활동이 필요할 때
                    - 치매가 걱정될 때
                    - 어르신의 건강이 걱정될 때
                    - 어르신을 돌봐 드릴 일손이 필요할 때
                    - 어르신을 위한 각종 요금 감면 혜택이 궁금할 때
                    ''')

with st.expander("찾아보장"):
    st.write("""
        '찾아보장' 서비스는 450여개의 다양한 복지제도를 상황별로 찾아볼 수 있는 서비스 입니다. 
    """)

#
# 서비스화면 관리
#
utility.make_content_card(FOLDER_PATH, PAGE_TITLE)


