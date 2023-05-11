import streamlit as st
def get8recipes():
    with st.container():
        col3, col4 = st.columns(2)
        #_____________________________________________________
        #chinese orange tofu
        with col3.expander("**Chinese Orange Tofu with Chocolate Sauce and Green Bean Salad**", expanded=False):
            colx1,coly1 = st.columns(2)
            with st.container():
                coly1.image("images/image1.jpg")
                colx1.subheader("Ingredients")
                colx1.markdown("""
            - 1 orange, peeled and sliced
            - 1 sheet of rice paper
            - 1 block of firm tofu, cubed
            - 1/4 cup of dark chocolate chips
            - 1 cup of wheat flour
            - 1 cup of green beans, trimmed
            - Salt and pepper to taste
            """)
            st.subheader("Cooking Instructions")
            st.markdown("""
            - Preheat the oven to 350°F.
            - In a small saucepan, melt the chocolate chips over low heat, stirring constantly until smooth.
            - In a separate pan, simmer the tofu cubes in orange juice for 5 minutes.
            - In a bowl, mix the wheat flour with salt and pepper to taste.
            - Dip the tofu cubes in the flour mixture and fry them in a pan until golden brown.
            - Place the rice paper on a baking sheet and bake for 5 minutes until crispy.
            - In a separate pan, sauté the green beans until tender.
            - Arrange the orange slices, tofu cubes, and green beans on a plate.
            - Drizzle the chocolate sauce over the tofu cubes and serve with the crispy rice paper.
            """)
#_____________________________________________________----------------------------------------------------
# #avocado asparagus        
        with col3.expander("**Avocado and Asparagus Salad with Roasted Beets, Carrots, and Celery**", expanded=False, ):
            colx2,coly2 = st.columns(2)
            with st.container():
                coly2.image("images/image2.jpg")
                colx2.subheader("Ingredients")
                colx2.markdown("""
            - 1 avocado, sliced
            - 1 bunch of asparagus, trimmed and blanched
            - 2 beets, roasted and sliced
            - 2 carrots, roasted and sliced
            - 2 stalks of celery, sliced
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
            - In a large bowl, combine the sliced avocado, blanched asparagus, roasted beets, carrots, and celery.
            - In a small saucepan, heat up some olive oil and add some garlic and red pepper flakes. Simmer for a few minutes until fragrant.
            - Pour the garlic and red pepper oil over the salad and toss well.
            - Serve hot and enjoy!
            """)
#_____________________________________________________----------------------------------------------------
#beans and pumpkin        

        with col3.expander("**Indian Style Squash and Cauliflower Curry with Beans and Pumpkin**", expanded=False):
            colx3,coly3 = st.columns(2)
            with st.container():
                coly3.image("images/image3.jpg")
                colx3.subheader("Ingredients")
                colx3.markdown("""
            - 1 small squash, peeled and diced
            - 1 small cauliflower, cut into florets
            - 1 can of beans, drained and rinsed
            - 1 onion, chopped
            - 1 cup of pumpkin, peeled and diced
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
            - Heat oil in a large pot over medium heat. 
            - Add onions and cook until softened. 
            - Add squash, cauliflower, and pumpkin and cook for 5 minutes. 
            - Add beans and spices and stir well. 
            - Cover and simmer for 20 minutes or until the vegetables are tender. 
            - Serve hot with rice or naan bread.
            """)
#_____________________________________________________----------------------------------------------------
# japanese cold simmered salad      

        with col3.expander("**Japanese Cold Simmered Salad**", expanded=False):
            colx4,coly4 = st.columns(2)
            with st.container():
                coly4.image("images/image4.jpg")
                colx4.subheader("Ingredients")
                colx4.markdown("""
            - 1 cucumber, sliced
            - 1 leek, sliced
            - 1 potato, diced
            - 1 turnip, diced
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
            - In a pot, add the sliced cucumber, leek, diced potato, and turnip.
            - Add enough water to cover the vegetables and bring to a simmer.
            - Let the vegetables simmer for 10-15 minutes until they are tender but still firm.
            - Drain the vegetables and let them cool.
            - In a separate bowl, mix together 2 tablespoons of rice vinegar, 1 tablespoon of soy sauce, and 1 tablespoon of sesame oil.
            - Add the cooled vegetables to the bowl and toss to coat with the dressing.
            - Serve chilled.
            """)
#_____________________________________________________----------------------------------------------------
# artichoke      

        with col4.expander("**Artichoke and Mushroom Cinnamon Corn Polenta**", expanded=False):
            colx5,coly5 = st.columns(2)
            with st.container():
                coly5.image("images/image5.jpg")
                colx5.subheader("Ingredients")
                colx5.markdown("""
            - 1 can of artichoke hearts, drained and chopped
            - 1 cup of sliced mushrooms
            - 1 tsp of cinnamon
            - 1 cup of cornmeal
            - 3 cups of water
            - Salt and pepper to taste
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
            - To make this delicious Artichoke and Mushroom Cinnamon Corn Polenta, start by heating a large pot of water over medium heat.
            - Add the chopped artichoke hearts and sliced mushrooms to the pot and let them simmer for 10 minutes.
            - In a separate pot, bring 3 cups of water to a boil and add the cornmeal, cinnamon, salt, and pepper.
            - Stir the mixture until it thickens and becomes smooth. 
            - Add the artichoke and mushroom mixture to the cornmeal mixture and stir well. 
            - Let the polenta simmer for another 10 minutes until it becomes firm. 
            - Serve hot and enjoy!            """)

#_____________________________________________________----------------------------------------------------
# chinese eggplant      

        with col4.expander("**Chinese Eggplant and Shrimp Stir-Fry with Figs and Egg**", expanded=False):
            colx6,coly6 = st.columns(2)
            with st.container():
                coly6.image("images/image6.jpg")
                colx6.subheader("Ingredients")
                colx6.markdown("""
            - 1 lb lamb, sliced
            - 1 cup mixed nuts (almonds, cashews, and walnuts), chopped
            - 1 cup dairy-free cheese, grated
            - 8 oz gluten-free noodles
            - 2 cups kale, chopped
            - 1 tbsp olive oil
            - 1 tsp garlic powder
            - 1 tsp onion powder
            - Salt and pepper to taste
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
           - Heat olive oil in a large skillet over medium-high heat. 
           - Add sliced lamb and cook until browned on both sides. 
           - Add chopped nuts, garlic powder, onion powder, salt, and pepper. 
           - Stir to combine and cook for 2-3 minutes. 
           - Add chopped kale and cook until wilted. 
           - In a separate pot, cook gluten-free noodles according to package instructions. 
           - Drain and add to the skillet with the lamb and kale. Stir to combine. 
           - In a small saucepan, heat dairy-free cheese until melted. 
           - Pour over the noodle bowl and serve hot.           """)
#_____________________________________________________----------------------------------------------------
#italian lamb     

        with col4.expander("**Italian Lamb and Kale Noodle Bowl with Nutty Cheese Sauce**", expanded=False):
            colx7,coly7= st.columns(2)
            with st.container():
                coly7.image("images/image7.jpg")
                colx7.subheader("Ingredients")
                colx7.markdown("""
            - 1 large eggplant, sliced into thin rounds
            - 8 fresh figs, sliced in half
            - 1 lb. shrimp, peeled and deveined
            - 2 eggs, beaten
            - 2 tbsp. butter
            - Salt and pepper to taste
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
           - Heat a large skillet over medium-high heat. 
           - Add butter and let it melt. 
           - Add eggplant and stir-fry for 5-7 minutes until it becomes tender. 
           - Add shrimp and cook for another 3-4 minutes until it turns pink. 
           - Add figs and stir-fry for 1-2 minutes. Pour in beaten eggs and stir-fry until the eggs are cooked. 
           - Season with salt and pepper to taste. Serve hot with rice or noodles.
           """)
#_____________________________________________________----------------------------------------------------
# lemon fried fish      

        with col4.expander("**Lemon Fried Fish with Bell Peppers and Tomato Salad**", expanded=False):
            colx8,coly8 = st.columns(2)
            with st.container():
                coly8.image("images/image8.jpg")
                colx8.subheader("Ingredients")
                colx8.markdown("""
            - 4 fish fillets
            - 2 bell peppers, sliced
            - 1 lemon, sliced
            - 1/4 cup olives, sliced
            - 2 tomatoes, diced
            """)
            st.write()
            st.subheader("Cooking Instructions")
            st.markdown("""
           - Heat a large skillet over medium-high heat. 
           - Add enough oil to coat the bottom of the pan. 
           - Season the fish fillets with salt and pepper and place them in the skillet. 
           - Cook for 3-4 minutes on each side until golden brown and crispy. 
           - Remove the fish from the skillet and set aside. 
           - In the same skillet, add the sliced bell peppers and cook for 2-3 minutes until slightly softened. 
           - Add the lemon slices and olives and cook for another minute. 
           - In a separate bowl, mix the diced tomatoes with salt, pepper, and a drizzle of olive oil. 
           - Serve the fish with the bell pepper and lemon mixture and the tomato salad on the side.           """)

def getallrecipes():
    
    get8recipes()