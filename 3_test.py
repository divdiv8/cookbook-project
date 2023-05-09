import streamlit as st

html_template = """
<!DOCTYPE html>
<html>
<head>
<title>W3.CSS Template</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<style>
body {font-family: "Times New Roman", Georgia, Serif;}
h1, h2, h3, h4, h5, h6 {
  font-family: "Playfair Display";
  letter-spacing: 5px;
}

.button {
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.button1 {background-color: #4CAF50;} /* Green */
</style>
</style>
</head>
<body>

<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-padding w3-card" style="letter-spacing:4px;">
    <a href="#home" class="w3-bar-item w3-button">The Flavor Files</a>
    <!-- Right-sided navbar links. Hide them on small screens -->
    <div class="w3-right w3-hide-small">
      <a href="#about" class="w3-bar-item w3-button">About</a>
      <a href="#menu" class="w3-bar-item w3-button">Example Recipes</a>
      <a href="#contact" class="w3-bar-item w3-button">Recipe Generator</a>
    </div>
  </div>
</div>

<!-- Header -->
<header class="w3-display-container w3-content w3-wide" style="max-width:1600px;min-width:500px" id="home">
  <img class="w3-image" src="https://images.pexels.com/photos/2284166/pexels-photo-2284166.jpeg" width="1600" height="800">
  <div class="w3-display-bottomleft w3-padding-large w3-opacity">
    <h1 class="w3-xxlarge">Delicious Recipes!</h1>
  </div>
</header>

<!-- Page content -->
<div class="w3-content" style="max-width:1100px">

  <!-- About Section -->
  <div class="w3-row w3-padding-64" id="about">
    <div class="w3-col m6 w3-padding-large w3-hide-small">
     <img src="https://cdn.discordapp.com/attachments/1103765490607849562/1105190817108332575/fotor-ai-20230508135249_1.jpg" class="w3-round w3-image w3-opacity-min" alt="Table Setting" width="600" height="750">
    </div>

    <div class="w3-col m6 w3-padding-large">
      <h1 class="w3-center">About Us</h1><br>
      <h5 class="w3-center">Founded in 2023</h5>
      <p class="w3-large">Welcome to The Flavor Files, where we celebrate the joy of cooking and sharing meals with loved ones. We're a team of passionate home cooks who believe that food is not just about sustenance, but also about creating meaningful connections and memories.</p>
      <p class="w3-large">Our website is a place where you can generate an array of delicious recipes made from the ingredients you have in your kitchen. From simple weeknight dinners to festive holiday feasts, we have something for every occasion and palate.</p>
      <p class="w3-large w3-text-grey w3-hide-medium">We believe that cooking should be fun, creative, and accessible to everyone, regardless of their level of experience in the kitchen.</p>
      <p class="w3-large w3-text-grey w3-hide-medium">That's why we strive to make our recipes easy to follow and adaptable to suit your preferences and dietary needs.</p>
      <p class="w3-large w3-text-grey w3-hide-medium">We also understand that food is deeply personal and cultural, and we value diversity and inclusivity in our recipes and content which is reflected in our recipe generator.</p>

    </div>
      <center>
      <p class="w3-large">Thank you for visiting our website and joining us on this culinary journey. Let's get cooking!</p>
      </center>
  </div>
  
  <hr>
  
  <!-- Menu Section -->
  <div class="w3-row w3-padding-64" id="menu">
    <div class="w3-col l6 w3-padding-large">
      <h1 class="w3-center">Example Recipes</h1><br>
      <h4>Bread Basket</h4>
      <p class="w3-text-grey">Assortment of fresh baked fruit breads and muffins. </p><br>
    
      <h4>Honey Almond Granola with Fruits</h4>
      <p class="w3-text-grey">Natural cereal of honey toasted oats, raisins, almonds and dates. </p><br>
    
      <h4>Belgian Waffle</h4>
      <p class="w3-text-grey">Vanilla flavored batter with malted flour. </p><br>
    
      <h4>Scrambled eggs</h4>
      <p class="w3-text-grey">Scrambled eggs, roasted red pepper and garlic, with green onions.</p><br>
    
      <h4>Blueberry Pancakes</h4>
      <p class="w3-text-grey">With syrup, butter and lots of berries. </p>    
    </div>
    
    <div class="w3-col l6 w3-padding-large">
      <img src="https://cdn.discordapp.com/attachments/1103765490607849562/1105190817108332575/fotor-ai-20230508135249_1.jpg" class="w3-round w3-image w3-opacity-min" alt="Menu" style="width:100%">
    </div>
  </div>

  <hr>

  <!-- Contact Section -->
  <div class="w3-container w3-padding-64" id="contact">
    <h1>Recipe Generator</h1><br>
    <p class="w3-text-blue-grey w3-large"><b>Not sure what you're hungry for?</p>
    <p class="w3-text-blue-grey w3-medium">Our recipe generator can help you determine a delicious recipe based on the ingredients in your kitchen as well as your dietary needs.</b></p>
    <p>We offer many different ways to customize your cooking experience. Select from over 100 ingredients, different cultures, sweet or savory, textures and more. </p>
    <p><i>Or just generate something random!</i></p>

   <button class="button button1">Take me to the Recipe Generator!</button>
  </div>
  
<!-- End page content -->
</div>

<!-- Footer -->
<footer class="w3-center w3-light-grey w3-padding-32">
  <p class="w3-text-blue-grey w3-large">DISCLAIMER</p>
  <p>This website by any means is not a legitimate recipe collection.</p>
  <p><i>Powered by OpenAI. Use at your own discretion.</i></p> 
</footer>

</body>
</html>
"""

# home = "<a href='http://localhost:8501/' target='_self'><button style='background-color: #4CAF50; border-radius: 10px; padding: 5px; height: 50px; width: 80px;'>Home</button></a>"

st.markdown(html_template, unsafe_allow_html=True)
