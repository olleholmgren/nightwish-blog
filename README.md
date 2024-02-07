# **NIGHTWISH Platform**

![MOCKUP](/static/images/mockup-fav-album.png)

An online interactive fanzine for dedicated fans of the great symphonic metal band.

Visit site at [NIGHTWISH Platform](https://nightwish-blog.herokuapp.com/).

# Table of Content

* [**Purpose**](<#purpose>)
* [**Existing Features**](<#existing-features>)
* [**Project Journey**](<#project-journey>)
* [**UI/UX**](<#uiux>)
* [**Agile**](<#agile>)
* [**Future Features**](<#future-features>)
* [**Testing**](<#testing>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
* [**Acknowledgements**](<#acknowledgements>)

# Purpose
The aim for this project is to create a PLATFORM for NIGHTWISH fans to gather and share thoughts and opinions as well as exchange experiences with each other about NIGHTWISH.

### Goal
As an owner, my goal is to be able to run and maintain a PLATFORM that will use the CRUD(Create, Read, Update, Delete) functionality in order to serve dedicated fans of NIGHTWISH. The user will have the choice of either sign up as a Member to the PLATFORM or to just remain a Guest
This means that the user will be able to: 

[Back to top](<#table-of-content>)
# Existing Features
### Guest, Member and Admin
#### Guest(User)
If the user does not sign up to the PLATFORM they will remain a Guest.
The Guests of the PLATFORM will enjoy the following features:
- View/read posts

#### Member(User)
If the user choose to sign up to the PLATFORM they will become a Member.
The Members of the PLATFORM will enjoy the following features(new features not presented above are written in bold italics):
- View/read posts
- ***Create posts***
- ***Update (their own) posts***
- ***Delete (their own) posts***

#### Admin (Owner)
The Admin is the person "at the controls" who runs and maintains the PLATFORM.
If the Guest or Member grants the permission to run and maintain the PLATFORM they will become an Admin.
The Members of the PLATFORM will enjoy the following features(new features not presented above are written in bold italics):
- View/read posts
- Search posts
- Create posts
- Like posts
- Comment posts
- ***Verify posts***
- ***Update (all) posts***
- ***Delete (all) posts***

[Back to top](<#table-of-content>)
# Project Journey
## Diagrams and wireframe
While staring up my blog project, I wanted to have a clear overview of what features and functions I need my PLATFORM in order to have a fully functional PLATFORM.	
After discussing with my fellow classmates at Code Institute it came to my understanding that it is a very good idea to start with a sketch or flowchart. So I started to create the Use Case Diagram as visible below:

## Use Case Diagram
I made this Use Case Diagram mostly in order to get the broader picture of what the actual product will have in terms of features for the:
- Admin
- User
- Guest

![UCD](/static/images/ucd-fav-album.png)

[Back to top](<#table-of-content>)
# UI/UX
I wanted to build a clean and neat blog/forum which is very easy to use. There are no surprises or misguiding attributes. The main focus is to meet the user's expectations of what a blog should look like.

## The 5 'S' Planes of User Experience(UX)
### Strategy
Focuses on fulfilling user needs and product objectives. In this particular project, the emphasis was on deviating from the common functionalities found on other websites, such as social media interactions, discussions, and excessive visual content. The primary goal was to create a serene and creative space. The content available for browsing was deliberately kept at a simplistic level.

### Scope
Determines the project's functional boundaries and included features. Minimal functionality was considered essential for this project, meaning that most features were considered basic requirements. Features like user sign up and login were necessary, along with fundamental CRUD functionality for authenticated users. More comprehensive explanations of all the current features can be found in the Existing Features section. Future features, discussed in the Future Features section, were considered unnecessary at the present moment, although they remained within the project's potential scope.

### Structure
Defines how users can navigate the site and utilize all the existing features. The site's structure was modeled after a basic blog site, which is a commonly used template. This structure enables users to visit the site, browse posts from fans and share thoughts on favourite albums.
However, in order to contribute to the site in any capacity, user authentication is required, which necessitates creating an account.

### Skeleton
Translates the features outlined in the structure into navigational elements. For an initial overview of the project's skeleton. To ensure an intuitive navigation experience, both the navbar and the main content adhere to a standard layout pattern that most users would find familiar. The navbar provides links to the main features and functions of the site, with variations depending on whether the user is authenticated or not. On smaller to medium screen sizes, a drop-down 'burger' menu replaces the full navigation bar. Buttons and links are appropriately labeled, and clear and simple instructions on how to use the page can be found in relevant sections. The footer includes social media links, which are currently serving as placeholders, completing the overall layout of the site.

### Surface
Addresses visual design and the means of conveying desired emotions and achieving desired effects.

[Back to top](<#table-of-content>)
# Agile
In software and web development, it is very useful to adapt the Agile mindset when working on or starting up a project. 
For this project, I have imagined and made up an imaginary group of people and they are called Users. 
I sort these Users in three different categories: Guests, Members and Admin.
One important agile tool to use in the very beginning of a project is called User Stories.
So the User Strories for my project are as stated below.

### Design thinking and User Stories
I order to approach this project in a Design Thinkng way, I have put myself in the User's perspective so that I can manage to sort out what the purpose of the PLATFORM will be.

For the User Story part, I have referred to the very reliable source of Niel McEwens Common Agile Practices content from Code Institute.

### User Stories
#### Guest
- As a Guest, I want to be able to read posts without signing up for the PLATFORM in order to save time and energy.
- As a Guest, I want to be able to search for posts in order to find content that interests me.
- As a Guest, I want to be able to sign up to the PLATFORM in order to enjoy all features of a Member.

#### Member
- As a Member, I want to be able to Create posts so that I can share my thoughts and feelings to the world.
- As a Member, I want to be able to Read posts in order to be able to gain information about other peoples thoughts and feelings.
- As a Member, I want to be able to Update posts so that I can add any additional content of my choice.
- As a Member, I want to be able to Delete posts so that I can choose to not show a post that I do not like.
- As a Member, I want to be able to like posts in order to express my feelings about other peoples posts.

#### Admin
- As an Admin, I want to be able to verify the posts before they are visible at the PLATFORM, in order to avoid for example foul or abusive language or even harassment.

[Back to top](<#table-of-content>)
# Future Features
### Guest, Member and Admin
#### Guest(User)
If the user does not sign up to the PLATFORM they will remain a Guest.
The Guests of the PLATFORM will enjoy the following features:
- View/read posts
- Search posts

#### Member(User)
If the user choose to sign up to the PLATFORM they will become a Member.
The Members of the PLATFORM will enjoy the following features(new features not presented above are written in bold italics):
- View/read posts
- Search posts
- ***Create posts***
- ***Like posts***
- ***Comment (all) posts***
- ***Update (their own) posts***
- ***Delete (their own) posts***

#### Admin (Owner)
The Admin is the person "at the controls" who runs and maintains the PLATFORM.
If the Guest or Member grants the permission to run and maintain the PLATFORM they will become an Admin.
The Members of the PLATFORM will enjoy the following features(new features not presented above are written in bold italics):
- View/read posts
- Search posts
- Create posts
- Like posts
- Comment posts
- ***Verify posts***
- ***Update (all) posts***
- ***Delete (all) posts***

[Back to top](<#table-of-content>)

# Testing
## Manual testing throughout the entire website

| Status | **Website (NIGHTWISH PLATFORM) - User not logged in**

index.html & base.html
|:-------:|:--------|
| &check; | Clicking the website name in nav bar loads the home page
| &check; | Clicking the nav-bar 'HOME' button loads the home page
| &check; | Clicking the nav-bar 'Pick your album(favourite_album.html)' button loads blank page with instructions how to sign up/log in
| &check; | Clicking the nav-bar 'List of albums' button loads the page with users favourite albums
| &check; | Clicking the nav-bar 'Sign Up' button loads the 'Sign up' page
| &check; | Clicking the nav-bar 'Log in' button loads the 'Log in' page
| &check; | Clicking the body 'Log in' link loads the 'Log in' page
| &check; | Clicking the body 'SIGN UP TO BECOME A MEMBER' button loads the 'Sign up' page
| &check; | Clicking the footer 'X'-icon link redirects to X.com
| &check; | Clicking the footer 'f'-icon link redirects to facebook.com
| &check; | Clicking the footer Instagram icon link redirects to instagram.com

favourite_album.html('Pick your album')
|:-------:|:--------|
| &check; | Clicking the body 'SIGN UP' link loads the 'Sign up' page
| &check; | Clicking the body 'LOG IN' link loads the 'Log in' page

user_favourite_albums.html
|:-------:|:--------|
| &check; | Clicking the body 'PICK YOUR FAVOURITE ALBUM(favourite_album.html)' button loads blank page with instructions how to sign up/log in

accounts/signup.html
|:-------:|:--------|
| &check; | Clicking the body 'sign in' link loads the 'Log in' page
| &check; | Clicking the form 'SIGN UP' button (without completing form correctly) shows error message
| &check; | Clicking the form 'SIGN UP' button (having completed form correctly) creates account, renders HOME page with welcome message, greeting new user by name(how polite.)

accounts/login.html
|:-------:|:--------|
| &check; | Clicking the body 'sign up' link loads the 'Sign up' page
| &check; | Clicking the form 'LOG IN' button (without completing form correctly) shows error message
| &check; | Clicking the form 'LOG IN' button (having completed form correctly) logs in user, renders HOME page with welcome message, greeting the user by name(how polite!)


| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page



## Code Validation
### Python
The Python code on the 'NIGHTWISH Platform' site has been tested and validated through the fantastic Python Linter at https://pep8ci.herokuapp.com/ by Code Institute.

* admin.py - 
* forms.py - 
* models.py - 
* test_forms.py - 
* urls.py - 
* views.py - 

### HTML
The HTML code on the 'NIGHTWISH Platform' site has been tested through W3C Markup Validation Service.
The 10 problems and errors shown on the first image were later fixed by myself. The result is shown in the second image.

![HTML Result Error](/static/images/html_validation_error.png)

![HTML Result No Error](/static/images/html_validation_no_error.png)

### CSS
The CSS code on the 'NIGHTWISH Platform' site has been tested manually by inputting my css file in the W3C CSS Jigsaw Validator.
No errors reported.

![CSS Result](/static/images/css_validation_no_error.png)

![CSS Result 2](/static/images/css_validation_no_error2.png)

### JavaScript
The JavaScript code on the 'NIGHTWISH Platform' site has been tested in JSHint.com.
No errors were returned but the test reported one undefined variable connected to Bootstrap which is fine.

![JSHint Validation](/static/images/js_hint_validation.png)

[Back to top](<#table-of-content>)

## Languages and technologies
- HTML: Used for structuring all the templates on the site.
- CSS: Utilized to provide additional styling to the site.
- JavaScript: Used to be able to collapse the nav bar whilst using on smaller screens.
- Bootstrap: Utilized to style the website, ensuring responsiveness and interactivity.
- Python: Implemented to deliver functionality to the site. All written code in the class-based models, views, admin, forms etc are written in Python.
- Django: Utilized as the backend logic framework for the project, enabling rapid and secure development.
- Django Packages:
    - Summernote: Utilized as a text editor.
    - Allauth: Employed for authentication, registration, and account management.
    - Crispy Forms: Used for styling forms.

- Git: Used for version control, with the Gitpod terminal being utilized to commit changes to Git and push them to GitHub.
- GitHub: Employed to store the project's code after pushing it from the workspace.
- Heroku: Utilized for deploying the live project.
- PostgreSQL: Database that is used through Heroku.
- Lucid Chart: Used to create diagrams and use case for the project.
- Chrome Developer Tools: Utilized for inspecting page elements, debugging and troubleshooting.The Lighthouse extension installed in the Chrome Browser was used to generate the performance report.
- Google Fonts
- Font Awesome

[Back to top](<#table-of-content>)
# Deployment
## Deployment To Heroku
The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

1. To begin with we need to create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.

<details><summary><b>Heroku Deployment - Step 1</b></summary>

</details><br />

2. Fill in the needed details as stated in the screenshot below and then click 'Create Repository From Template'.

<details><summary><b>Heroku Deployment - Step 2</b></summary>

</details><br />

3. When the repository creation is done click 'Gitpod' as stated in the screenshot below.

<details><summary><b>Heroku Deployment - Step 3</b></summary>

</details><br />

4. Now it's time to install Django and the supporting libraries that are needed. Type the commands below to do this.

* ```pip3 install 'django<4' gunicorn```
* ```pip3 install 'dj_database_url psycopg2```
* ```pip3 install 'dj3-cloudinary-storage```

<details><summary><b>Heroku Deployment - Step 4</b></summary>

</details><br />

5. When Django and the libraries are installed we need to create a requirements file.

* ```pip3 freeze --local > requirements.txt``` - This will create and add required libraries to requirements.txt

<details><summary><b>Heroku Deployment - Step 5</b></summary>

</details><br />

6. Now it's time to create the project.

* ```django-admin startproject YOUR_PROJECT_NAME .``` - This will create your project

<details><summary><b>Heroku Deployment - Step 6</b></summary>

</details><br />

7. When the project is created we can now create the application.

* ```python3 manage.py startapp APP_NAME``` - This will create your application

<details><summary><b>Heroku Deployment - Step 7</b></summary>

</details><br />

8. We now need to add the application to settings.py

<details><summary><b>Heroku Deployment - Step 8</b></summary>

</details><br />

8. Now it is time to do our first migration and run the server to test that everything works as expected. This is done by writing the commands below.

* ```python3 manage.py migrate``` - This will migrate the changes
* ```python3 manage.py runserver``` - This runs the server. To test it, click the open browser button that will be visible after the command is run.

9. Now it is time to create our application on Heroku, attach a database, prepare our environment and settings.py file and setup the Cloudinary storage for our static and media files.

* Head on to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

* In the top right corner there is a button that is labeled 'New'. Click that and then select 'Create new app'.

<details><summary><b>Heroku Step 09</b></summary>

</details><br />

10. Now it's time to enter an application name that needs to be unique. When you have chosen the name, choose your region and click 'Create app".

<details><summary><b>Heroku Step 10</b></summary>

</details><br />

11. To add a database to the app you need to go to the resources tab ->> add-ons, search for 'Heroku Postgres' and add it.

<details><summary><b>Heroku Step 11</b></summary>

</details><br />

12. Go to the settings tab and click on the reveal Config Vars button. Copy the text from DATABASE_URL (because we are going to need it in the next step).

<details><summary><b>Heroku Step 12</b></summary>

</details><br />

13. Go back to GitPod and create a new env.py in the top level directory. Then add these rows.

* ```import os``` - This imports the os library
* ```os.environ["DATABASE_URL_FROM HEROKU"]``` - This sets the environment variables.
* ```os.environ["SECRET_KEY"]``` - Here you can choose whatever secret key you want.

<details><summary><b>Heroku Step 13</b></summary>

</details><br />

14. Now we are going to head back to Heroku to add our secret key to config vars. See screenshot below.

<details><summary><b>Heroku Step 14</b></summary>

</details><br />

15. Now we have some preparations to do connected to our environment and settings.py file. In the settings.py, add the following code:

```import os```

```import dj_database_url```

```if os.path.isfile("env.py"):```

```import env```

<details><summary><b>Heroku Step 15</b></summary>

</details><br />

16. In the settings file, remove the insecure secret key and replace it with:
```SECRET_KEY = os.environ.get('SECRET_KEY')```

<details><summary><b>Heroku Step 16</b></summary>

</details><br />

17. Now we need to comment out the old database setting in the settings.py file (this is because we are going to use the postgres database instead of the sqlite3 database).

<details><summary><b>Heroku Step 17 1/2</b></summary>

</details><br />

Now, add the link to the DATABASE_URL that we added to the environment file earlier.

<details><summary><b>Heroku Step 17 2/2</b></summary>

</details><br />

18. Save all your fields and migrate the changes.

```python3 manage.py migrate```

19. Now we are going to get our connection to Cloudinary connection working (this is were we will store our static files). First you need to create a Cloudinary account and from the Cloudinary dashboard copy the API Environment Variable.

20. Go back to the env.py file in Gitpod and add the Cloudinary url (it's very important that the url is correct):

```os.environ["CLOUDINARY_URL"] = "cloudinary://************************"```

21. Let's head back to Heroku and add the Cloudinary url in Config Vars. We also need to add a disable collectstatic variable to get our first deployment to Heroku to work.

<details><summary><b>Heroku Step 21</b></summary>

</details><br />

22. Let's head back to our settings.py file on Gitpod. We now need to add our Cloudinary Libraries we installed earlier to the installed apps. Here it is important to get the order correct.

<details><summary><b>Heroku Step 22</b></summary>

</details><br />

23. For Django to be able to understand how to use and where to store static files we need to add some extra rows to the settings.py file.

<details><summary><b>Heroku Step 23</b></summary>

</details><br />

24. Hang in there, we have just a couple of steps left. Now it's time to link the file to the Heroku templates directory.

<details><summary><b>Heroku Step 24</b></summary>

</details><br />

25. Let's change the templates directory to TEMPLATES_DIR in the teamplates array.

<details><summary><b>Heroku Step 25</b></summary>

</details><br />

26. To be able to get the application to work through Heroku we also need to add our Heroku app and localhost to which hosts that are allowed.

<details><summary><b>Heroku Step 26</b></summary>

</details><br />

27. Now we just need to add some files to Gitpod.

* Create 3 folders in the top level directory: **media**, **static**, **templates**
* Create a file called **Procfile* and add the line ```web: gunicorn PROJ_NAME.wsgi?``` to it.d

28. Now you can save all the files and prepare for the first commit and push to Github by writing the lines below.

* ```git add .```
* ```git commit -m "Deployment Commit```
* ```git push```

29. Before moving on to the Heroku deployment we just need to add one more thing in the config vars. We need to add "PORT" in the KEY input field and "8000" in the VALUE field. If we don't add this there might be problems with the deployment.

30. Now it's time for deployment. Scroll to the top of the settings page in Heroku and click the 'Deploy' tab. For deployment method, select 'Github'. Search for the repository name you want to deploy and then click connect.

31. Scroll down to the manual deployment section and click 'Deploy Branch'. Hopefully the deployment is successful!

<details><summary><b>Heroku Step 31</b></summary>

</details><br />

The live link to the 'NIGHTWISH Platform' site can be found [here](https://nightwish-blog.herokuapp.com/).

My GitHub repository can be found [here](https://github.com/olleholmgren/nightwish-blog/).

[Back to top](<#table-of-content>)
# Credits
Inspiration regarding structure with table of contents and the ReadMe sections manual testing and deployment are taken from my fellow school mate Marcus Eriksson with his project portfolio work "Review | Alliance".

You can find his project here:
* [Review | Alliance by Marcus Eriksson](https://github.com/worldofmarcus/project-portfolio-4/)

Credits of course goes to my favourite mentor Spencer Barriball as he (with patience) gave me a huge amount of help throughout this entire project

[Back to top](<#table-of-content>)
# Acknowledgements
A huge THANK YOU to my excellent mentor, the wizard of programming: Spencer Barriball at Code Institute.
