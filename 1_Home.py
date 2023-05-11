import streamlit as st
from PIL import Image
import allrecipes as rec
st.set_page_config(
    page_title="The Flavor Files",
    page_icon="🥘",
    layout="wide"
)




logo = Image.open('images/logo.png')
st.image(logo, width="50%", use_column_width=True)
home_tab, about_tab, recipe_tab = st.tabs(["Home", "About","Our Recipes"])
with about_tab:
    st.header("About Us")
    st.subheader("Founded in 2023")
    st.write("Welcome to The Flavor Files, where we celebrate the joy of cooking and sharing meals with loved ones. We're a team of passionate home cooks who believe that food is not just about sustenance, but also about creating meaningful connections and memories.")        
    st.write("Our website is a place where you can generate an array of delicious recipes made from the ingredients you have in your kitchen. From simple weeknight dinners to festive holiday feasts, we have something for every occasion and palate.")
    st.write('We believe that cooking should be fun, creative, and accessible to everyone, regardless of their level of experience in the kitchen.\n')
    st.write("That's why we strive to make our recipes easy to follow and adaptable to suit your preferences and dietary needs.\n")

with recipe_tab:
    st.subheader("Hey there! Here are our most popular recipes!")
    rec.getallrecipes()

with home_tab:
    image = Image.open('images/main.jpeg')
    st.image(image, use_column_width=True) 
    st.markdown("""
        <style>
            /* Set the font and font-size for all elements */
            body {
                font-family: 'Times New Roman', Georgia, Serif;
                
            }

            /* Set the font and font-size specifically for headers */
            h1, h2, h3 {
                font-family: 'Playfair Display';
                letter-spacing: 3px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.write('---\n')

    with st.container():
        col1, col2 = st.columns(2)
        image2 = Image.open('images/main2.png')
        col1.image(image2, use_column_width=True, width="100%")
        col2.header("About Us")
        col2.subheader("Founded in 2023")
        col2.write("Welcome to The Flavor Files, where we celebrate the joy of cooking and sharing meals with loved ones. We're a team of passionate home cooks who believe that food is not just about sustenance, but also about creating meaningful connections and memories.")
        col2.write("Our website is a place where you can generate an array of delicious recipes made from the ingredients you have in your kitchen. From simple weeknight dinners to festive holiday feasts, we have something for every occasion and palate.")
        col2.write('We believe that cooking should be fun, creative, and accessible to everyone, regardless of their level of experience in the kitchen.\n')
        col2.write("That's why we strive to make our recipes easy to follow and adaptable to suit your preferences and dietary needs.\n")

    st.write('---\n')
    st.header("Our Recipes")
    with st.container():
        col3, col4 = st.columns(2)
        rec.get8recipes()
    st.write('---\n')

# st.sidebar.write("---\n")
st.sidebar.caption("**DISCLAIMER**\n")
st.sidebar.caption("This website by any means is not a legitimate recipe collection.\n\
Powered by OpenAI. Use at your own discretion.")
st.sidebar.write("---\n")
html_template2 = """
<div style="display: inline-block;">
  <a href='http://localhost:8501/RecipeSearch' target='_self'>
    <button style='border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  background-color: #4CAF50;'>Take me to Recipe Search</button>
  </a>
  
</div>
"""

# home = "<a href='http://localhost:8501/' target='_self'><button style='background-color: #4CAF50; border-radius: 10px; padding: 5px; height: 50px; width: 80px;'>Home</button></a>"

st.markdown(html_template2, unsafe_allow_html=True)