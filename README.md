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



#### Future Features