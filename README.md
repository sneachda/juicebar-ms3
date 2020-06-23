# **JuiceBar** 

***Practical Python and Data-Centric Development - Code Institute - Third Milestone Project***

LiveWebsite
Github

The main purpose of this project is to build a responsive website that allows user to create, read, update and delete (*CRUD*) recipes. **JuiceBar** is a MongoDB based Flask project

The user from the start will have access to all recipes stored in database. If the user wish to manipulate data - they would have to register.

It's a great way to create and store some of your favourite recipes.  

Give it a go here



 ***

>## Content:
> 

 - UX
 - [Deployment](https://github.com/irinatu17/MyCookBook#deployment)
 - Features
 - Technology Used
 - Testing
 - Deployment
 - Credits

***

## UX
### User Stories

**As a user, I want/expect:**

-   to view all the recipes without having to register
-   to view all recipe details (including cuisine, meal and diet types, cooking time, servings, list of ingredients and directions)
-   to see how many recipes are on the website
-   to create my own account
-   to add new recipes
-   to edit my recipes
-   to view a list of my recipes on a separate page and see how many recipes I've created
-   to delete my recipes
-   to log out any time and have the session terminated
-   to change my current username
-   to change my current password
-   to delete my account and all recipes I've created
-   to use the website from any device (laptop, tablet, mobile)

_Design_
The goal in design was to create a website that is overall user friendly, has a modern feel with emphasis on providing information about recipes in a readable and eye-catching way. Therefore, following design choices were made:

[Materialize](https://materializecss.com/), front-end framework based on Material Design was chosen for this project for its modern interface and ease of use. It was used for creating features such as navbar, cards, forms, modal, as well as for its grid.  
[JQuery](https://jquery.com/)  was used for initializing some Materialize elements listed above, as well as for custom functions, simple DOM manipulation.
_Font and Colour Scheme_

_Logo_

_Wireframe:_
designs

## Features
**Existing Features**

***Navbar***
The navbar is fixed at the top of the page, this allows a user to easily navigate throughout the website. The logo is located in the top right corner on a desktop and in the center on smaller devices. It redirects the user to the home page when clicked. On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.

***Home page and Featured Recipes***
The home page contains a button that redirects a user to the "All Recipes" page. It also displays 4 random images from the database using the  `$sample`  function of MongoDB.

The all recipes page displays recipe cards sorted from the oldest to the most recently added. As well as that, there is a total number of recipes displayed in parentheses after the heading. All recipe cards are clickable and redirect a user to the individual recipe page with detailed information. The pagination at the bottom of the page allows to display 8 recipes per page.

***Register***
The register page allows a user to create a new account. The user is asked to fill the fields "username", "password" and "confirm password". When adding a username, the code compares it against existing usernames to ensure that it is unique. A username must be 3-15 characters long. The same requirement applies to the password field. The "confirm password" field must match the original password. All passwords are hashed for security purposes. If user's input does not meet requirements, flash messages will inform a user about the error. When the form is submitted successfully, a user is redirected to the home page and informed that account was created. There is also a link to the login page for existing users at the bottom of the form.

***Login***
The login page features the form with "username" and "password" fields, allowing registered users to log into their account. If the entered username and hashed password match the ones in the database, a user is redirected to the home page and informed that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input. There is also a link to the register page for new users at the bottom of the form.

***My Recipes***
CRUD

***Footer***

The footer features links to the social media which open in a new tab (by using  `'target="_blank"`).


**Features to implement**
#### Search recipe

At this stage Search functionality was considered not as important as other features. However, I believe that in future as the website will grow, it will be necessary to implement it.  
The search recipe function is based on the keyword and recipe name, allowing user to search for the recipe. Filters "by cuisine", "by meal type" and "by diet type" would allow user to have more detailed search.

 ## **Technology Used**

-   [GitPod](https://www.gitpod.io/)  - an online IDE for developing this project.
-   [Git](https://git-scm.com/)  - for version control.
-   [GitHub](https://git-scm.com/)  - for remotely storing project's code.
-   [PIP](https://pip.pypa.io/en/stable/installing/)  - for installation of necessary tools.
-   [GIMP2](https://www.gimp.org/)  - for editing, compressing and resizing images.
-   [Am I Responsive](http://ami.responsivedesign.is/)  - for creation of the images in the readme file and checking responsiveness.
-   [Ezgit](https://ezgif.com/)  - to create gifs for README
-   [Imgur](https://imgur.com/)  - to host gifs
-   [ImgBB](https://imgbb.com/)  - to host images used in README

**Front-End**

-   [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)  - to build the foundation of the project.
-   [CSS](https://developer.mozilla.org/en-US/docs/Archive/CSS3)  - to create custom styles.

**Back-End**

-   [Python 3.8.2](https://www.python.org/)  - back-end programming language used in this project.
-   [Flask 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)  - microframework for building and rendering pages.
-   [MongoDB Atlas](https://www.mongodb.com/)  - NoSQL database for storing back-end data.
-   [PyMongo](https://api.mongodb.com/python/current/)  - for Python to get access the MongoDB database.
-   [WTForms 2.2.1](https://pypi.org/project/WTForms/)  - for creating forms with validation.
-   [Werkzeug 0.16.1](https://werkzeug.palletsprojects.com/en/0.16.x/)  - to generate and verify password hashing.
-   [Jinja 2.10.1](https://jinja.palletsprojects.com/en/2.10.x/)  - templating language for Python, to display back-end data in HTML.
-   [Heroku](https://heroku.com/)  - to host the project.

**Libraries**

-   [Materialize 1.0.0](https://materializecss.com/)  - main responsive modern front-end framework used for grid and responsivesness.
-   [Google Fonts](https://fonts.google.com/)  - to import fonts.
-   [FontAwesome](https://fontawesome.com/)  - to provide icons used across the project.
-   [Adorable Avatars](http://avatars.adorable.io/)  - to create user avatars.
-   [JQuery 3.5.0](https://jquery.com/)  - to simplify DOM manipulation and to initialize Materialize functions.

**Testing**

The code has been validated using:

-   [W3C Mark-up Validation Service](https://validator.w3.org/)
    
-   [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

#### JavaScript

JS file was tested through  [Esprima](https://esprima.org/demo/validate.html)  and  [JSHint](https://jshint.com/)  validators, code was syntactically valid. "$" was not defined by JSHint (it is necessary for jQuery Materialize initializing).

#### [](https://github.com/irinatu17/MyCookBook#python)Python

All python files were tested through  [PEP8 Online](http://pep8online.com/)  validator and were completely PEP8 compliant, except one thing:

-   in "_init_.py" file, the following import  `from mycookbook import routes`  has to be located at the bottom of the file as it needs to import routes after the app has been initialised to prevent circular imports.

*Manual testing*

#### User stories testing

All the following manual testing was implemented on both desktop and mobile devices.

##### [](https://github.com/irinatu17/MyCookBook#all-recipes-and-single-recipe-display)All recipes and single recipe display

When I click on "All Recipe page", I can see recipe cards displayed in rows, 8 recipes per page. In that view, I can see image, recipe name and short information about the recipe. Clicking on the recipe card redirects me to the single recipe page, where I can see all the detailed information about the recipe. I tested this functionality as a non-logged in (guest) user and a logged in user and it perfectly worked in both cases. I also can see the total number of the recipes in parentheses. I tried to add and delete some recipes, and this number changed accordingly.

##### [](https://github.com/irinatu17/MyCookBook#create-a-new-user-account)Create a new user account

I created my main account, as well as a few test accounts to test this functionality. Clicking on the "Register" button in the navbar opens the form, where I can put username and password to create a new account. I tried to input an existing username, not matching passwords in "password" and "confirm password" fields, and input less then 3 or more then 15 charachters. In all cases I got a corresponding flash error message. As well as that, I tried to leave an empty field and submit the form, but got an error message again asking to fill the field. When the form was successfully submitted, I was redirected to the home page, seeing a message that my new account was created. I also checked the link to the Login page at the bottom of the form, which worked well.

##### [](https://github.com/irinatu17/MyCookBook#login-1)Login

Clicking on the "Login" button in the navbar opens the form, allowing me to login to my account. I tried to leave empty fields or input incorrect details, but I was not able to submit the form if something was entered incorrectly. After a successful login I was redirected to the home page, seeing the message that I was logged in. I also checked the link to the Register page at the bottom of the form, which worked well.

##### [](https://github.com/irinatu17/MyCookBook#change-usernamepassword)Change username/password

I changed my username and password multiple times to ensure that this functionality works well. Both pages open when the corresponding buttons are clicked. Validations against existing username and against incorrect input works well. In both forms I can see the flash messages about the changes I made. As well as that, If I click "Cancel" button, I will be redirected to the "Account Settings" page. For "change username" function, I checked database to make sure that username was updated there.

##### [](https://github.com/irinatu17/MyCookBook#delete-account-1)Delete Account

I deleted some testing accounts to test the functionality. Followed by clicking the "Delete account" button on the Account Settings page, the modal opens and I am asked to confirm the deletion by entering my password. I tried to put the wrong password, but got an error flash message. When I input the correct password, I am redirected to the home page and see the message that my account was deleted. Then, I checked the database to make sure that the account as well as all the recipes created by this user were removed.

##### [](https://github.com/irinatu17/MyCookBook#add-new-recipe)Add New Recipe

I added plenty of test recipes to check the functionality throughout the development. If I leave some of the required fields empty, I will not be able to submit the form. I can see the flash messages displayed if my input does not meet length requirement. I also tried to create recipe without the URL image provided, to check if the placeholder is in place and it works well.

##### [](https://github.com/irinatu17/MyCookBook#edit-recipe-1)Edit Recipe

If I am the author of selected recipe, I can see the buttons "Edit" and "Delete" in the single_recipe page. I tried to view someone else's recipes and the buttons were not displayed. I also tried to change the link manually in the browser to edit other's recipe. However, I was not able to open the form and got the message, that I can only edit my own recipes, which means defensive design works well against brute forcing. Being the author of the recipe, I can view the form with pre-populated fields and can change anything that I want. If all fields are valid, I can see the changes I made in a Single Recipe Details Page after the submission. I tried to edit a number of recipes and edit different fields, everything worked correctly.

##### [](https://github.com/irinatu17/MyCookBook#delete-recipe-1)Delete Recipe

I deleted some dummy testing recipes to test the functionality. After clicking the "delete" button, I saw the modal showing up asking me to confirm the deletion. After clicking "Cancel" I was redirected back and modal closeed. After clicking "Delete" button in the modal, I was redirected to the home page and saw the message about the succsessful deletion.  
Then I checked the database to make sure, that the recipe was removed. As well as that, I tested against brute-forcing, trying to delete another user's recipe(by changing the link manually in the browser), but wasn't able to do that.

##### [](https://github.com/irinatu17/MyCookBook#my-recipes-1)My Recipes

The link in the navbar leads to the My Recipes page, where I can see the total number of my recipes, my recipe cards, "Add New Recipe" button and pagination in place. I tested pagination by clicking the buttons to switch pages, tested the "Add New Recipe" button that redirects to the corresponding form and tested total number change by creating/deleting a recipe. All functionality works well.

##### [](https://github.com/irinatu17/MyCookBook#404-and-500-errors)404 and 500 errors

I manually changed URL in the browser to get a non-existing page to test errors-handler function. Custom page loads and all links in the navbar and the button "Back Home" work well.

##### [](https://github.com/irinatu17/MyCookBook#navbar-footer)Navbar/ Footer

All links in the navbar and the footer were manually tested to ensure that they are pointing to the correct destination.

Apart from that, I was manually testing the app with  **debugger**:  `debug=True`  throughout all the development process. Every time when there was an error (when app crashed), the debugger displayed an error message to the view, that allowed me to find the location of the error and fix it.

#### [](https://github.com/irinatu17/MyCookBook#further-testing)Further testing

I also asked my friends, family members and fellow students in Slack to thoroughly test my website in different devices. So, a number of new accounts were created and new recipes added/edited and some of them were deleted. At that stage I got useful feedback and a few issues were found:

##### [](https://github.com/irinatu17/MyCookBook#known-bugs)Known bugs

-   The text of the "Delete" and "Edit" buttons disappeared on small devices (320px size), so I added a media query to fix this issue
-   There was a similar issue with the "Change username" and the "Change password" buttons, to solve it I removed "buttons-container" class to increase width between the buttons.
-   I was adviced to make "Add Recipe" button more visible to the user, as it was dipplayed only on the navbar dropdown. To fix that, I added the "Add new recipe" button to the "My Recipes" page above the recipe cards. Also, I added icons in the navbar dropdown to give a user visual clue about the links.
-   I also added a small-greeting text above the user avtar in "Account Settings" to make it more user-friendly as some users did not understand "what does this face mean".
-   IMPORTANT NOTE: I accidentally introduced that error with creating extra spaces again during "last-minute" corrections. I was trying to beautify the code, which broke the Jinja logic and was not able to fix it quickly

## Deployment

The site was developed using PyCharm. Using version control in PyCharm I was able to commit and push to GitHub.

Those steps were taking in order to deploy my page from GitHub repository:

1.  On Github navigate to  [sneachda/portfolio-milestone-1](https://github.com/sneachda/portfolio-milestone-1)
2.  From the menu at the top click on  `settings`
3.  Scroll down to the  _GitHub pages_  section
4.  Under  _Source_  section click on dropdown menu and select  _Master Branch_  as your GitHub pages publishing source.
5.  Select  `save`.

To create a local repository please follow those steps:

1.  Go to  [Github Project Repository](https://github.com/sneachda/portfolio-milestone-1)
2.  Under the repository name click  `Clone or download`
3.  In the 'Clone with HTTPs section' clone URL for the repository.
4.  Open Git Bash in your local platform.
5.  Change the current working directory to the location where you want the cloned directory to be made.
6.  Type git clone, and then paste the URL copied earlier: git clone  [https://github.com/sneachda/portfolio-milestone-1.git](https://github.com/sneachda/portfolio-milestone-1.git)
7.  After pressing ENTER your local clone will be created.

## Credits

**Content**
All recipes and recipes' images are taken from [BBC Good Food](https://www.bbcgoodfood.com/) except the ones added by other users.


**Code**

### Code

1.  [Stack Overflow](https://stackoverflow.com/), the Code Institute Slack were extremely helpful and useful during the process of building this project.
2.  I constantly referred to the following documentation sources:  [Flask](https://flask.palletsprojects.com/en/1.1.x/)  and  [MongoDB](https://docs.mongodb.com/manual/).
3.  For building the Register, Login, Change Username/Password pages, as well as for better understanding  `session`  , I used the following tutorials:

-   **Flask Tutorials**  -  [Corey Schafer](https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)  - package structure, custom error pages, WTForms, hashing passwords
-   **The Flask Mega-Tutorial**  -  [Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
-   **Flask WTForms Tutorials**  -  [Pretty Printed](https://www.youtube.com/watch?v=eu0tg4vgFr4&list=PLXmMXHVSvS-C_T5JWEDWIc9yEM3Hj52-1)

4.  Pagination logic, used for All Recipes and My Recipes pages, was inspired by Shane Muirhead's project.
5.  For UI & UX design concept I took inspiration from different projects found in  [Dribble](https://dribbble.com/)
6.  The idea of using prefix-icons, asterixes and question-mark tooltips in forms was taken and modified from Tim Nelson's project.
    

**Acknowledgments**



**Disclaimer**

_The content of this website is for educational purposes only._