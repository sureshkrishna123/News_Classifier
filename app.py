import streamlit as st
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from io import BytesIO
from PIL import Image
from PIL import ImageDraw
import json
import torch
import bs4



st.set_page_config(layout="wide")
#st.sidebar.image('images/Azure_Image.png', width=300)
st.sidebar.header('A website using Azure Api')
st.sidebar.markdown('Face Api,Translator Api')


app_mode = st.sidebar.radio(
    "",
    ("About Me","Input Text","Input URL" ),
)


st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.markdown('---')
st.sidebar.write('N.V.Suresh Krishna | sureshkrishnanv24@gmail.com https://github.com/sureshkrishna123')

if app_mode =='About Me':
    #st.image('images/wp4498220.jpg', use_column_width=True)
    st.markdown('''
              # About Me \n 
                Hey this is ** N.V.Suresh Krishna **. \n
                
                
                Also check me out on Social Media
                - [git-Hub](https://github.com/sureshkrishna123)
                - [LinkedIn](https://www.linkedin.com/in/suresh-krishna-nv/)
                - [Instagram](https://www.instagram.com/worldofsuresh._/)
                - [Portfolio](https://sureshkrishna123.github.io/sureshportfolio/)
                - [Blog](https://ingenious-point.blogspot.com/)\n
                If you are interested in building more about Microsoft Azure then   [click here](https://azure.microsoft.com/en-in/)\n
                ''')
               

if app_mode=='Input Text':
  #st.image(os.path.join('./images','facial-recognition-software-image.jpg'),use_column_width=True )
  st.title("News Classifier using Transformer model")
  st.header('News Classifier:')
  st.markdown("Using Transformer model I build to detect, identify and analyse the News or Article.")
  st.text("Classify the News or Article")
  
  st.text("wait for sometime to load and display the model")
    html("""<script
	    type="module"
	    src="https://gradio.s3-us-west-2.amazonaws.com/4.5.0/gradio.js"></script>
      <gradio-app src="https://sureshkrishna01-sureshkrishna01-newsclassifier.hf.space"></gradio-app>

        """,height=1000,
        )
