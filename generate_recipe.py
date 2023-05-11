import openai
import json
import requests
import re

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def search_recipes(query, cuisine, dish_type, meal_time, food_restrictions, temperature, mood, texture, smell, calories, color, heating_method):
    prompt_1 = f"""

Perform the following actions and output the result after all the actions are performed: 

1 - Generate a recipe that incorporates the following factors: \
ingredients - {query}, dish type - {dish_type}, cuisine type - {cuisine}, \
food-restrictions - {food_restrictions}, meal-type - {meal_time}, mood - {mood}, \
texture of the food - {texture}, smell - {smell}, color - {color}, \
 temperature - {temperature},  \
heating method - {heating_method}, and calories - {calories}. 

2 - check if the recipe is edible and safe and assure the reader about its safety with a heading 

3 - make the recipe compelling with cooking instructions like the blog of a famous food blogger \
which targets an advanced food connoisseur to push the boundaries of culinary savoir-faire.

4 - add a paragraph about the place of origin of the dish and \
 make sure the recipe focusses more on the usage of {query} and
 translate them in the local language of place of origin and \
 explain their cultural significance and any obscure facts about them 

5 - create a table showing the macronutrient and micronutrient composition \
of the recipe based on the ingredients and their quantities used.

6 - add a paragraph on the nurtitional value and medical benefits this recipe \
provides by the research studies in the style of health information site like "Healthline"

7 - at the end, add three comments from blog users with realistic names \
on the above recipe with positive, negative, and mixed sentiments 

8 - make sure to use  heading names exactly as listed: Recipe Name, Ingredients, Dish Type, Cuisine Type,
Food Restrictions, Meal Type, Mood, Texture, Smell, Color, Temperature, Heating Method,
Calories, Instructions, Safety Assurance, Origin and Cultural Significance, Nutrical Composition,
Nutritional Value and Medical Benefits. 

"""
    # get the response- recipe
    response = get_completion(prompt_1)
    text = response
    
    ingredients_pattern = r"Ingredients:\s+([\s\S]*?)\n\n"
    Dish_Type_pattern = r"Dish Type:\s+(.*?)\n"
    Cuisine_Type_pattern = r"Cuisine Type:\s+(.*?)\n"
    Food_Restrictions_pattern = r"Food Restrictions:\s+(.*?)\n"
    Meal_Type_pattern = r"Meal Type:\s+(.*?)\n"
    Mood_pattern = r"Mood:\s+(.*?)\n"
    Texture__pattern = r"Texture\s+(.*?)\n"
    Smell_pattern = r"Smell:\s+(.*?)\n"
    Color_pattern = r"Color:\s+(.*?)\n"
    Temperature_pattern = r"Temperature:\s+(.*?)\n"
    Heating_Method_pattern = r"Heating Method:\s+(.*?)\n"
    Calories_pattern = r"Calories:\s+(.*?)\n"
    recipe_pattern = r"Recipe:\s+([\s\S]*?)\n\n"
    recipe_pattern = r"Recipe Name:\s+([\s\S]*?)\n\n"
    Cooking_Instructions_pattern = r"Instructions:\s+([\s\S]*?)\n\n"
    Safety_pattern = r"Safety Assurance:\s+([\s\S]*?)\n\n"
    origin_pattern = r"Origin and Cultural Significance:\s+([\s\S]*?)\n\n"
    nutrition_composition_pattern = r"Nutritional Composition:\s+([\s\S]*?)\n\n"
    medical_pattern = r"Nutritional Value and Medical Benefits:\s+([\s\S]*?)\n\n"

    # Extract data using regular expressions
    try:
        Dish_Type = re.search(Dish_Type_pattern, text).group(1)
    except: 
        Dish_Type = None
    try:
        Cuisine_Type = re.search(Cuisine_Type_pattern, text).group(1)
    except: 
        Cuisine_Type = None
    try:
        Food_Restrictions = re.search(Food_Restrictions_pattern, text).group(1)
    except: 
        Food_Restrictions = None
    try:
        Meal_Type = re.search(Meal_Type_pattern, text).group(1)
    except: 
        Meal_Type = None
    try:
        Mood = re.search(Mood_pattern, text).group(1)
    except: 
        Mood = None 
    try:
        Texture = re.search(Texture__pattern, text).group(1)
    except: 
        Texture = None
    try:
        Smell = re.search(Smell_pattern, text).group(1)
    except: 
        Smell = None
    try:
        Color = re.search(Color_pattern, text).group(1)
    except: 
        Color = None
    try:
        Temperature = re.search(Temperature_pattern, text).group(1)
    except:
        Temperature = None
    try:
        Heating_Method = re.search(Heating_Method_pattern, text).group(1)
    except:
        Heating_Method = None
    try:
        Calories = re.search(Calories_pattern, text).group(1)
    except:
        Calories = None
    try:
        ingredients = re.findall(ingredients_pattern, text)[0]
    except:
        ingredients = None
    try:
        recipe_name = re.findall(recipe_pattern, text)[0]
    except:
        recipe_name = None
    try:
        Cooking_Instructions = re.findall(Cooking_Instructions_pattern, text)[0]
    except: 
        Cooking_Instructions = None 
    try:
        Safety = re.findall(Safety_pattern, text)[0]
    except: 
        Safety = None 
    try:
        origin = re.findall(origin_pattern, text)[0]
    except:
        origin = None 
    try:
        nutrition_composition = re.findall(nutrition_composition_pattern, text)[0]
    except: 
        nutrition_composition = None 
    try:
        medical = re.findall(medical_pattern, text)[0]
    except: 
        medical = None 

    # Create a JSON object with extracted data
    data = {
        "Recipe_name": recipe_name,
        "Dish_Type": Dish_Type,
        "Cuisine_Type": Cuisine_Type,
        "Food_Restrictions": Food_Restrictions,
        "Meal_Type": Meal_Type,
        "Mood": Mood,
        "Texture": Texture,
        "Smell": Smell,
        "Color":Color,
        "Temperature": Temperature,
        "Heating_Method":Heating_Method,
        "Calories":Calories,
        "Ingredients": ingredients,
        "Cooking_Instructions": Cooking_Instructions,
        "Safety": Safety,
        "Origin": origin,
        "Nutrition_composition": nutrition_composition,
        "Medical": medical

    }

    # Convert the data to a JSON string and print it
    json_data = json.dumps(data)
    print(json_data)

    with open("gptout.json", "w") as f:
        f.write(json_data) 
    file = open('gptout.json', 'r')
    data = file.read()
    cdata = json.loads(data)
    file.close()
    idea = (cdata['Recipe_name'])
    # get the image

        
    bsize = "512x512"

    response2 = openai.Image.create(prompt=idea, n=1, size=bsize)
    image_url = response2['data'][0]['url']

    # save the image
    image_name = "dalle_image.jpg"
    data = requests.get(image_url).content
    f = open(image_name, 'wb')
    f.write(data)
    f.close()