# Code Institute Data Centric Development Milestone Project

## What’s Up | Blog

This blog was created to host posts covering a series of different topics, such as travel, lifestyle, food & drink, fashion, and so on. Users can browse through many different posts and engage with them. If registered, users can submit, edit and delete posts published by themselves. It was designed to have a clean and simple navigation, aiming for a smooth user experience. 

## UI/UX

### Project goals

This project is part of my Code Institute Full Stack Software Development studies, specifically the Data Centric Development module. The objective for this milestone project is to "Create a web application that allows users to store and easily access cooking recipes", using the CRUD operations of Create, Read, Update, and Delete for their recipes. The goal of this project is to create, store, edit and delete posts (CRUD). Target audience for this project is people that are interested in topics such as travel, lifestyle, books and movies. Users have the ability to create different categories, expanding the topics for discussion on the blog. 

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
* Be able to create my own profile.
* Be able to add, edit and delete posts to the website.
* Be able to change my profile information.
* Be able to change my password.
* Be able to see a list of my own posts.
* Be able to add a new category.
* Be able to add a comment to a post.
* Be able to like a post if signed in.
* Be able to read other users' comments


### Wireframe 

This site was built on the basis of ideas from initial wireframes created in Figma and exported image files for these can be seen below. Some changes were done as the projectes started to get into shape, for instance the colour of the background is different from the initial idea. 

<details>
<summary>Desktop</summary>
<br>
<p class="align-center">
<img width="700" alt="desktop" src="https://user-images.githubusercontent.com/65717229/157550577-c41ea9a1-0361-44ca-a044-7b5c28b1530e.PNG"></p>
</details>
<br>
<details>
<summary>Tablet</summary>
<br>
<p class="align-center">
  <img width="700" src="https://user-images.githubusercontent.com/65717229/157550403-e90a505a-54e3-4c45-a54d-cd70752a3e63.PNG" alt="tablet">
</p>
</details>
<br>
<details>
<summary>Mobile</summary>
<br>
<p class="align-center">
  <img width="700" src="https://user-images.githubusercontent.com/65717229/157549908-f67ff91d-82e8-4586-aeac-cbb928d6f4ff.PNG" alt="mobile">
</p>
</details>
<br>

### Design 

This site was built using Bootstrap, as well as refactored designs I used in my previous milestones. On the homepage, individual category page and my posts page are displayed as cards that when clicked, lead to the individual post page. 
On the individual post page, users can find the photo, name, bio and social media links to the author of the posts. by clicking on the photo or "Profile" button, the users are directed to a page where they can see the author's full profile. 
The initial idea was to create a site which would be easy to navigate without many painpoints. The user can easily find what they are looking for as well as engage with the posts, by liking or leaving a comment to it. 

### Colour Scheme
Colours are kept to a minimum in order to keep focus on the imagery of the post, chosen colours are various shades of purple. Colour scheme can be found below:

![colour_scheme](https://user-images.githubusercontent.com/65717229/157550822-a0f2f9aa-cc02-44f2-af3d-e6cc1b293dff.PNG)

### Typography
Two Google Fonts were used across the site: 
- [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto)
- [Lato](https://fonts.google.com/specimen/Lato?query=lato) 

###  Media

The images on the blog were from [Pexel](https://www.pexels.com/).


## Features

### Existing Features on every page


**Navbar**

The navigation bar features the blog name in the top left corner, which works as a link to the home page from any other page on the blog. The other navigation links are in the top right. 
For users who visited to site and are not registered/logged in yet, the follow links are visible:

* Home
* Categories
* Login
* Register

<br>
<img width="700" src="https://user-images.githubusercontent.com/65717229/157740977-d28e27a5-bd48-4949-9b23-992e14f52bca.PNG" alt="not logged in navbar">
<br>
<br>

For users who are logged in, the follow links are visible:

* Home
* Categories
* Add Post
* User's name 
    * Profile (the actual profile page)
    * Edit Profile
    * My Posts
    * Settings
    * Logout 

<br>
<img width="700" src="https://user-images.githubusercontent.com/65717229/157741278-a7392e69-6285-42be-a9e2-a07a866eadd3.PNG" alt="not logged in navbar">
<br>
<br>


Python determines if the user is logged in or not by checking if 'user' in session and passes this data to Jinja to display the correct navbar for the user.
On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.

<br>

**Footer**

The footer features some key Information such as copyright information and links to social media platforms.

<img width="700" src="https://user-images.githubusercontent.com/65717229/157741717-b23d3686-2356-4666-9ae6-8a4a91de5adb.PNG" alt="footer">
<br>


### Elements on Multiple Pages
<br>

**Posts Cards** 
(Home, individual category page, my posts page)

It displays the post's image, a small headline of the post, date posted, author of the post and a "Read More" button which directs users to the individual post page. The user can also be directed to that page by clicking on the images. 
On large and medium devices, 3 cards are displayed in a row and on smaller devices, one card per row. If the user hover over the images, they zoom in a little, giving it a bit of effect. 

**Pagination**

(Home, individual category page, my posts page)

Where there are more than six results navigation links to pages are displayed below the number of results (6 results per page).

**Sort into categories**

(Home, categories page, individual category page, post page, my posts page)

One the card, in the home page, it is possible to see the category the post belongs to and by clicking on it, the user is directed to a page with all the posts from that specific category. The same happens on the individual post page and also on the my posts page, which is where a user can see all the posts published by himself/herself.


### Individual Pages

* Post Page

**Edit and Delete post**

If logged in and the author of the post, the user can either edit or delete it, if desired. 

**Like button**

If logged in, the user can like and dislike a post.

**Author Profile**

The user can check the profile of the author of the post, as well as see their social media. 

**Comments**

When logged in, users can leave comments on the posts. Everyone is able to see them, logged in or not.

**edit and delete post**

The owner of the post has the power to edit and delete it, if desired.

* Login
This section contains a form where users may login and be redirected to Home Page. Below the form, the user can find a link to register.

* Logout
Clicking 'Logout' ends a user session and redirects them to the 'Home' page.

* Register
This section contains a registration form.Once it is completed, they will be redirected to the login page where they can then sign in.

* User Profile

It contains a profile image, the user first and last name, their email, bio and a link to their social media.

* Edit Profile

The owner of the profile can edit it, for instance change the profile image or the information provided in the bio. 

* Settings
On this page, the user can change their first and last name, email, and password. 

* My Post
This page displays as posts published by the user, who is logged in. if there are no posts, there is a message and a button directing them to the add post page. 

* Add Post
Users who are registered can create their own post.

* Categories
Users can see all the existing categories and if needed, add a new one. For instance, pets.

* Admin Superuser

-   My 'Admin' profile has several extra features, which currently include:
-   Edit / Delete any post from the database.
-   Edit / Delete any comment from the database.
-   Edit / Delete any users/profile from the database.


### Future Features

* make it possible for users to edit and delete comments.
* Have a "favourites" area where users can add their favourite posts.

### Database
This website have 4 databases, 1 for user profile, 1 for posts, 1 for comments and 1 for the categories. they are connected to some extend to each other as well as being used to store various calculations, and store all general information on the page. 

- Profile Database
- Post Database 
- Categories
- Comment Database

**Profile database explained**
User: Stores the chosen username added by the user.
First_name: Stores the user's first name.
Last_name: Stores the user's last name.
Email: Stores the email address added by the user.
Bio: Stores the bio added by the user to the profile.
Profile_Pic: Stores the profile picture uploaded by the user. If none is uploaded by the user, a default images will be added instead. 
Instagram_url: Store the url of the user's instragram account
Facebook_url: Store the url of the user's facebook account
Twitter_url: Store the url of the user's Twitter account

**Post database explained**
Post_title: Stores the title of the blog post. 
Author: Stores the name of the user who created a post. 
Created_on: Stores when a post was created.
Content: Stores the actual content of the blog post. 
Category: Stores which category the post belongs to.
Likes: Stores the likes a post recieved.
Image: Stores the image related to the post. If no images is uploaded, a default one will be applied. 

**Categories database explained**
name: It is the category name. Example: LifeStyle.

**Comment database explained**
Post: Stores which is the post which the comment should be added to. 
Name: Stores the name of the user who made the comment. 
Body: Stores the actual comment.
Date_added: Stores when the comment was created. 


### Technologies Used

- HTML5 - Used as the base for markup text.
- CSS3 - Used as the base for cascading styles.
- Bootstrap - Used to simplify the structure of the website and make the website responsive easily.

### Back-End Technologies

- Python 3.6.7 - Used as the back-end programming language.
- Django 2.2.16 - Used as my Python web framework.
- Heroku - Used for "Platform as a Service" (PaaS) for app hosting.
- PostgreSQL 11.4 - Used as relational SQL database plugin via Heroku.

### Frameworks, Libraries, & Programs Used

- Many different Django libraries were used:
    - django.shortcuts, django.views.generic, django.urls,django.http, among many others.
- For the textarea ckeditor was used. 

Further details on all Python packages used on this project can be found in the requirements.txt file.

### Credits

**Resources Used**

- MDN General Web Docs: For semantic structure reference, arrays, localStorage, fetch.
- W3Schools.com: For html/css/js general reference, semantic structure reference, arrays, localStorage.
- Django Tutorial : 
    - [Django Model](https://www.geeksforgeeks.org/django-model-data-types-and-fields-list/#:~:text=Basic%20model%20data%20types%20and%20fields%20list%20,raw%20binary%20data.%20%2021%20more%20rows%20)
    - [Django Project](https://docs.djangoproject.com/en/4.0/)
    - [Ask Python](https://www.askpython.com/django/django-blog-app)

**Content**

All the posts from the website have the name of the original author as well as a link to the original post on the bottom of each post. This blog was only done for educational purposes. 

### Testing

### Validators and linters

- W3C HTML Validator Passed tests without issues
- W3C CSS Validator Passed tests without issues
- CSS Lint VSCode extension
- PEP8 and AUTOPEP8. Online PEP8 warns about lines being too long but when I attempted to fix that
  AUTOPEP8 would break the code, otherwise no issues.

### Manual Testing

Extensively used Crome Developer tools to test form submissions through network tab etc.

1. Visiting page

    - Test if navigation bar works correctly on phone, tablet and desktop browsers.
    - Test if page is responsive at all sizes.
    - Test footer social icon links (links open homepages in a new window).
    - Test If I see the different posts on the home page (Pagination).
    - Test if I could go to each post individually, by clicking on the image or "Read More" button.

2. Sign Up

    - Try registering with empty form/inputs (shows tooltip "Please fill out this field")
    
    <img width="380" alt="fillin-form" src="https://user-images.githubusercontent.com/65717229/157551573-7e03c92a-5ecb-4f01-bfe4-632ab8dd7baf.PNG">
     

    - Try to register with invalid email or not email at all ("Please include a "@" in the email address" or "Please fill out this field")
    
    <img width="380" alt="email-error" src="https://user-images.githubusercontent.com/65717229/157551420-76787c9c-04e6-4552-9dd5-660672684d37.PNG">
    
    
    - Attempt to use username/password that is too long or too short ("There was an error with your form!")

3. Login

    - Try leaving fields empty (message "There was an error with your form...Please try again")
    - Typed the wrong username or password (message "There was an error with your form...Please try again" )

4. Create  Profile

    - Try leaving the form empty. A default image will be added to the profile image.
    - Try not to add all the social media links. It will be displayed in the profile page only the ones added. 
    - Try to create a profile without being logged in (Message "You need to login to be able to create a profile")

5. Edit Profile

    - Test if it is possible to edit an existing profile.
    - Check if changes were effective.
    - try to edit a post without being logged in (Message "You need to login to be able to edit your profile. Login here")

6. Settings

    - Try to update the user's first name. 
    - Check if the change was effective.
    - Try to change the password, once it is done a successful message will pop up.
    - Test if the passwords do not match.(Message "The two password fields didn’t match.")
    - Try inserting the wrong "old password". (Message "Your old password was entered incorrectly. Please enter it again.")

7. Add Post

    - Log in
    - Go to the "Add Post" page
    - Try to submit an empty form and verify that no post has been added to any category page.The page just reloads and will not submit the form until it is filled in.
    - Try to submit a filled out form and verify that fields appear correctly, there is no missing information.
    - Try not to add any image to the post. A default image is added as a placeholder. 
    - Try to add a post without being logged in (Message "You need to login to be able to add a post. Log in here")

8. Edit and Delete Post

    - Try to edit a post published by me.
    - Try to delete a post published by me. 
    - Check if changes have been made and displayed correctly.
    - Try to edit or delete a post while not logged in. (Message "You need to login to be able to edit/delete a post. Log in here" )

9. My Posts page

    - Try to check if all the posts from the user who is logged in are on one page.
    - Try to check the "My Posts" page without having any posts. (Message "You do not have any post yet")
    - Try to go to "My Posts" without being logged in. (Message "You are not authorised to view this page")

10. Categories

    - Try to sort all the posts from the same category, without being logged in and when logged in. 
    - Try to see all the categories without being logged in.
    - Try to add a category and see if it appears.
    - Try to add a category without being logged in. 

11. Comment

    - Try to see the comments without being logged in.
    - Try to add a comment while logged in and see the comment on the post page.
    - Try to add a comment without being logged in. 

### Deployment

The website can be accessed [here]().

Deployment instructions assume that you have already set up your repository and basic flask application. The website is deployed on the Heroku cloud platform using the following steps:

    1. Create the necessary files for deployment
    2. Create requirements file using pip3 freeze > requirements.txt which will contain the required dependencies.
    3. Create Procfile using echo web: python app.py > Procfile.
    4. Push both files to GitHub
    5. Login to Heroku and create a new app
    6. Connect the app to your project
    7. Go to the deployment method section and choose the method. If using GitHub, select that option, otherwise use the Heroku CLI method.
    8. Following the GitHub method, search for the desired repository and connect to it
    9. Enter configuration variables
    10. Go to the settings tab and select Reveal Config Vars. Enter the variables defined in the env.py file (IP, PORT and SECRET_KEY).
    11. Deploy and preview
    12. Go back to the deployment tab and enable automatic deployment.
    13. Finally, press deploy branch and preview your website.


### Acknowledgements

A thanks to my friend Authur Pereira Neto for all the support and help throughout this project, and the Slack groups. 

##### Disclaimer

If there are any issues with copyright of content, please contact me. I will fix that as soon as possible. This project is for educational purposes only.

Beatriz Amorim 






