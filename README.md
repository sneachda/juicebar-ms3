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
    
*Color Scheme* One of the main goals was to focus user's attention on the recipe cards and recipes' images. Therefore, I decided to have clean white pages with popping color from images which comes with recipes.     
    
    
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
  
  
 - app.py was tested through  [PEP8 Online](_http://pep8online.com/_) 
   validator.

  
  
*Manual testing was carried out on mobile devices and desktop.*  
  
*Index/Browse Recipes/Single Recipe Page*  
Pages are working as expected, all links directing to correct categories.   
I have browsed as a visitor and as a logged in user. Both times features I have intended to have appeared accordingly.   
When browsing through recipes, 3 of them will appear per page with limited information about them. User has an option to view full recipe and this function worked well.  
While browsing as a guest don't give you a lot of options, as a username clicking on own recipes, option for edit and delete will appear.   
  
*Register/Login*  
Few dummies accounts have been created through out the process to test functionality. Clicking on register will take you to the simple form where username and password can be inputed. There is a character limit 3-30, if not achieved error message will pop up. I have tried all scenarios and it worked as expected. When both fields are correct and submit button clicked, user will be redirected to index page - where a paragraph inviting him to register changed to my account button. Flash message will also indicate successful creation of account.  
  
Returning user can easily access Login page through navbar. Attempts where made to throw an error message - empty fields, username and password not corresponding, wrong username - which all came back with flash error notification. If login is successful - user again will be redirected to index page with flash message indicating sucesfull login.   

*My Recipes*
It allows user to view their own recipes in one place.  Pagination and change in navbar after login worked each time. 
  
*Add/Edit/Delete Recipes*  
Logged in user has an option to add and edit their own recipes. They cannot amend any other recipe in database (no option available for them to do so).   
Throughout the testing I have added bunch of recipes. Form has a required fields - if left empty - user is notified. Once the recipe is created and add button is clicked, user is redirected to 'My Account'.   
  
While viewing the recipe's full page, author of the recipe has an option to edit it or delete it. I have tried to view recipes created by others and those options were not available to me - which is perfect.  I also tried to change the link manually in the browser to edit other's recipe. However, I was not able to open the form and got the message, that I can only edit my own recipes.

I deleted some dummy testing recipes to test the functionality. I received confirmation message saying deletion was successful. 

Each time I performed above tasks I have checked Mongo DB to ensure actions were reflected there.  

*Footer*
Links have been tested to check if they redirecting to correct source.

***
*General issues*

Throughout the editing process I have been testing application with 'debug=true' Each time the error appeared, I was pointed to the location and was able to fix it.

Biggest issues appeared when I tried to register not locally but through heroku app. Error message with pointing to majority was coming up each time someone tried to create new username. It was easily fixed by copying the link from MongoDB again and updating variable in heroku settings. 

App was tested by friends and family members. Overall I received positive feedback about functionality of the app. I have changed few styling issues - changed the colour scheme to make it more 'clean' looking, made sure cursor has a style attached while hovering above navbar. 
  
  ***
  ### Compatibility and Responsiveness

This website had been being tested during the development across  **multiple browsers**  and on  **multiple devices**: mobile (iPhone, Samsung), tablets(iPad) and laptops.
I also used  **Google Chrome's developer tools**  to see how it looks across all the different device screen sizes to ensure compatibility and responsiveness.  
Necessary media queries were added to make the website fully responsive.  
The one issue was found that website renders poorly on Internet Explorer browser.
  
>## Deployment 


This project was developed using PyCharm as the chosen IDE and GitHub as a remote repository.

***Deploying this project to Heroku***

 1.  I created a Heroku account, signed in and created a new app with a unique name. I then set the region to the closest to me: 'Europe'.
 2.  With the app created, I went to the 'Settings' tab and clicked the 'Reveal Config Variables' button. From here, I input the following values:

```
MONGO_URI: mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority
MONGO_DBNAME
SECRET_KEY
IP: 0.0.0.0
PORT: 5000
```
 3.  I have deployed project to Heroku by connecting with GitHub. I found it easier pushing changes to one remote repository.  And I allowed for automatic deploys which means my project was updating 'in real time'

***
To create a ***local repository*** please follow those steps:

 
1.  Go to  [Github Project Repository](https://github.com/sneachda/juicebar-ms3)

2.  Under the repository name click  `Clone or download`

3.  In the 'Clone with HTTPs section' clone URL for the repository.

4.  Open Git Bash in your local platform.

5.  Change the current working directory to the location where you want the cloned directory to be made.

6.  Type git clone, and then paste the URL copied earlier: git clone  [https://github.com/sneachda/juicebar-ms3.git](https://github.com/sneachda/juicebar-ms3.git)

7.  After pressing ENTER your local clone will be created.

  
Once you have the project cloned on your computer, you are ready to set everything up.

8.  Open the Terminal and navigate to  downloaded  folder on the computer.
9.  Install the libraries from requirements.txt by typing  `pip3 install -r requirements.txt`
10. At this stage env.py file should be created where you would store details like: MONGO_URI (mongodb+srv://<username>:<password>@<cluster_name>-ocous.mongodb.net/<database_name>?retryWrites=true&w=majority -- replacing fields username, password and cluster name) and secret_key. 1.  At the top of env.py add the following line  `import os`. The env.py should be added to .gitignore for security reasons. 
11.  Your cloned version is now ready to run locally with the following command:
```
python3 app.py
```
12.  Paste  `[http://127.0.0.1:5000/](http://127.0.0.1:5000/)` into your browser URL to access.

>## Credits 

**Content**

 - All recipes and recipes' images are taken from [BBC Good
   Food](_https://www.bbcgoodfood.com/_) except the ones added by other
   users.
   
  - To achieve hover effect on some of my images I have looked into
   [https://thebrandsmen.com/css-image-hover-effects/](https://thebrandsmen.com/css-image-hover-effects/)
   
   - I have used several flask tutorials and edited the code to my needs.
   Biggest help was [Corey Schafer](_https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH_) with his youtube tutorials that helped me with set up and WTF forms mainly. I have also learned about pagination from him.

	- The Flask Mega-Tutorial  -  [Miguel Grinberg](_https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world_) was recommended to me by my mentor.

	- Projects of other student have been very useful during this process. I have adopted pagination from Shane Muirhead's project and I was also guided by student with GitHub username: [irinatu17](https://github.com/irinatu17)



>## Acknowledgements 

I have had a big support network during the development process and I would like to thank all who have been involved: Code Institute tutors, students, friends and my mentor: Maranatha Ilesanmi. 

>## Disclaimer    
 _The content of this website is for educational purposes only._