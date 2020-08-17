# **JuiceBar**   
***Practical Python and Data-Centric Development - Code Institute - Third Milestone Project***  
  
[LiveWebsite: JuiceBar](https://juicebar-cookbook.herokuapp.com/)
[JuiceBar Github repository](https://github.com/sneachda/juicebar-ms3) 
[Wireframes]()

  
The main purpose of this project is to build a responsive website that allows user to create, read, update and delete (*CRUD*) recipes. **JuiceBar** is a MongoDB based Flask project  
  
The user from the start will have access to all recipes stored in database. If the user wish to manipulate data - they would have to register.  
  
It's a great way to create and store some of your favourite recipes.    
  
Give it a go [here](https://juicebar-cookbook.herokuapp.com/)

***
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

***Features***

*Navbar*
The navbar is fixed on top of the page. Logo is located on the left hand side, which redirects user to home page when clicked.  On the smaller devices the navbar is collapsed into a burger icon.  

*Home Page and Recipes Pages*
Home Page has a very simple role to play - it invites users to create their own account. It also allows them to browse all recipes that have been already created. 
Once they create account, paragraph previously containing link to register page has three buttons allowing them to browse recipes with ease. 

Depending on browsing option chosen, people visiting the page can browse all recipes at once, or pick by category: juices or smoothies. They all display recipe cards, which contain short description of the recipe with few additional details. All recipe cards are clickable and redirect user to the individual recipe page with detailed information. 

*Register/Login*
The register page allows a user to create a new account. Two fields are displayed: username and password which need to be filled in. When adding a username, the code compares it against existing usernames to ensure that it is unique. A username must be 3-30 characters long. Same rule applies to password, which is also hashed for security purposes. If user makes a mistake, flash message is displayed. If submission is successful, user will be redirected to home page and flash message will notify them of account creation. 

The login page also contains username and password fields. Returning registered users can log in that way to access the account. 
If the entered username and hashed password match the ones in the database, a user is redirected to the home page and informed that the log in was successful. Otherwise, flash messages will be displayed about incorrect user's input. 

*My Recipes - **CRUD***


*Footer*
The footer features links to the social media which open in a new tab (by using  `'target="_blank"`).

