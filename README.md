# Code Institute Data-Centric Development Milestone Project

## What’s Up | Blog

This blog was created to host posts covering a series of different topics, such as travel, lifestyle, food & drink, fashion, and so on. Users can browse through many different posts and engage with them. If registered, users can submit, edit and delete posts published by themselves. It was designed to have clean and simple navigation, aiming for a smooth user experience. 

You can view the live site [here](https://travellifestyleblog22.herokuapp.com/)

## UI/UX

### Project goals

This project is part of my Code Institute Full Stack Software Development studies, specifically the Data-Centric Development module. The objective of this milestone project is to create a web application that allows users to store and easily access cooking recipes, using the CRUD operations of Create, Read, Update, and Delete for their recipes. The goal of this project is to create, store, edit and delete posts (CRUD). The target audience for this project is people that are interested in topics such as travel, lifestyle, books and movies. Users can create different categories, expanding the topics for discussion on the blog. 

### User Stories
As a user, I want: 

* Be able to view the site on my preferred device (mobile, tablet, desktop).
* Be able to view all the posts without needing to sign up.
* Be able to see each post individually.
* Be able to choose a category.
* Be able to see all the categories.
* Be able to see the profile of the author of the post.
* Be able to register to the site.
* Be able to sign in and sign out. 
* Be able to create my profile.
* Be able to add, edit and delete posts to the website.
* Be able to change my profile information.
* Be able to change my password.
* Be able to see a list of my posts.
* Be able to add a new category.
* Be able to add a comment to a post.
* Be able to like a post if signed in.
* Be able to read other users' comments


### Wireframe 

This site was built based on ideas from initial wireframes created in Figma and exported image files for these can be seen below. Some changes were done as the projects started to get into shape, for instance, the colour of the background is different from the initial idea. 

**Tablet and Mobile**

![Wireframe- tablet and mobile](https://user-images.githubusercontent.com/65717229/158603516-b8760174-0f04-4ae1-8765-5bc600861e07.png)


**Desktop**

<img width="500" src="https://user-images.githubusercontent.com/65717229/158603412-10817e70-7db2-44fc-9181-21f37becf6d7.png" alt="Wireframe- desktop">

***Figma Wireframe**

<img width="552" alt="wireframe-figma" src="https://user-images.githubusercontent.com/65717229/158605393-25fe2fce-7282-45e0-a6d1-4c3465c30e69.PNG">

### Design 
This site was built using Bootstrap, as well as refactored designs I used in my previous milestones. On the homepage, the individual category page and my posts page are displayed as cards that when clicked, lead to the individual post page. 
On the individual post page, users can find the photo, name, bio and social media links to the author of the posts. by clicking on the photo or "Profile" button, the users are directed to a page where they can see the author's full profile. 
The initial idea was to create a site that would be easy to navigate without any pain points. The user can easily find what they are looking for as well as engage with the posts, by liking or leaving a comment on them. 

### Colour Scheme
Colours are kept to a minimum to keep the focus on the imagery of the post, chosen colours were based on the hero image. The Colour scheme can be found below:

![colour_scheme](https://user-images.githubusercontent.com/65717229/158066980-21028c56-d426-453c-83cd-52559dac98ab.PNG)

### Typography
Google Fonts used across the site: 
- [Montserrat](https://fonts.google.com/specimen/Montserrat?query=mont)
- [Comfortaa](https://fonts.google.com/specimen/Comfortaa?preview.text=What%27s%20up%20&preview.text_type=custom)

###  Media
The images on the blog were from [Pexel](https://www.pexels.com/).

## Features

### Existing Features on every page

**Navbar**

The navigation bar features the blog name in the top left corner, which works as a link to the home page from any other page on the blog. The other navigation links are in the top right. 
For users who visited the site and are not registered/logged in yet, the following links are visible:

* Home
* Categories
* Login
* Register

<img width="500" src="https://user-images.githubusercontent.com/65717229/158068621-2d679857-dbfc-4c12-b162-a94484937852.PNG" alt="not logged in navbar">

For users who are logged in, the following links are visible:

* Home
* Categories
* Add Post
* User's name 
    * Profile (the actual profile page)
    * Edit Profile
    * My Posts
    * Settings
    * Logout 

<img width="500" src="https://user-images.githubusercontent.com/65717229/158068642-60da9b2f-4636-4209-87f7-1a752cfe7e0e.PNG" alt="logged in navbar">


Python determines if the user is logged in or not by checking if 'user' is in session and passes this data to Jinja to display the correct navbar for the user.
On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide-out menu opens when the burger icon is clicked.

<img width="500" src="https://user-images.githubusercontent.com/65717229/158069792-6af5848c-11e0-4f87-ac28-8b5d47684496.PNG" alt="hambuger navbar">


**Footer**

The footer features some key Information such as copyright information and links to social media platforms.

<img width="500" src="https://user-images.githubusercontent.com/65717229/158068681-dee6ad4c-f9b9-4cbd-956a-563b0329b498.PNG" alt="footer">


### Elements on Multiple Pages

**Posts Cards** 

(Home, individual category page, my posts page)

-   It displays the post's image, the post category, a small headline of the post, and the date on which it was posted. The user can read the whole post by clicking on the image or the post name.

<img width="500" alt="post-card" src="https://user-images.githubusercontent.com/65717229/158068746-9fbe3bd4-796f-493a-b4af-b9296e2dbdf9.PNG">


**Pagination**

(Home, individual category page, my posts page)

- Where there are more than six results, navigation links to pages are displayed below the number of results (6 results per page).

<img width="500"  alt="pagination-homepage" src="https://user-images.githubusercontent.com/65717229/158068759-8aba7919-67bd-45a4-89a9-d6a4d30c90dd.PNG">

**Sort into categories**

(Home, categories page, individual category page, post page, my posts page)

- On the card, on the home page, it is possible to see the category the post belongs to and by clicking on it, the user is directed to a page with all the posts from that specific category. The same happens on the individual post page and also on my posts page, which is where a user can see all the posts published by himself/herself.

<img width="500"  alt="categories" src="https://user-images.githubusercontent.com/65717229/158068780-73338ec0-009b-4498-8a4a-f1c10ecf0304.PNG">


### Individual Pages

### Post Page

**Individual Post Page**
- if the users click on the image or the post title, they will be directed to the individual post page, where they can read the full post. 

<img width="500" alt="post" src="https://user-images.githubusercontent.com/65717229/158068839-cf856fd6-f93f-4c56-8bb5-e53cfd1249f6.PNG">

**Edit and Delete post**

- If logged in and the author of the post, the user can either edit or delete it, if desired. 

<img width="500" alt="add-edit-delete-btn" src="https://user-images.githubusercontent.com/65717229/158068950-0c22af61-3cea-4be8-abeb-78a76f9513be.PNG">
<img width="500" alt="edit-post" src="https://user-images.githubusercontent.com/65717229/158069645-919590d7-c9fc-42ad-92c1-82d5b14844f6.PNG">
<img width="500" alt="delete-post" src="https://user-images.githubusercontent.com/65717229/158069659-445ff5a7-ddb3-405e-ba30-2c723b325469.PNG">


**Like button**

- If logged in, the user can like and dislike a post.

<img width="500"  alt="like" src="https://user-images.githubusercontent.com/65717229/158068956-b0ba8962-c081-4a8d-929c-fb420df9d301.PNG">

**Author Profile**

- The user can check the profile of the author of the post, as well as see their social media. 

<img width="500"  alt="authoer-card" src="https://user-images.githubusercontent.com/65717229/158069005-01c52e22-60e9-4d88-8a7f-49cb55605898.PNG">


**Comments**

- When logged in, users can leave comments on the posts. Everyone can see them, log in or not.

<img width="500"  alt="comments" src="https://user-images.githubusercontent.com/65717229/158069298-6e64d93a-8468-45b3-8a52-5ab9014b9a86.PNG">


### Login Page
- This section contains a form where users may log in and be redirected to the Home Page. Below the form, the user can find a link to register.

<img width="500" alt="login" src="https://user-images.githubusercontent.com/65717229/158069311-f753376c-8e59-42c1-8478-771a0cf8e007.PNG">


### Logout
- Clicking 'Logout' ends a user session and redirects them to the 'Home' page.

### Register Page
- This section contains a registration form. Once it is completed, they will be redirected to the login page where they can then sign in.

<img width="500"  alt="register" src="https://user-images.githubusercontent.com/65717229/158069320-657b6016-fdd5-4766-a2a5-a0aa9f7e9af3.PNG">

### User Profile Page

It contains a profile image, the user's first and last name, their email, bio and a link to their social media.

<img width="500" alt="profile" src="https://user-images.githubusercontent.com/65717229/158069371-eb34de0f-e2ea-4fe0-8a60-3e3697a59ebe.PNG">

### Create a User Profile page

Once users create an account, they can create a profile.

<img width="500" alt="profile" src="https://user-images.githubusercontent.com/65717229/158069860-d085e4fc-1a43-443f-8f73-a50e8afb5d8c.PNG">

### Edit Profile Page

The owner of the profile can edit it, for instance, change the profile image or the information provided in the bio. 

<img width="500" alt="edit-pro" src="https://user-images.githubusercontent.com/65717229/158069387-b49f4915-ddfa-48e1-a7a7-afca729e9650.PNG">

### Settings

On this page, the user can change their first and last name, email, and password. 

<img width="500" alt="setting" src="https://user-images.githubusercontent.com/65717229/158069403-09a2a589-0ded-4ea4-8131-6a199188366f.PNG">

<img width="500"  alt="change-password" src="https://user-images.githubusercontent.com/65717229/158070956-f8b79530-ed1b-4ecc-9d09-7f003456a621.PNG">


### My Posts Page

This page displays as posts published by the user, who is logged in. if there are no posts, a message and a button is directing them to the add post page. 

<img width="500" alt="myposts" src="https://user-images.githubusercontent.com/65717229/158069429-88bd5027-d7e6-429e-b740-b88bd125be53.PNG">

### Add Post Page

Users who are registered can create their posts.

<img width="500" alt="add-post" src="https://user-images.githubusercontent.com/65717229/158069440-1e749af1-e3e8-4774-a39e-8c9a339381d8.PNG">

### Categories Page

Users can see all the existing categories and if needed, add a new one. For instance, pets.

<img width="500" alt="categories-list" src="https://user-images.githubusercontent.com/65717229/158069453-96c42a43-cc76-4434-86a0-65720b45b745.PNG">

### Add Categories Page

Users can add new categories if they see necessary.

<img width="500" alt="categories-list" src="https://user-images.githubusercontent.com/65717229/158069928-3cad7e6a-ed87-4744-b71a-5e6eb921ef6d.PNG">


**Admin Superuser**

-   My 'Admin' profile has several extra features, which currently include:
-   Edit / Delete any post from the database.
-   Edit / Delete any comment from the database.
-   Edit / Delete any users/profiles from the database.

## Future Features

* make it possible for users to edit and delete comments.
* Have a "favourites" area where users can add their favourite posts.

## Models
This website has one Postgres database with a number of collections or data models. The models are connected to some extent to each other as well as being used to store various calculations and store all general information on the page. 

 **Profile model**

- User: Stores the chosen username added by the user.
- First_name: Stores the user's first name.
- Last_name: Stores the user's last name.
- Email: Stores the email address added by the user.
- Bio: Stores the bio added by the user to the profile.
- Profile_pic: Stores the profile picture uploaded by the user. If none is uploaded by the user, a default image will be added instead. 
- Instagram_url: Store the URL of the user's Instagram account.
- Facebook_url: Store the URL of the user's Facebook account.
- Twitter_url: Store the URL of the user's Twitter account
- Pinterest_url: Store the URL of the user's Pinterest account

**Post model**

  - Post_title: Stores the title of the blog post.
  - Author: Stores the name of the user who created a post. 
  - Created_on: Stores when a post was created.
  - Content: Stores the actual content of the blog post. 
  - Category: Stores which category the post belongs to.
  - Likes: Stores the likes a post received.
  - Image: Stores the image related to the post. If no images are uploaded, a default one will be applied. 

**Categories model**

  - name: It is the category name. Example: LifeStyle.

**Comment model**

  - Post: Stores which is the post to which the comment should be added. 
  - Name: Stores the name of the user who commented. 
  - Body: Stores the actual comment.
  - Date_added: Stores when the comment was created. 


### Technologies Used

- HTML5 - Used as the base for markup text.
- CSS3 - Used as the base for cascading styles.
- Bootstrap - Used to simplify the structure of the website and make the website responsive easily.

### Back-End Technologies

- Python 3.6.7 - Used as the back-end programming language.
- Django 2.2.16 - Used as my Python web framework.
- Heroku - Used for "Platform as a Service" (PaaS) for app hosting.
- PostgreSQL 11.4 - Used as a relational SQL database plugin via Heroku.

### Frameworks, Libraries, & Programs Used

- Many different Django libraries were used:
    - Django. shortcuts, Django. views.generic, Django.URLs, Django. HTTP, among many others.
- For the textarea, CKEditor was used. 

Further details on all Python packages used on this project can be found in the requirements.txt file.

## Credits

### Resources Used

- MDN General Web Docs: For semantic structure reference, arrays, localStorage, fetch.
- W3Schools.com: For html/css/js general reference, semantic structure reference, arrays, localStorage.
- Django Tutorial : 
    - [Django Model](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/#:~:text=Basic%20model%20data%20types%20and%20fields%20list%20,raw%20binary%20data.%20%2021%20more%20rows%20)
    - [Django Project](https://docs.djangoproject.com/en/4.0/)
    - [Ask Python](https://www.askpython.com/django/django-blog-app)
    - [Django Central](https://djangocentral.com/building-a-blog-application-with-django/)
- [Social Media Icons](https://icons8.com/icon)

### Content

All the posts from the website have the name of the original author as well as a link to the original post at the bottom of each post. This blog was only done for educational purposes. 

## Testing

The testing can be seen [here](tests.md).

### Deployment

The website can be accessed [here](https://travellifestyleblog22.herokuapp.com/).

Deployment instructions assume that you have already set up your repository and basic Django application. The website is deployed on the Heroku cloud platform using the following steps:

- To run this project locally, you will need to clone the repository.
- Login to GitHub (https://wwww.github.com)
- Select the repository biareiam/travellifestyleblog
- Click the “Code” button and copy the HTTPS URL, for example, https://github.com/biareiam/travellifestyleblog.git
- In your IDE, open a terminal and run the git clone command:
- git clone https://github.com/biareiam/travellifestyleblog.git
- The repository will now be cloned in your workspace.
- Create an env.py file in the root folder in your project, and add the following code with the relevant key, value pairs, and ensure you enter the correct key values.
- Add to the env.py file: 
   import os
   os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
   os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
- Install the relevant packages as per the requirements.txt file
- Start the application by running "python3 manage.py runserver" 

#### Heroku

- To deploy this application to Heroku, run the following steps.
- In the app.py file, ensure that debug is not enabled, i.e. set to True
- Create a file called ProcFile in the root directory, and add the line - “web: gunicorn PROJ_NAME.wsgi”. If this file already exists, just go to the next step.
- Run the command “pip freeze > requirements.txt” to create a requirements.txt file in your terminal if the file doesn't already exist.
- Both the ProcFile and requirements.txt files should be added to your git repo in the root directory
- Create an account on heroku.com
- Create a new application and give it a unique name
- In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo
- Select the branch, for example, master and enable automatic deploys if desired. Otherwise, deployment will be manual
- The next step is to set the config variables in the Settings section
- Set key/value pairs for the following keys: DATABASE_URL, SECRET_KEY
- Go to the dashboard and trigger a deployment - “deploy branch”
- This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app
- If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

Note: 
- If Heroku can not be connected to gitpod. On the terminal, type “Heroku login -i”.
- Your Heroku email and password will be requested.
- Once it is done, type “ Heroku git:remote -a travellifestyleblog22”.
- The next step is to push it to Heroku by typing “ git push Heroku main”. 
- If you encounter any issues accessing the build logs is a good way to troubleshoot the issue


### Acknowledgements

Thanks to my friend Authur Pereira Neto for all the support and help throughout this project, and the Slack groups. 

#### Disclaimer

If there are any issues with the copyright of the content, please contact me. I will fix that as soon as possible. This project is for educational purposes only.

Beatriz Amorim 
