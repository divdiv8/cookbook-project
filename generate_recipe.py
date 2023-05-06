import openai
import json
import requests

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def search_recipes(query, cuisine, diet_label, dish_type, meal_time, food_restrictions, temperature, mood, texture, smell, calories, color, heating_method):
    prompt_1 = f"""

Perform the following actions and output the result after all the actions are performed: 

1 - Generate a recipe that incorporates the following factors: \
ingredients - {query}, dish type - {dish_type}, cuisine type - {cuisine}, \
food-restrictions - {food_restrictions}, meal-time - {meal_time}, mood - {mood}, \
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

"""
# get the response- recipe
    response = get_completion(prompt_1)

    print(response)
# create a json file
    prompt_3 = f"""
        Output a text in json format containing the following keys: recipe_name, ingredients, \
        safety_assurance, cooking_instructions, origin, nutrition_comp, n_values, user_com\
        and Use the following instructions for creating json keys and values: \
        recipe_name: <name of the recipe >\
        ingredients: <ingredients of the recipe  >\
        safety_assurance: < safety assurance of the recipe   > \
        cooking_instructions: < cooking instructions of the recipe  > \
        origin: < origin and cultural significance of the recipe  > \
        nutrition_comp: < Nutritional Composition of the recipe   > \
        n_values: < Nutritional Value and Medical Benefits of the recipe   > \
        in {response}
        and format them as list of items separated by commas \
        Text: '''{response}'''\
        """
    response_3 = get_completion(prompt_3)
    with open("gptout.json", "w") as f:
        f.write(response_3) 
    file = open('gptout.json', 'r')
    data = file.read()
    cdata = json.loads(data)
    file.close()
    idea = (cdata['recipe_name'])
# get the image

    
    bsize = "256x256"

    response2 = openai.Image.create(prompt=idea, n=1, size=bsize)
    image_url = response2['data'][0]['url']

# save the image
    image_name = "dalle_image.jpg"
    data = requests.get(image_url).content
    f = open(image_name, 'wb')
    f.write(data)
    f.close()
