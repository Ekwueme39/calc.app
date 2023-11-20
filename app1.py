import streamlit as st
from PIL import Image
st.title("Welcome To My First App")
img = Image.open("cj.jpg")
st.sidebar.image(img)
st.subheader("This app does absolutely well")
col1, col2 = st.columns(2)

with col1: 
    st.number_input("How old are you", step = 1)
    st.selectbox("Title",["Mr", "Mrs", "Miss"])
    st.selectbox("Gender",["Male", "female"],)                     
    st.text_input("Name")

with col2: 
    st.text_area("Address")
    st.selectbox("Gender", ["Female","Male","Others","Prefer not to say"])
    st.sidebar.radio("Gender", ["female","Male","Others","Prefer not to say"])
    st.sidebar.checkbox("Agree")
    st.balloons()
    st.button("calculate")
    st.spinner("In progress")





