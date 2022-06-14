# Code Institute Data-Centric Development Milestone Project

## What’s Up | Blog

This blog was created to host posts covering a series of different topics, such as travel, lifestyle, food & drink, fashion, and so on. Users can browse through many different posts and engage with them. If registered, users can submit, edit and delete posts published by themselves. It was designed to have clean and simple navigation, aiming for a smooth user experience. 

You can view the live site [here](https://travellifestyleblog22.herokuapp.com/)

## UI/UX

### Project goals

This project is part of my Code Institute Full Stack Software Development studies, specifically the Data-Centric Development module. The objective for this milestone project is to create a web application that allows users to store and easily access cooking recipes, using the CRUD operations of Create, Read, Update, and Delete for their recipes. The goal of this project is to create, store, edit and delete posts (CRUD). The target audience for this project is people that are interested in topics such as travel, lifestyle, books and movies. Users can create different categories, expanding the topics for discussion on the blog. 

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

**Tablet and Mobie**

![Wireframe- tablet and mobile](https://user-images.githubusercontent.com/65717229/158603516-b8760174-0f04-4ae1-8765-5bc600861e07.png)


**Desktop**

<img width="500" src="https://user-images.githubusercontent.com/65717229/158603412-10817e70-7db2-44fc-9181-21f37becf6d7.png" alt="Wireframe- desktop">

***Figma Wireframe**

<img width="552" alt="wireframe-figma" src="https://user-images.githubusercontent.com/65717229/158605393-25fe2fce-7282-45e0-a6d1-4c3465c30e69.PNG">

### Design 
This site was built using Bootstrap, as well as refactored designs I used in my previous milestones. On the homepage, the individual category page and my posts page are displayed as cards that when clicked, lead to the individual post page. 
On the individual post page, users can find the photo, name, bio and social media links to the author of the posts. by clicking on the photo or "Profile" button, the users are directed to a page where they can see the author's full profile. 
The initial idea was to create a site that would be easy to navigate without any pain points. The user can easily find what they are looking for as well as engage with the posts, by liking or leaving a comment to them. 

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
This website has one postgres database with a number of collections or data models.The models  are connected to some extent to each other as well as being used to store various calculations, and store all general information on the page. 

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

All the posts from the website have the name of the original author as well as a link to the original post on the bottom of each post. This blog was only done for educational purposes. 

## Testing

### Validators

## Validators

  * W3C HTML Validator Passed tests without issues
  * W3C CSS Validator Passed tests without issues
  * PEP8 and AUTOPEP8. Online PEP8  previously warned about lines being too long and it was FIXED. No errors should be displayed. 
  * Lighthouse:

<img width="500" alt="lighthouse-test" src="https://user-images.githubusercontent.com/65717229/159161401-c3ab6e39-386f-42db-ab67-cbf3b5ef7a43.PNG">

### [Manual Testing]

Extensively used Chrome Developer tools to test form submissions through network tab etc.

# Tests

The testing approach will be described in detail in this section.
 
## Manual testing information:

  * Testing was completed on the following browsers and device types:
  * Browsers: Safari, Chrome, IE Edge, Mozilla Firefox and Chrome Emulator.
  * Devices: Mobile, tablet and desktop.
 
## User stories and tests 

### Feature 1 Navigation Bar

01 - User story:
* As an admin/ user, while not logged in, I would like to see the navigation bar displayed with a logo on all pages for easy navigation, redirecting to the home, on the different devices.

Test case: 
* Navigate to the home/index page on desktop, tablet and mobile.  

Expected result : 
* Be able to see the full navigation bar in different devices. 

Results: 
 Desktop

 ![Desktop](https://user-images.githubusercontent.com/65717229/170710769-78055156-f0fa-4931-a376-55127fe39118.PNG)

 Tablet 

 ![Tablet](https://user-images.githubusercontent.com/65717229/170710991-ca7968eb-f86e-4b0c-a663-a7db462abb65.PNG)

 Mobile 

 ![Mobile](https://user-images.githubusercontent.com/65717229/170711132-0b2688f6-beaf-4b03-ad1a-d642212a410f.PNG)


02 - User story:
* As an admin/regular user, while logged in, I would like to see the navigation bar displayed with a logo on all pages for easy navigation, redirecting to the home, on the different devices. As well as the other features available to logged in members. 

Test case:  
* Navigate to the home page after logged in.
* See the links displayed to members who are logged in.

Expected result: 
* Be able to see all the links available to a person who is logged in the navigation bar, such as add a post and profile. 

Results: 
 Desktop

 ![loged in - desktop](https://user-images.githubusercontent.com/65717229/170711636-1ac5fb0f-e435-44df-b4d7-267dae5228a6.PNG)

 Tablet

 ![loged in - tablet](https://user-images.githubusercontent.com/65717229/170711643-00129cac-b3c3-4baa-b1b9-7d6da6ba2b10.PNG)

 Mobile

 ![loged in - mobile](https://user-images.githubusercontent.com/65717229/170711640-84648a3e-53ec-4a0d-bf7c-c307e3b89917.PNG)


### Feature 2 Login Register Logout administration

03 - User Story:
* As a regular user I can register for an account by providing my username, password, confirm password, first name, last name, and email. Once it is done, be redirected to the login page. 

Test case: 
* As a regular user, navigate to the register page from the home page and create an account. 

Expected result:
* Be able to successfully register to the blog and be notified of it. 

Result: 

 ![success - desktop](https://user-images.githubusercontent.com/65717229/170715699-2f048b1e-89dd-488e-addf-3acc637ba2b4.PNG)
 ![success - tablet](https://user-images.githubusercontent.com/65717229/170715695-28517919-b0d9-467a-a5cb-39ada5a726db.PNG)
 ![success - mobile](https://user-images.githubusercontent.com/65717229/170715691-d2d256c5-67a2-4f0f-b811-3cfb235adc6c.PNG)


04 - User Story:
* As a regular user I will be notified if I did not fill one of the fields or if I entered any wrong information. 

Test case:  
* Enter my email with the “@”  and click register. 
* Do not enter an email and click on the register.
* Enter a username which already exists and click register. 
* Do not enter a user name and click register.
* Do not enter a first name or last name and click on register.
* Enter passwords which do not match. 

Expected result: 
* In all these cases, the user is notified that something went wrong or an information is missing. 

Results:

  Already a user:

  ![already user - desktop](https://user-images.githubusercontent.com/65717229/170713987-c1a857c1-76a1-4190-b36c-8bd314bdfc52.PNG)
  ![already user - tablet](https://user-images.githubusercontent.com/65717229/170713983-daee3263-37c7-4f58-af19-d8cad020b69d.PNG)
  ![already user - mobile](https://user-images.githubusercontent.com/65717229/170713979-db27d5f5-339f-47cc-95d0-9806b65983a3.PNG)

  Missing "@" on the email:

  ![resgister no @ - desktop](https://user-images.githubusercontent.com/65717229/170714132-c9c17a6f-698b-47c3-8056-738df54e522c.png)
  ![resgister no @ - tablet](https://user-images.githubusercontent.com/65717229/170714124-6f46f8d4-73f8-4e11-9ece-9b8e7432ff98.png)
  ![resgister no @ - mobile](https://user-images.githubusercontent.com/65717229/170714135-1a6d6df0-824c-4fd7-b346-56d63763b319.png)


  Do not enter an username:

  ![username missing - desktop](https://user-images.githubusercontent.com/65717229/170714306-24cf532f-1925-45a6-af4d-f9241baaf9a8.PNG)
  ![username missing - tablet](https://user-images.githubusercontent.com/65717229/170714310-e8a8f617-0072-49bd-8161-a8c723354a75.PNG)
  ![username missing  - mobile](https://user-images.githubusercontent.com/65717229/170714313-3174c629-3acf-4d34-b33a-bc626c7aead1.PNG)

  Password do not match or do not fullfil the requirement:

  ![password not matching - desktop](https://user-images.githubusercontent.com/65717229/170714421-a76a59e9-90f9-4d74-823e-b8a8367b39b4.png)
  ![password not matching - tablet](https://user-images.githubusercontent.com/65717229/170714429-2b66dded-da30-4b34-a168-6d3662f1031c.png)
  ![password not matching  - mobile](https://user-images.githubusercontent.com/65717229/170714434-738b44ff-a0cf-4aa2-8fe7-d08d9efe0a49.png)

  Missing password:

  ![missing password - desktop](https://user-images.githubusercontent.com/65717229/170714497-dd023809-2d5b-4a99-9ec1-996806670263.png)
  ![missing password - tablet](https://user-images.githubusercontent.com/65717229/170714510-aac9dcc4-f3df-4e6f-b507-3a930380d718.png)
  ![missing password - mobile](https://user-images.githubusercontent.com/65717229/170714505-5880d8ab-17fc-4543-9919-174a7ba00796.png)

05 - User Story:
* As a regular user/admin user I can log in to my account by providing my username and password and clicking Login and I will be navigated to the home page. A username and password must be provided. If the username and/or password entered is incorrectly a relevant message will be displayed 

Test case:  
* Navigate to the login page and click the Login button.
* Enter a username and/or password that does not exist
* Enter a valid username and password

Expected results:

* An error message is displayed that both the username and password fields must be entered, if not filled in. 
* An error message is displayed if the username or password are incorrect or if the user does not have an account. 
* The user is successfully logged in and is brought to the memories page
 
 
Result :

 Login form

 ![login - desktop](https://user-images.githubusercontent.com/65717229/170716116-b960de91-f911-433e-8206-7c639cdeeeab.PNG)
 ![login - tablet](https://user-images.githubusercontent.com/65717229/170716122-90cfd3ad-b68d-44b3-af81-8012ab2b51c2.PNG)
 ![login - mobile](https://user-images.githubusercontent.com/65717229/170716125-e4d94e4a-9375-4928-87fa-ea805cf39f82.PNG)

 Logged in

 ![login - mobile](https://user-images.githubusercontent.com/65717229/170716455-df1b5d3c-e051-4041-9b63-87b15a7f0e64.PNG)
 ![login - tablet](https://user-images.githubusercontent.com/65717229/170716470-35c52998-af12-40a1-b79a-5f0bb5d84eb3.PNG)
 ![login - desktop](https://user-images.githubusercontent.com/65717229/170716464-f0cdec71-c688-460f-a910-6dc6f5b20ab4.PNG)


### Feature 3 Profile/settings

06 - User Story:
As an admin/regular user, when I am logged into the site for the first time, I can create a profile.

Test case: 
* As an admin/regular user logged in for the first time, and through the navigation bar can create a profile.
* As an admin/regular user I choose not to add a profile image or I forgot to add one. 

Expected result: 
* New user can successfully create a profile, with a bio, image and add links to social media, if desired. If a profile image is not provided, a default one will be add instead.  

Result:
 Create a profile - Navigation bar:

 ![login - desktop](https://user-images.githubusercontent.com/65717229/170717302-6fa3d125-f72f-4623-91f4-c0439ed74f85.PNG)
 ![login - tablet](https://user-images.githubusercontent.com/65717229/170717305-8472d0d0-1b66-4847-9e9c-9647c66cfb2a.PNG)
 ![login - mobile](https://user-images.githubusercontent.com/65717229/170717296-2143103a-6cd9-4648-b812-7261c4fdfce3.PNG)

 Create a profile form:

 ![create - desktop](https://user-images.githubusercontent.com/65717229/170717489-c1aa0476-d154-49fa-a951-309e683d5f13.png)
 ![create - tablet](https://user-images.githubusercontent.com/65717229/170717485-916e9085-42cb-413a-bb90-1aa7d97f9aaf.png)
 ![create - mobile](https://user-images.githubusercontent.com/65717229/170717480-40d92eb6-3bf2-405f-a3cc-4daf5228f093.png)

 Profile without picture:

 ![no photo - desktop](https://user-images.githubusercontent.com/65717229/170717951-b14e5249-acc9-4094-9153-914d1894e325.PNG)
 ![no photo - tablet](https://user-images.githubusercontent.com/65717229/170717956-b45ec607-8641-45e4-8ee0-0b592c04ec58.PNG)
 ![no photo - mobile](https://user-images.githubusercontent.com/65717229/170717960-573420db-90ec-4ff3-ad42-e868f781ea39.PNG)


07.user story:
* As an admin/regular user, when I am logged into the site, I can see and edit my existing profile.

Test case:
* Users can see their own profile. 
* Users can edit their own profile. 
* Users can edit their account settings

Expected result: 
* Users can successfully view their profile and edit the text, social media links and the bio.

Results:
User Profile:

 ![no photo - desktop](https://user-images.githubusercontent.com/65717229/170717951-b14e5249-acc9-4094-9153-914d1894e325.PNG)
 ![no photo - tablet](https://user-images.githubusercontent.com/65717229/170717956-b45ec607-8641-45e4-8ee0-0b592c04ec58.PNG)
 ![no photo - mobile](https://user-images.githubusercontent.com/65717229/170717960-573420db-90ec-4ff3-ad42-e868f781ea39.PNG)

 Edit Profile:
 Before:

 ![edit before](https://user-images.githubusercontent.com/65717229/170719246-a75a1006-7166-408f-a45b-b13e67136fe5.png)
 ![edit before - tablet](https://user-images.githubusercontent.com/65717229/170719237-233038f5-e12e-4304-b67d-eeb39b0a2250.png)
 ![edit before - mobile](https://user-images.githubusercontent.com/65717229/170719243-b517af9b-fc66-4d1e-b449-ac3c52422d75.png)

 - After:

 ![UPDATED DESKTOP](https://user-images.githubusercontent.com/65717229/170719318-d38981cb-feeb-4030-95df-caf145ed66ea.png)
 ![UPDATED tablet](https://user-images.githubusercontent.com/65717229/170719326-a03b85a4-e432-4a8a-a688-d7e94497491a.png)
 ![UPDATED mobile](https://user-images.githubusercontent.com/65717229/170719330-fda07cbd-fac4-45f5-b63b-dae313fa55ad.png)

 Edit Account settings:
 - Before:
 
 ![SETTING DESK](https://user-images.githubusercontent.com/65717229/170719423-9560b179-8166-4412-81c9-e5b343d1d338.png)
 ![SETTING TABLET](https://user-images.githubusercontent.com/65717229/170719432-ead151da-784d-4540-af81-80ba2c4f798b.png)
 ![SETTING MOBILE](https://user-images.githubusercontent.com/65717229/170719429-98084312-ef36-4ed1-8765-fbd4814d3ae4.png)

 - After: 
 ![updated](https://user-images.githubusercontent.com/65717229/170719632-5cabdfef-5902-4a7d-9038-0925d90623ed.PNG)


08. user story:
* As an admin/regular user, when I am logged into the site, I can change my password.

Test case:
* Users can see the settings form and successfully change its password.
* Be notified if passwords do not match. 

Expected result: 
* Users can successfully change the password and be notified of it as well as be notified if anything went wrong. 

Result: 
 Old password is wrong:

 ![wrong old](https://user-images.githubusercontent.com/65717229/170720269-f3552d82-64bd-49e2-bb4a-96e6947abbec.PNG)

 Password changed:

 ![updated password](https://user-images.githubusercontent.com/65717229/170720263-7161928d-945e-4560-a66b-61b42f1eb4fe.PNG)

 Password do not fullfiul the requirements:

 ![not match](https://user-images.githubusercontent.com/65717229/170720507-8c7e8689-b414-4cb4-af0c-4b5b403f1058.PNG)

### Feature 4 Home page

09.  User story:
* As a regular user/admin user, logged in or not, I can view all the posts added on the blog, as well as when it was added, title, a snippet of the post an image and which categories the post belongs to. 

Test case:
* As a regular user/admin I can navigate through the home page and see all the posts, from newest to oldest. 

Results:

 ![home page](https://user-images.githubusercontent.com/65717229/170720860-4b6c7923-2964-4739-81f0-d377c33da87f.png)


10.  User story:
* As a regular user/admin user I can view the posts by filtering it by category.

Test case:
*As a regular user/admin I can navigate through the different categories.

Results:

 ![category](https://user-images.githubusercontent.com/65717229/170721070-bf2b03d3-f112-44b5-a567-1def49b4b529.png)
 
### Feature 5 Post detail page

11. User story:
* As a regular user/admin user I can click on any of the posts and be directed to a page where I can read the whole blog post. 

Test case:  
* User wants to read the entire post, see how it was posted, when it was posted.

Expected result:
* Be able to access the post page.

Results:

![detail](https://user-images.githubusercontent.com/65717229/170721264-7df16950-0359-4947-b0bb-9f8afd4ed693.png)


11. User story:
* As a regular user/admin user I can click on the name or image of the author of the post and see their page.It does not matter if I am logged in or not. 

Test case:  
* Go into one of the posts and check its author.

Expected result: 
* Be able to access the profile of the author of the post. 

Results: 
Author of the post:

![author](https://user-images.githubusercontent.com/65717229/170721546-c65d13d7-2fa6-4b6f-86c2-8df0dc00bf1d.PNG)

Profile of the author:

 ![author profile](https://user-images.githubusercontent.com/65717229/170721552-75ed14fd-bbe2-4f80-bdf9-05e4bba31852.PNG)

12.User story:
* As a regular user/admin user, when logged in, I can leave a comment in one of the posts. 

Test case:  
* Go into one of the posts and leave a comment.

Expected result:
* A comment is added to the chosen post. Displaying the name of the author of the post, the date and the posts itself. 

Result:
 Logged in:

 ![leave comment](https://user-images.githubusercontent.com/65717229/171625063-869af14f-a8e4-4ace-acd3-9e0b1a1c7944.PNG)
 ![my comment](https://user-images.githubusercontent.com/65717229/171625034-c0deb2d6-1be1-4268-b9bb-13fff5371971.PNG)


13. User story:
* As a regular user/admin user, when logged out, I can not leave a comment.

Test case:  
* Try to access to leave a comment on a post.

Expected result:
* Be notified that the user does not log in or does not have an account so a comment can not be created. 

Result:
 Not logged in:

 ![comment](https://user-images.githubusercontent.com/65717229/171625052-6300ae56-f176-470b-b8a1-0faf0741cf21.PNG)


### Feature 6 Add post

14.  User story:
* As a regular user/admin user, when logged in, I can add a new post.

Test case:  
* Go into one of the “add post” page through the navigation bar.
* Create a new post. 

Expected result:
* Post successfully created. 
* If an image is not added, a default one should be added instead. 
* If a category is not chosen, a default one should be applied. 
* Be notified of missing information on the form 

Result: 
 Adding a post:

 ![adding post](https://user-images.githubusercontent.com/65717229/171625948-b8e52d7c-c6dd-478b-90f7-2d0a25cb171d.PNG)
 ![new post](https://user-images.githubusercontent.com/65717229/171626118-ab941039-437b-44c0-bec1-a69d2e951187.PNG)

 Missing Title:

 ![no title](https://user-images.githubusercontent.com/65717229/171626096-1a7b157b-a9a7-4923-be00-2f2b6ef876f6.PNG)

 Missing content: 

 ![no content](https://user-images.githubusercontent.com/65717229/171626104-fe1c2da7-2da1-4e5b-b0d1-f9027e0ce816.PNG)


15. User story:
* As a regular user/admin user, when logged out, I can not access the add post page .

Test case:  
* Try to access the add post page without being logged in or having an account.  

Expected result:
* Be notified that the user do not logged in or do not have an account. 

Result:

 ![add post loggoed out](https://user-images.githubusercontent.com/65717229/171626432-377e26e6-a9bd-4c3e-8e6f-9a0b1079597c.PNG)


### Feature 7 Edit/delete post

16. User story:
* As a regular user/admin user, when logged in, I can edit my own posts.

Test case:  
* Go into one of your own posts and through the post detail page be directed to the edit post page. 
* Be able to edit the test, category and image of the post. 

Expected result:
* Post successfully edit. 
* New image should be displayed.
* New text or category should be displayed.  

Result:
 Edit photo:

 ![edit detail](https://user-images.githubusercontent.com/65717229/171627152-8a0fd14a-ace5-4a73-aac2-63eaf383afed.PNG)
 ![edit](https://user-images.githubusercontent.com/65717229/171627169-4b83a38d-88c6-4506-b2f7-a46588404c61.PNG)
 ![change image](https://user-images.githubusercontent.com/65717229/171627184-a4ecde83-f3b7-4ecc-b351-e1386dc505a0.PNG)

 
17. User story:
*As a regular user/admin user, when logged in, I can delete my own posts.

Test case:  
* Go into one of your own posts and through the post detail page be directed to the delete post page. 
* Delete a post 

Expected result:
*Post successfully deleted.

Resullt:
Delete Post:

 ![delete](https://user-images.githubusercontent.com/65717229/171627306-23153841-6069-48ee-b82f-cdf87ab2b069.PNG)
 ![deleted](https://user-images.githubusercontent.com/65717229/171627313-c9836569-fdb2-4285-8f84-fa7f25c8492b.PNG)


18.User story:
* As a regular user/admin user, when logged out, I can not access the edit or delete post page .

Test case:  
* Try to access the edit/delete without being logged in or having an account.  

Expected result:
* Be notified that the user does not log in or do not have an account as well as that they are not allowed to edit or delete someone else’s post. 

Result:
Not able to delete:

![not delete](https://user-images.githubusercontent.com/65717229/171628143-98ec5c14-98b2-4cb3-bb97-cba8cee4812f.PNG)

Not able to edit:
![not edit](https://user-images.githubusercontent.com/65717229/171628146-1dac4e56-74a9-4630-9a16-7e22d7b5628a.PNG)


### Feature 8 my posts page
19. User story:
* As a regular user/admin user, when logged in, I can see all the posts published by me.

Test case:  
* From a link on the navigation bar go to all my posts. 

Expected result:
* Be able to see all my published posts in one place. 

Results: 
 My posts:

 ![myposts](https://user-images.githubusercontent.com/65717229/171628403-74e7d4a6-dfc0-482c-8898-c061862b3075.PNG)


20. User story:
As a regular user/admin user, when logged out in, I am can see my posts page even if I do not publish any post yet. 

Test case:  
* From a link on the navigation bar go to all my posts. 

Expected result:
* Be able to see all my post page and the message notifying that i do not publish anything yet. 

Result: 
 No posts:

 ![no post](https://user-images.githubusercontent.com/65717229/171628393-16d07332-33c8-4a52-9680-a2b39be8e1bd.PNG)

### Feature 9 add Category  page

21. User story:
* As a regular user/admin user, when logged in or out, I can see all the different categories in one place.

Test case:  
* From a link on the navigation bar go and see all the existing categories and see all the posts from a specific category. 

Expected result:
* Be able to see all the available categories.

Result: 
 All categories:

 ![categories](https://user-images.githubusercontent.com/65717229/171628830-7b8a19ad-7541-439d-bd24-f0a47f3f900a.PNG)

 Speficic category:

 ![category1](https://user-images.githubusercontent.com/65717229/171628827-ff1b3d7f-b5ba-44c8-a800-fba96dc45103.PNG)


22. User story:
* As a regular user/admin user, when logged in , I can add a new category if I need to. 

Test case:  
* From a link on the navigation bar go and see all the existing categories.
* Add a new category. 
* Be notified if the field was not filled in. 

Expected result:
* Be able to add a new category. It will be displayed in the all categories page and on the dropdown from the navigation bar. 
* A message should be displayed if nothing is filled in the form. 

Result: 
 Creating new category:

 ![category new](https://user-images.githubusercontent.com/65717229/171629447-b365689c-f3cb-4fcf-a17f-407c80ac49f9.PNG)
 ![NEW CATEGORY](https://user-images.githubusercontent.com/65717229/171629471-721f6979-66fd-4db4-b87f-d70b712a16af.PNG)
 ![NEW NEW CATEGORY](https://user-images.githubusercontent.com/65717229/171629481-1a75fdbf-cfee-49a3-a6b4-354191437d8d.PNG)

 Missing information:

 ![missing category](https://user-images.githubusercontent.com/65717229/171629462-eec25dfa-a5a5-4d1f-87c2-55dbbcd0c4b4.PNG)


23. User story:
* As a regular user/admin user, when logged out, I can add a new category.

Test case:  
* From a link on the navigation bar go and see all the existing categories. 
* Try to add a new category without logging.

Expected result:
* Messages alert the users that they should have an account or be logging in to be able to add a new category. 

Result:
 Not able to create a new category:
 
 ![NO CATEGORY](https://user-images.githubusercontent.com/65717229/171629491-cac67fd4-a85c-4c22-854e-c5cea61b9399.PNG)

### Deployment

The website can be accessed [here](https://travellifestyleblog22.herokuapp.com/).

Deployment instructions assume that you have already set up your repository and basic django application. The website is deployed on the Heroku cloud platform using the following steps:

- To run this project locally, you will need to clone the repository.
- Login to GitHub (https://wwww.github.com)
- Select the repository biareiam/travellifestyleblog
- Click the “Code” button and copy the HTTPS url, for example: https://github.com/biareiam/travellifestyleblog.git
- In your IDE, open a terminal and run the git clone command:
- git clone https://github.com/biareiam/travellifestyleblog.git
- The repository will now be cloned in your workspace.
- Create an env.py file in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values.
- Add to the env.py file: 
   import os
   os.environ["DATABASE_URL"] = "Paste in Heroku DATABASE_URL Link"
   os.environ["SECRET_KEY"] = "Make up your own randomSecretKey"
- Install the relevant packages as per the requirements.txt file
- Start the application by running python3 manage.py runserver 

#### Heroku

- To deploy this application to Heroku, run the following steps.
- In the app.py file, ensure that debug is not enabled, i.e. set to True
- Create a file called ProcFile in the root directory, and add the line - “web: gunicorn PROJ_NAME.wsgi”. If this file already exists, just go to the next step.
- Run the command “pip freeze > requirements.txt” to create a requirements.txt file in your terminal if the file doesn't already exist.
- Both the ProcFile and requirements.txt files should be added to your git repo in the root directory
- Create an account on heroku.com
- Create a new application and give it a unique name
- In the application dashboard, navigate to the deploy section and connect your application to your git repo, by selecting your repo
- Select the branch, for example, master and enable automatic deploys if desired. Otherwise, a deployment will be manual
- The next step is to set the config variables in the Settings section
- Set key/value pairs for the following keys:DATABASE_URL, SECRET_KEY
- Go to the dashboard and trigger a deployment - “deploy branch”
- This will trigger a deployment, once the deployment has been successful click on the "Open App" link to open the app
- If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

Note: 
- If Heroku can not be connected to gitpod. On the terminal, type “heroku login -i”.
- Your heroku email and password will be requested.
- Once it is done, type “ heroku git:remote -a travellifestyleblog22”.
- The next step is to push it to heroku by typing “ git push heroku main”. 
- If you encounter any issues accessing the build logs is a good way to troubleshoot the issue


### Acknowledgements

Thanks to my friend Authur Pereira Neto for all the support and help throughout this project, and the Slack groups. 

#### Disclaimer

If there are any issues with the copyright of the content, please contact me. I will fix that as soon as possible. This project is for educational purposes only.

Beatriz Amorim 






