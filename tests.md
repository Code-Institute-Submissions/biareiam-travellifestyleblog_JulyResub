# What'up Blog - Testing documentation

*This file contains the Testing section of the [full README.md file for the what's Up | Blog](README.md).*
## Validators

  * W3C HTML Validator Passed tests without issues
  * W3C CSS Validator Passed tests without issues
  * PEP8 and AUTOPEP8. Online PEP8  previously warned about lines being too long and it was FIXED. No errors should be displayed. 

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