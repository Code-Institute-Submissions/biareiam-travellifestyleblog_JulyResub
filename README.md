# Code Institute Data Centric Development Milestone Project

## What’s Up | Blog

This blog was created to host posts covering a series of different topics, such as travel, lifestyle, food & drink, fashion, and so on. Users can browse through many different posts and engage with them. If registered, users can submit, edit and delete posts published by themselves. It was designed to have a clean and simple navigation, aiming for a smooth user experience. 

## UI/UX
### Project goals

What's Up Blog is milestone project for Code Institute Data Centric Development module. The goal of this project is to create, store, edit and delete posts (CRUD). Target audience for this project is people that are interesting in topics such as travel, lifestyle, books and movie. User have the abilite to create different categories, expading the topics for discussion on the blog. 

#### User Stories
As a user, I want: 

* Be able to view the site on my preferred device (mobile, tablet, desktop).
* Be able to view all the posts without needing to sign up.
* Be able to see each post individually.
* Be able to choose a category.
* Be able to see all the categories.
* Be able to see the profile of the author of the post.
* Be able to register to the site.
* Be able to sign in and sign out. 
* Be to create my own profile.
* Be able to add, edit and delete posts to the website.
* Be able to change my profile information.
* Be able to change my password.
* Be able to see a list of my own posts.
* Be able to add a new category.
* Be able to add a comment to a post.
* Be able to like a post if signed in.
* Be able to read other users' comments


This site was built on the basis of ideas from initial wireframes created in Figma and exported image files for these can be seen below. Some changes were done as the projectes started to getting into shape, for instance the color of the background are different from the initial idea. 

IMAGES!!!!

#### Color Scheme
Colors are kept to a minimum in order to keep focus on the imagery of the post, chosen colours are various shades of purple. Color scheme can be found below:

IMAGESS!!

#### Typography
tWO Google Fonts were used across the site:

fontssssss

####  Media

The images on the blog were from [Pexel](https://www.pexels.com/).

### Features

#### Existing Features on every page

**Navbar**
The navigation bar features the blog name in the top left corner, which works as a link to the home page from any other page on the blog. The other navigation links are in the top right. 

For users who visited to site and are not registered/logged in yet, the follow links are visible:

* Home
* Categories
* Login
* Register

For users who are logged in, the follow links are visible:

* Home
* Categories
* Add Post
* User's name 
    * Profile (the actual profile page)
    * Edit Profile
    * My Posts
    * Settings
    * Logou out 

Python determines if the user is logged in or not by checking if 'user' in session and passes this data to Jinja to display the correct navbar for the user.

On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked.

**Footer**
The footer features some key Information such as copyright information and links to social media platforms.

#### Elements on Multiple Pages

**Posts Cards**
(Home, individual category page, my posts page)

It displays the post's image, a small headline of the post, date posted, author of the post and a "Read More" button which directs users to the individual post page. The user can also be directed to that page by clicking on the images. 
On large and medium devices, 3 cards are displayed in a row and on smaller devices, one card per row. If the user hover over the images, they zoom in a little giving it a bit of effect. 

**Pagination**
(Home, individual category page, my posts page)

Where there are more than six results navigation links to pages are displayed below the number of results (6 results per page).

**Sort into categories**
(Home, categories page, individual category page, post page, my posts page)

One the card, in the home page, it is possible to see the category the post belongs to and by clicking on it, the user is directed to a page with all the posts from that specific category. The same happens on the individual post page and also on the my posts page, which is were a user can see all the posts published by himself/herself.


#### Individual Pages

* Post Page

**Edit and Delete post**

If logged in and the author of the post, the user can either edit or delete it, if desired. 

**Like button**
If logged in, the user can like and deslike a post.

**Author Profile**
The user can check the profile of the author of the post, as well as see their social media. 

**Comments**
When logged in, user can leave comments on the posts. Everyone is able to see them, logged in or not.

**edit and delete post**

The owner of the post have the power to edit and delete it, if wish.

* Login
This section contains a form where users may login and be redirected to Home Page. Below the form, the user can find a link to register.

* Logout
Clicking 'Logout' ends a user session and redirects them to the 'Home' page.

* Register
This section contains a registration form.Once it is completed, they will be redirectd to the login page where they can then sign in.

* User Profile

It contains a profile image, the user first and last name, their email, bio and a link to their social media.

* Edit Profile

The own of the profile can edit it, for instance change the profile image or the information provided in the bio. 

* Settings
On this page, the user can change their first and last name, email, and password. 

* My Post
This page display as posts published by the user, who is logged in. if there is no posts, there is a message and a button directing them to the add post page. 

* Add Post
User who are registered can cread their own post.

* Categories
User can see all the existing categories and if needed, add a new one. For instance, pets.

#### Future Features
* make it possible for users to edit and deleted comments.
* Have "favorites" area where users can add their favorite posts.
