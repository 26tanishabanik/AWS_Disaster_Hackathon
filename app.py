import streamlit as st
import numpy as np
from PIL import Image, ImageOps
import base64

st.sidebar.markdown('<h1 style="margin-left:8%; color:	#FF9933 ">Menu </h1>',
                    unsafe_allow_html=True)
option = st.sidebar.radio(" ",('Home','About Project'))

if option == 'Home':
      
      col1,col2,col3 = st.columns([50,100,1])
    
      
      st.markdown(
          """
          <style>
          .container1 {
          display: flex;
        }
        .logo-img1 {
             float:right;
             width:350px;
             height:350px;
             margin: 0px 0px 0px 170px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(
          """
          <style>
          .container2 {
          display: flex;
        }
        .img {
             float:right;
             width:300px;
             height:350px;
             margin: 0px 0px 0px 200px;
        }
        </style>
        """,
        unsafe_allow_html=True
      )
      st.markdown(
          f"""
          <div class="container1">
               <img class="logo-img1" src="data:image/jpg;base64,{base64.b64encode(open('urban-heat-island.jpg', "rb").read()).decode()}">
          </div>
          """,
          unsafe_allow_html=True
      )
      st.text("")
      st.text("")
      st.text("")
      html_temp = """
        <div style="background-color:blue;padding:10px">
        <h2 style="color:white;text-align:center;">Urban Heat Island</h2>
        </div>
        """
      st.markdown(html_temp,unsafe_allow_html=True)
      st.text("")
      st.text("")
      st.text("")

      def upload_image_ui():
          uploaded_image = st.file_uploader("Please upload a image", type=["png", "jpg", "jpeg"])
          if uploaded_image is not None:
            try:
                image = Image.open(uploaded_image)
                image = ImageOps.grayscale(image)
            except:
                st.error("Error: Invalid image")
