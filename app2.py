import streamlit as st
from PIL import Image

st.title("Calculator")
img = Image.open("cj.jpg")
st.sidebar.image(img)

Col1, Col2, Col3 = st.columns(3)

def add (a, b):
    c = a + b
    return c


def sub (x, y):
    z = x - y
    return z


def mult (p, d):
    f = p * d
    return f



x = st.number_input("input your first Number")
y = st.number_input("input your next Number")



with Col1:
   if st.button("Add"):
      st.write(add(x,y))
      

with Col2:
   if st.button("subtract"):
      st.write(sub(x,y))

with Col3:
   if st.button("Multiply"):
      st.wrrite(mult(x,y))
