#streamlit run d:/Desktop/me/python_test/20231012.py


import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Interactive Widgets')

condition=st.slider('あなたの今の調子は？',0,100,50)
'コンディション：',condition

# text = st.text_input('あなたの趣味を教えてください。')
# 'あなたの趣味：',text,


# option =st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

#'あなたの好きな数字は、',option,'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('Ruby.png')
#     st.image(img,caption='Ruby',use_column_width=True)

