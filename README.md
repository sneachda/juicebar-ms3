# **JuiceBar** ***Practical Python and Data-Centric Development - Code Institute - Third Milestone Project***    
    
 [LiveWebsite: JuiceBar](https://juicebar-cookbook.herokuapp.com/)  
   
[JuiceBar Github repository](https://github.com/sneachda/juicebar-ms3)   
  
[Wireframes]()  
  
  
    
The main purpose of this project is to build a responsive website that allows user to create, read, update and delete (*CRUD*) recipes. **JuiceBar** is a MongoDB based Flask project    
    
The user from the start will have access to all recipes stored in database. If the user wish to manipulate data - they would have to register.    
    
It's a great way to create and store some of your favourite recipes.      
    
Give it a go [here](https://juicebar-cookbook.herokuapp.com/)  
  
  
  
>##  UX  
  
  
***User Stories***  
  
****As a user, I want/expect:****  
  
- to view all the recipes without having to register  
  
- to create my own account  
  
- to add new recipes  
  
- to edit my recipes  
  
- to delete my recipes  
  
- to log out any time and have the session terminated  
  
- to use the website from any device (laptop, tablet, mobile)  
  
  
***Design***  
Main goal, following the industry standards, was to make website easily accessible, include all information required while keeping minimalistic design.   
Decision was made to use [Bootstrap](https://getbootstrap.com) to create simple, responsive project. Features like navbar forms, card as well as responsive display were built using it.   
  
*Color Scheme*  
One of the main goals was to focus user's attention on the recipe cards and recipes' images. Therefore, I decided to have clean white pages with popping color from images which comes with recipes.   
  
  
>## Features  
  
*Navbar*  
  
The navbar is fixed on top of the page. Logo is located on the left hand side, which redirects user to home page when clicked.  On the smaller devices the navbar is collapsed into a burger icon.    
For **non-logged in** users or **guests** navbar contains the following links: Browse, Register and Login.   
For **logged-in** users navbar contains the following links: Browse and My Account which opens up allowing user to view their Recipes, Add Recipes and Log out.   
  
*Home Page and Recipes Pages*  
  
All people visiting website will be able to view all recipes.   
  
Home Page has a very simple role to play - it invites users to create their own account. It also allows them to browse all recipes that have been already created.   
Once they create account, paragraph previously containing link to register page has three buttons allowing them to browse recipes with ease.   
  
Depending on browsing option chosen, people visiting the page can browse all recipes at once, or pick by category: juices or smoothies. They all display recipe cards, which contain short description of the recipe with few additional details. All recipe cards are clickable and redirect user to the individual recipe page with detailed information.   
  
*Register/Login*  
  
The register page allows a user to create a new account. Two fields are displayed: username and password which need to be filled in. When adding a username, the code compares it against existing usernames to ensure that it is unique. A username must be 3-30 characters long. Same rule applies to password, which is also hashed for security purposes. If user makes a mistake, flash message is displayed. If submission is successful, user will be redirected to home page and flash message will notify them of account creation.   
  
The login page also contains username and password fields. Returning registered users can log in that way to access the account.   
If the entered username and hashed password match the ones in the database, a user is redirected to the home page and informed that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input.   
  
*Logout*  
  
Hitting "logout" button by the logged in users ends their session and redirects to the homepage.  
  
  
*My Recipes - **CRUD***  
  
**Logged In** username has access to CRUD method, which allows them to read all recipes in DB, create recipes and update/delete recipes they have created.   
  
*Read*  
To view all recipes created by username logged in, they need to click on 'My Recipes'. If they have not created any recipes, the page will display paragraph inviting them to add new recipe.  
  
*Create*  
The registered and logged in users can add new recipes through the form. There are some validations in place - all the fields except "Recipe Image" are required.  If user does not provide a URL to the recipe image, the recipe placeholder will be assigned for that recipe.   
After the successful addition, a user is redirected to 'My Recipes'. There is also a button "Cancel" that simply redirects a user to 'My Recipes' page.  
  
*Edit*  
The edit recipe page allows the logged in user to update information about the recipe. The "Edit" button will appear only for the author of the recipe.  
  
*Delete*  
The delete recipe function allows only author of the recipe to delete it  
  
*Footer*  
  
The footer features links to the social media which open in a new tab (by using  `'target="_blank"`).  
  
  
**Features to implement**  
  
  
*My favourites*  
  
User would have an opportunity to "like" other recipes, saving them in "my favourites" collection, which would be displayed on a separate page. Each recipe card will include a small "heart" icon, clicking which will enable user to add the selected recipe to "my favourites".  
  
  
>##  Technology Used  
  
  
- [PyCharm](https://www.jetbrains.com/pycharm/)  -  IDE for developing this project.  
  
- [GitHub](https://github.com)  - for remotely storing project's code.  
  
  
**Front-End**  
  
- HTML - to build the foundation of the project.  
  
- CSS  - to style the project.  
  
  
**Back-End**  
  
- [Python](https://www.python.org/)  - back-end programming language used in this project.  
  
- Flask  - micro-framework for building and rendering pages.  
  
- [MongoDB](https://www.mongodb.com/)  - NoSQL database for storing back-end data.  
  
- PyMongo - for Python to get access the MongoDB database.  
  
- WTForms  - for creating forms with validation.  
  
- Bcrypt - to generate and verify password hashing.  
  
- [Heroku](https://heroku.com/)  - to host the project.  
  
    
  
**Libraries**  
  
  
- [Bootstrap](https://getbootstrap.com)  - main responsive modern front-end framework  
  
- [Google Fonts](https://fonts.google.com/)  - to import fonts.  
  
- [FontAwesome](https://fontawesome.com/)  - to provide icons used across the project.  
  
- [JQuery](_https://jquery.com/)  - to simplify DOM manipulation  

  
>## Testing 


The code has been validated using:


- [W3C Mark-up Validation Service](_https://validator.w3.org/_)

- [W3C CSS Validation Service](_https://jigsaw.w3.org/css-validator/_)


app.py was tested through  [PEP8 Online](_http://pep8online.com/_)  validator.


Manual testing was carried out on mobile devices and desktop.

*Index/Browse Recipes/Single Recipe Page*
Pages are working as expected, all links directing to correct categories. 
I have browsed as a visitor and as a logged in user. Both times features I have intended to have appeared accordingly. 
When browsing through recipes, 3 of them will appear per page with limited information about them. User has an option to view full recipe and this function worked well.
While browsing as a guest don't give you a lot of options, as a username clicking on own recipes, option for edit and delete will appear. 

*Register/Login*
Few dummies accounts have been created through out the process to test functionality. Clicking on register will take you to the simple form where username and password can be inputed. There is a character limit 3-30, if not achieved error message will pop up. I have tried all scenarios and it worked as expected. When both fields are correct and submit button clicked, user will be redirected to index page - where a paragraph inviting him to register changed to my account button. Flash message will also indicate successful creation of account.

Returning user can easily access Login page through navbar. Attempts where made to throw an error message - empty fields, username and password not corresponding, wrong username - which all came back with flash error notification. If login is successful - user again will be redirected to index page with flash message indicating sucesfull login. 

*Add/Edit/Delete Recipes*
Logged in user has an option to add and edit their own recipes. They cannot amend any other recipe in database (no option available for them to do so). 
Throughout the testing I have added bunch of recipes. Form has a required fields - if left empty - user is notified. Once the recipe is created and add button is clicked, user is redirected to 'My Account'. 

While viewing the recipe's full page, author of the recipe has an option to edit it or delete it. I have tried to view recipes created by others and those options were not available to me - which is perfect. 



>>## Deployment  
>## Credits  
>## Acknowledgements  
>## Disclaimer  
  
_The content of this website is for educational purposes only._