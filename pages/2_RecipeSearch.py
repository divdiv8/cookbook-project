import streamlit as st
import requests
import openai
import generate_recipe as gr
import json

api_key = "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"
openai.api_key = api_key
st.set_page_config(layout="wide")

def display_recipe():
    file = open('gptout.json', 'r')
    data = file.read()
    cdata = json.loads(data)
    #st.image('./dalle_image.jpg')
    #st.write(cdata['recipe_name'])
    st.header(cdata['Recipe_name'])
    with st.container():
        c1,c2 = st.columns(2)
        with c1:
            st.subheader("Ingredients")
            st.write(cdata['Ingredients'])

        with c2:
            st.image("./dalle_image.jpg")
            
            
            st.write("🤫 **Calories:** *"+cdata['Calories']+"*")
            st.write("🏃‍♂️ **Food Restrictions:** *"+cdata['Food_Restrictions']+"*")
            st.write("🌐 **Cuisine:** *"+cdata['Cuisine_Type']+"*")

    st.subheader('Cooking Instructions')
    st.write(cdata['Cooking_Instructions'])
    st.subheader('Origin and Cultural Significance')
    st.write(cdata['Origin'])
    n_comp = cdata['Nutrition_composition']
    st.subheader('Nutritional Composition')
    st.write(n_comp)
    st.write('\n')
    st.subheader('Nutritional Value and Medical Benefits')
    st.write(cdata['Medical'])
    st.subheader("\n Recipe Details")
    st.write("🌈 **Color:** *"+cdata['Color']+"*")
    st.write("🔆 **Temperature:** *"+cdata['Temperature']+"*")
    st.write("💭 **Smell:** *"+cdata['Smell']+"*")
    #st.write("🟠 **Texture:** *"+cdata['Texture']+"*")
    st.write("😶 **Mood:** *"+cdata['Mood']+"*")
    
    st.write("🧑‍🍳 **Heating Method:** *"+cdata['Heating_Method']+"*")
    st.write("🍞 **Dish Type:** *"+cdata['Dish_Type']+"*")
    st.write("🌟 **Meal Type:** *"+cdata['Meal_Type']+"*")

    st.write("🎈 **Heating Method:** "+"*"+cdata['Heating_Method']+"*")

html_template = """
<div style="display: inline-block;">
  <a href='http://localhost:8501/' target='_self' ;>
    <button style='border: none;
    border-radius:10px;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  background-color: #4CAF50;
  color: white;'>Home</button>
  </a>

  
</div>
"""

# home = "<a href='http://localhost:8501/' target='_self'><button style='background-color: #4CAF50; border-radius: 10px; padding: 5px; heig>

st.markdown(html_template, unsafe_allow_html=True)


#st.title("Recipe Search")
#st.markdown("<h1 style='text-align: center; color: red; font-size: 36px; font-weight: bold;font-family: monospace;'>Recipe Search</h1>", u>
title = '<h1 style="font-family:cursive; font-size: 45px;text-align: center; -wekit-text-stroke:2px black;">Recipe Search</h1>'
st.markdown(title, unsafe_allow_html=True)


# First horizontal line: search bar
input_style = """
<style>
div[class*="stTextInput"] label p {
  font-family:cursive;
  font-size: 20px;
}
div[class*="stTextInput"] input::placeholder {
  background-color: #FACA2B;
}
</style>
"""
st.write(input_style, unsafe_allow_html=True)
with st.container():
    query = st.text_input("Enter a key ingredient")



# Second horizontal line: dropdowns
st.markdown(
    """
    <style>

    div[data-baseweb="select"] > div {
    background-color: #E5A863;
    font-family:cursive;
    color: blue;
    }
    
   </style>
    """,
    unsafe_allow_html=True,
)

all_dish_type = ['','snacks', 'salads', 'soups', 'stews and curries', 'pasta', 'rice dishes', 'sandwiches and wraps', 'pizza', 'meat dishes', 'seafood dishes', 'vegetarian and vegan dishes', 'desserts']
all_cuisine = ['','Italian cuisine', 'French cuisine', 'Chinese cuisine', 'Japanese cuisine', 'Indian cuisine', 'Mexican cuisine', 'Thai cuisine', 'Spanish cuisine', 'Middle Eastern cuisine', 'Greek cuisine', 'Korean cuisine', 'Vietnamese cuisine']
all_food_restrictions = ['','vegetarian', 'gluten-free', 'lactose intolerance', 'nut allergies', 'shellfish allergies', 'Kosher', 'Halal','low-carb diets', 'low-fat diets']
all_meal_time = ['','Breakfast','Brunch', 'Lunch', 'Snack', 'Dinner', 'Supper']
all_mood = ['','Happy', 'Excited', 'Relaxed', 'Stressed', 'Bored', 'Indifferent', 'Nostalgic', 'Guilty', 'Disgusted', 'Satisfied']
all_texture = ['','crunchy', 'creamy', 'chewy', 'soft', 'grainy', 'crispy', 'smooth', 'flaky', 'juicy', 'gooey']
all_temperature = ['','Freezing (0 °C or lower)', 'Cold (0°C - 15 °C)', 'Cool (15°C - 20°C)', 'Room temperature (20°C - 25°C)', 'Warm (25°C - 40°C)', 'Hot (40°C - 60°C)', 'Boiling (100°C or higher)']
all_smell = ['','Roasted', 'Grilled', 'Baked', 'Fried', 'Spicy', 'Citrusy', 'Herbaceous', 'Fermented', 'Sweet', 'Umami']
all_color = ['','Red', 'Green', 'Yellow', 'Orange', 'Brown', 'White', 'Purple', 'Pink', 'Black', 'Blue', 'Gold', 'Silver', 'Burgundy', 'Ivory', 'Lavender', 'Turquoise', 'Magenta']
all_sound = ['','sizzle', 'crackle', 'pop', 'crunch', 'slurp', 'chew', 'gurgling', 'grind', 'whisk', 'blend']
all_heating_method = ['','Baking', 'Broiling', 'Frying', 'Grilling', 'Roasting', 'Sauteing', 'Slowing cooking', 'Steaming', 'Sous vide']
all_calories = ['','50-100 calories', '50-150 calories', '100-200 calories', '200-300 calories', '500-800 calories']

with st.container():
    col1, col2, col3 = st.columns(3)
    cuisine = col1.selectbox(":blue[Select a cuisine]  :globe_with_meridians:", all_cuisine, key=1)
    meal_time = col1.selectbox(":orange[Select a meal type]  :star2:", all_meal_time, key=2)
    #diet_label = col1.selectbox(":green[Select a diet label] :eyes:", ["", "Low-Carb", "High-Fiber", "Low-Fat", "High-Protein"], key=3)
    smell = col1.selectbox(":violet[Select the smell] :thought_balloon:", all_smell, key=10)
    
    dish_type = col1.selectbox(":blue[Select a dish type] :bread:", all_dish_type, key=4)
    food_restrictions = col2.selectbox(":orange[Select food restrictions]  :running:", all_food_restrictions, key=6)
    temperature = col2.selectbox(":green[Select the temperature] :high_brightness:", all_temperature, key=11)
    mood = col2.selectbox(":violet[Select a mood]   :no_mouth:", all_mood, key=7)
    
    texture = col2.selectbox(":blue[Select texture] :large_orange_circle:", all_texture, key=8)
    calories = col3.selectbox(":orange[Select the calories]  :shushing_face:", all_calories, key=5)
    color = col3.selectbox(":green[Select the color]  :rainbow:", all_color, key=13)
    heating_method = col3.selectbox(":violet[Select the heating method]  :balloon:", all_heating_method, key=14)


# Third horizontal line: search button
with st.container():
    if st.button("Search"):
        if not query:
            st.warning("Please enter a key ingredient.")
        else:
            gr.search_recipes(query, cuisine,dish_type,meal_time,food_restrictions,temperature,mood,texture,smell,calories,color,heating_method)
            display_recipe()




