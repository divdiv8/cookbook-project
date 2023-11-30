import streamlit as st
from PIL import Image
import allrecipes as rec

st.set_page_config(
    page_title="Neural Recipe Box",
    page_icon="🤖",
    layout="wide"
)

logo = Image.open('images/logo.png')
st.image(logo, width="50%", use_column_width=True)
home_tab, about_tab, recipe_tab = st.tabs(["Home", "About", "Our Recipes"])
with about_tab:
    st.header("About Us")
    st.subheader("Founded in 2023")
    st.write(
        "Welcome to Neural Recipe Box, where we bring the power of artificial intelligence to your kitchen! Our "
        "mission is to revolutionize the way people cook by providing cutting-edge, AI-generated recipes that are "
        "easy to follow and always delicious.")

    st.write(
        "Gone are the days of searching through countless recipe books or websites, only to be disappointed by "
        "lackluster results. With Neural Recipe Box, you can access a vast library of recipes that have been created "
        "and tested by our advanced AI algorithms. Whether you're a seasoned home cook or a novice in the kitchen, "
        "our recipes are designed to be easy to follow and produce consistently great results.")

    st.write(
        "At Neural Recipe Box, we believe that everyone should have access to great food. That's why our recipes are free to access and use. We're also committed to making our platform inclusive and accessible to all, regardless of skill level or dietary needs.")

    st.write(
        "Our team is comprised of passionate foodies, tech enthusiasts, and AI experts who are dedicated to pushing the boundaries of what's possible in the world of cooking. We're always experimenting with new ingredients, techniques, and flavor combinations to bring you the most innovative and exciting recipes.")

    st.write(
        "Thank you for choosing Neural Recipe Box as your go-to source for delicious, AI-generated recipes. We can't wait to see what you'll create in your kitchen!")
    # write("That's why we strive to make our recipes easy to follow and adaptable to suit your preferences and dietary needs.\n")

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
        with col2:
            st.write(
                "Welcome to Neural Recipe Box, where we bring the power of artificial intelligence to your kitchen! "
                "Our mission is to revolutionize the way people cook by providing cutting-edge, AI-generated recipes "
                "that are easy to follow and always delicious.")

            st.write(
                "Gone are the days of searching through countless recipe books or websites, only to be disappointed "
                "by lackluster results. With Neural Recipe Box, you can access a vast library of recipes that have "
                "been created and tested by our advanced AI algorithms. Whether you're a seasoned home cook or a "
                "novice in the kitchen, our recipes are designed to be easy to follow and produce consistently great "
                "results.")

            st.write(
                "At Neural Recipe Box, we believe that everyone should have access to great food. That's why our recipes are free to access and use. We're also committed to making our platform inclusive and accessible to all, regardless of skill level or dietary needs.")

            st.write(
                "Our team is comprised of passionate foodies, tech enthusiasts, and AI experts who are dedicated to pushing the boundaries of what's possible in the world of cooking. We're always experimenting with new ingredients, techniques, and flavor combinations to bring you the most innovative and exciting recipes.")

            st.write(
                "Thank you for choosing Neural Recipe Box as your go-to source for delicious, AI-generated recipes. We can't wait to see what you'll create in your kitchen!")

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
