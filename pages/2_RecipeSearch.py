import streamlit as st
import requests
import openai
import generate_recipe as gr
import json
import random

no_of_colors=5
color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(no_of_colors)]
print(color)


api_key = "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"
openai.api_key = api_key
st.set_page_config(layout="wide")

def display_recipe():
    file = open('gptout.json', 'r')
    data = file.read()
    cdata = json.loads(data)
    #st.image('./dalle_image.jpg')
    #st.write(cdata['recipe_name'])
    name = cdata['recipe_name']
    st.header(":blue["+name+"]")
    with st.container():
        c1,c2 = st.columns(2)
        with c1:
            st.subheader("Ingredients")
            for i in range(0,len(cdata['ingredients'])):
                st.write("🌟 "+ cdata['ingredients'][i])
        
        with c2:
            st.image("./dalle_image.jpg")
    st.subheader('Cooking Instructions')
    for i in range(0,len(cdata['cooking_instructions'])):
        st.write("🌟 "+ cdata['cooking_instructions'][i])
    st.subheader('Origin and Cultural Significance')
    st.write(cdata['origin'])
    n_comp = cdata['nutrition_comp']
    st.subheader('Nutritional Composition')
    st.table(n_comp)
    st.subheader('Nutritional Value and Medical Benefits')
    st.write(cdata['n_values'])


html_template = """
<div style="display: inline-block;">
  <a href='http://localhost:8501/' target='_self'>
    <button style='background-color: #C04000; border-radius: 10px; padding: 5px; height: 45px; width: 80px; margin-right: 10px'>Home</button>
  </a>

  
</div>
"""

# home = "<a href='http://localhost:8501/' target='_self'><button style='background-color: #4CAF50; border-radius: 10px; padding: 5px; height: 50px; width: 80px;'>Home</button></a>"

st.markdown(html_template, unsafe_allow_html=True)


st.title("Recipe Search")


# First horizontal line: search bar
with st.container():
    query = st.text_input("Enter a key ingredient")

# Second horizontal line: dropdowns
with st.container():
    col1, col2, col3 = st.columns(3)
    cuisine = col1.selectbox("Select a cuisine", ["", "American", "Italian", "Indian", "Chinese"], key=1)
    meal_time = col1.selectbox("Select a meal type", ["", "Breakfast", "Lunch", "Dinner", "Snack"], key=2)
    diet_label = col1.selectbox("Select a diet label", ["", "Low-Carb", "High-Fiber", "Low-Fat", "High-Protein"], key=3)
    smell = col1.selectbox("Select the smell", ["", "aromatic", "Acrid"], key=10)
    dish_type = col2.selectbox("Select a dish type", ["", "Bread", "Cakes", "Cookies", "Desserts"], key=4)

    
    food_restrictions = col2.selectbox("Select food restrictions", ["","gluten-free", "dairy-free","none"], key=6)
    temperature = col2.selectbox("Select the temperature", ["", "hot", "cold"], key=11)
    mood = col2.selectbox("Select a mood", ["","sad", "pleasant"], key=7)
    texture = col3.selectbox("Select texture", ["", "soft", "crunchy"], key=8)
    calories = col3.selectbox("Select the calories", ["", "less than 1000 calories", "less than 2000 calories"], key=12)
    color = col3.selectbox("Select the color", ["", "green", "yellow","red","pink","blue"], key=13)
    heating_method = col3.selectbox("Select the heating method", ["", "simmer", "high-flame"], key=14)


# Third horizontal line: search button
with st.container():
    if st.button("Search"):
        if not query:
            st.warning("Please enter a key ingredient.")
        else:
            gr.search_recipes(query, cuisine,diet_label,dish_type,meal_time,food_restrictions,temperature,mood,texture,smell,calories,color,heating_method)
            display_recipe()

