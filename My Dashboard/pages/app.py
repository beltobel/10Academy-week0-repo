import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import requests
from streamlit_lottie import st_lottie
from PIL import Image

local_css("style/style.css")

img_contact_form = Image.open("images/data_science.jpg")
img_lottie_animation = Image.open("images/eda.jpg")

# ---- PROJECTS ----
with st.container():
    st.write("")
    st.header("My Projects")
    st.header("task-1")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("EDA analysis ")
        st.write(
            """
            Anonymized Slack messages of Batch 6 from the 10 Academy training program. 
            The dataset is organised into folders, each representing a Slack channel, and
           contains JSON files for individual days.
           
           
           """
            
        )
        
        
        st.markdown("[Details...](https://youtu.be/TXSOitGoINE)")
        
        
with st.container():
    st.header("task-2")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Data Science Component Building")
        st.write(
            """
           
            """
        )
        st.markdown("[Details...](https://youtu.be/FOULV9Xij_8)")

        
        
with st.container():
    st.header("task-3")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("MongoDb and PostgreSQL")
        st.write(
            """
           
            """
        )
        st.markdown("[Details...](https://youtu.be/FOULV9Xij_8)")

        
with st.container():
    st.header("task-4")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Dashboards")
        st.write(
            """
           
            """
        )
        st.markdown("[Details...](https://youtu.be/FOULV9Xij_8)")

        
              
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/beletebogale2@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        
        st.empty()

with st.container():
    st.write("---")
    st.header("copy")