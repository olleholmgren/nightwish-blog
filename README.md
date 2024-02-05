# THE NIGHTWISH PLATFORM #

![MOCKUP](/static/images/mockup.png)

An online interactive fanzine for dedicated fans of the great symphonic metal band

## Purpose
The aim for this project is to create a PLATFORM for NIGHTWISH fans to gather and share thoughts and opinions as well as exchange experiences with each other about NIGHTWISH.

### Goal
As an owner, my goal is to be able to run and maintain a PLATFORM that will use the CRUD(Create, Read, Update, Delete) functionality in order to serve dedicated fans of NIGHTWISH. The user will have the choice of either sign up as a Member to the PLATFORM or to just remain a Guest
This means that the user will be able to: 

## Existing Features

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

## Project Journey

While staring up my blog project, I wanted to have a clear overview of what features and functions I need my PLATFORM in order to have a fully functional PLATFORM.	
After discussing with my fellow classmates at Code Institute it came to my understanding that it is a very good idea to start with a sketch or flowchart. So I started to create the Use Case Diagram as visible below:	

## Use Case Diagram

I made this Use Case Diagram mostly in order to get the broader picture of what the actual product will have in terms of features for the:
- Admin
- Member
- Guest

![UCD](https://github.com/olleholmgren/nightwish-blog/assets/114229598/f24f5b27-b4c4-44ea-a8a4-75b32bafc31a)

## Entity Relationship Diagram

For this ERD I used [Lucid Chart](https://www.lucidchart.com/) in order to structure up my database schema.

![ERD](https://github.com/olleholmgren/nightwish-blog/assets/114229598/6b0f5ca1-b78a-4f5f-afdf-377fdc9823a7)

## Wireframe

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

## Agile
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



## Future Features

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

## Project Journey

While staring up my blog project, I wanted to have a clear overview of what features and functions I need my PLATFORM in order to have a fully functional PLATFORM.	
After discussing with my fellow classmates at Code Institute it came to my understanding that it is a very good idea to start with a sketch or flowchart. So I started to create the Use Case Diagram as visible below:	

## Use Case Diagram

I made this Use Case Diagram mostly in order to get the broader picture of what the actual product will have in terms of features for the:
- Admin
- Member
- Guest


## Entity Relationship Diagram

# Testing

### Manual testing throughout the entire website

| Status | ***Website (NIGHTWISH PLATFORM) - User not logged in**
|:-------:|:--------|
| &check; | 
| &check; | Pasting page that needs authentication loads a forbidden page
| &check; | Clicking the website name in nav bar loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page
| &check; | 
| &check; | Clicking the Albums button on the nav bar lists all album reviews
| &check; | Clicking the Concert button on the nav bar lists all concert reviews
| &check; | Clicking the Log In / Sign Up loads the sign up page
| &check; | 6 Reviews are rendered for the user on all / albums / concert page before pagination kicks in
| &check; | Clicking the Read More button on the a review card loads the review detail page
| &check; | In the details view the user cannot create a comment
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window


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

# Deployment

# Credits

Inspiration regarding Manual testing and ReadMe structure are taken from my fellow school mate Marcus Eriksson with his project portfolio work "Review | Alliance":
* [Review | Alliance by Marcus Eriksson](https://github.com/worldofmarcus/project-portfolio-4/)

Credits of course goes to my favourite mentor Spencer Barriball as he (with patience) gave me a huge amount of help throughout this entire project

# Acknowledgements

A huge THANK YOU to my excellent mentor, the wizard of programming: Spencer Barriball at Code Institute.
