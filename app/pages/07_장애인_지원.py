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
PAGE_TITLE = "07장 장애인 지원"
ROOT_FOLDER = "./data/DB_work/"
FOLDER_PATH = "./data/DB_work/07_장애인_지원"

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
st.sidebar.markdown('### 장애인을 위한 복지서비스, 어떤 것이 있을까요?')
st.sidebar.markdown('''
                    - 장애로 인해 생활이 곤란할 때
                    - 자녀 양육에 곤란을 겪을 때
                    - 교육의 기회를 원할 때
                    - 일자리가 필요할 때
                    - 사회활동과 자립을 원할 때
                    - 의료 및 재활지원이 필요할 때
                    - 안정적인 일상생활을 원할 때
                    - 장애인을 위한 세제혜택을 받고 싶을 때
                    - 지역사회 복지시설을 이용하고 싶을 때
                    - 각종 요금을 감면받고 싶을 때
                    ''')

with st.expander("찾아보장"):
    st.write("""
        '찾아보장' 서비스는 450여개의 다양한 복지제도를 상황별로 찾아볼 수 있는 서비스 입니다. 
    """)

#
# 서비스화면 관리
#
utility.make_content_card(FOLDER_PATH, PAGE_TITLE)


