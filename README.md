# **United**
United is a project for searching a partner for co-op game, earn tropyes and have fun finding a new friends! The site is divided into two blocks, *United | Blog* with posts and *United | Connect* with games, and offers a convenient search for finding games of interest to contact the author or an interesting post for discussion in the comments. All visitors can create their own user to start creating posts and game connects, comment on other authors posts, connect with other authors of game connects. All game connects, posts, and comments need approval by *United* staff members so everyone can feel safe from abuse, inappropriate language, etc. The approvals are being made from website UI pages that only is accessed by staff members. From a visual point of view the site has a clean look that makes navigation easy, and the freedom to design the posts and connections themselves remains with the user.



This website was created for Portfolio Project #4 - Diploma in Full Stack Software Development Diploma at the [Code Institute](https://www.codeinstitute.net).

[View live website here](https://www.uniteds.games/)

![United responsive design](readme/images/responsive.png)

# Contents

* [**Project**](<#project>)
    * [Objective](<#objective>)
    
    * [Site Users Goal](<#site-users-goal>)
    
    * [Site Owners Goal](<#site-owners-goal>)
    
    * [Project Management](<#project-management>)

* [**User Experience (UX)**](<#user-experience-ux>)

    * [User Stories](<#user-stories>)

    * [Site Structure](<#site-structure>)

    * [Design Choices](<#design-choices>)

* [**Existing Features**](<#existing-features>)

    * [Navigation](<#navigation>)
    
    * [Blog](<#blog>)
    
    * [Connect](<#connect>)
    
    * [Account](<#account>)
    
    * [Social Account](<#social-account>)
    
    * [My Posts](<#my-posts>)
    
    * [My Games](<#my-games>)
    
    * [Post Detail View](<#post-detail-view>)
    
    * [Create Post](<#create-post>)
    
    * [Create Game Connect](<#create-game-connect>)
    
    * [Edit Post](<#edit-post>)
    
    * [Edit Game Connect](<#edit-game-connect>)
    
    * [Publish Posts](<#publish-posts>)
    
    * [Publish Connects](<#publish-connects>)
    
    * [Draft Post Detail View](<#draft-post-detail-view>)
    
    * [Draft Game Connect Detail View](<#draft-game-connect-detail-view>)
    
    * [Publish Post Confirmation](<#publish-post-confirmation>)
    
    * [Publish Game Connect Confirmation](<#publish-game-connect-confirmation>)
    
    * [Publish Comments](<#publish-comments>)
    
    * [Admin Page](<#admin-page>)
    
    * [Sign Up](<#sign-up>)
    
    * [Sign In](<#sign-in>)

    * [Sign Out](<#sign-out>)

    * [Footer](<#footer>)

    * [Flash Messages](<#flash-messages>)

* [**Features Left To Implement**](<#features-left-to-implement>)

# **Project**

## Objective
The idea of ​​creating this site came to me while looking for a partner to play together online to get the last trophy in one of the computer games. In the game itself, there is no auto-selection of a partner. And among my friends there are no gamers who are fond of the same game. I could not find a convenient tool with which to easily find a person to play together. The only option is to scroll through countless comment pages on old fashioned forums and send private messages to the commenters in the hope that they still have the game and the desire to win the trophy.

I also want to demonstrate my knowledge within the area of HTML, CSS, JavaScript, Python and the Django Framework.

## Site Users Goal
The user of 'United' loves gaming, to play together with others and to collect trophies, contributing with their knowledge to like minded. The user easily finds a partner in a game of interest and a post on a topic of interest.

## Site Owners Goal
The goal of the site owner is to deliver a site that the owner himself will use, where the users in an intuitive way can read about the games, contribute with their own posts, connect with new friends to play together. 

## Project Management

### Github Board
I've been using the project board in GitHub to keep my project together. It helped me structure up my work. GitHub was used to plan and organize my user stories.

<details><summary><b>User Stories</b></summary>

![User Stories](readme/images/user_stories.png)
</details><br/>

[Back to top](<#contents>)

### Database Schema
I've used a modelling tool called [Graph Models](https://django-extensions.readthedocs.io/en/latest/graph_models.html) to create the database schema. It shows the relationships between the different models in the database connected to the application. Graph Models exports a *.png file which visualize models.

Models used (besides standard user model) in this project are:

* **Post** - Handles all the posts in the blog application.
* **Comment** - Handles all the comments for posts in the blog application.
* **Game** - Handles all the games in the connect application.

<details><summary><b>Database Schema Small</b></summary>

![Database Schema Small](readme/images/database_schema_small.png)
</details><br/>

<details><summary><b>Database Schema Full</b></summary>

![Database Schema Full](readme/images/database_schema_full.png)
</details><br/>

# **User Experience (UX)**

## User Stories
Below the user stories for the project are listed to clarify why particular feature matters. These will then be tested and confirmed in the [Testing](<#testing>) section.

### Site User
|  | | |
|:-------:|:--------|:--------|
| As a Site User | I can view a list of posts so that I can select one to read | &check; |
| As a Site User | I can click on a post so that I can read the full text | &check; |
| As a Site User | I can view a paginated list of posts so that easily select a post to view | &check; |
| As a Site User | I can register an account so that I can comment and like | &check; |
| As a Site User | I can like or unlike a post so that I can interact with the content | &check; |
| As a Site User | I can view comments on an individual post so that I can read the conversation | &check; |
| As a Site User | I can leave comments on a post so that I can be involved in the conversation | &check; |
| As a Site User | I can view the number of likes on each post so that I can see which is the most popular or viral | &check; |
| As a Site User | I can add draft posts for the website UI so that staff member can approve it | &check; |
| As a Site User | I can see all my posts so that I knew which of them is published | &check; |
| As a Site User | I can search for posts so that I can filter posts that match my interests | &check; |
| As a Site User | I can view a list of connects so that I can select one to read | &check; |
| As a Site User | I can click on a connect so that I can read the full text | &check; |
| As a Site User | I can view a paginated list of connects so that easily select a connect to view | &check; |
| As a Site User | I can add draft connects for the website UI so that staff member can approve it | &check; |
| As a Site User | I can see all my connects so that I knew which of them is published | &check; |
| As a Site User | I can search for connects so that I can filter connects that match my interests | &check; |
| As a Site User | I can sign out from the site so that I can be safe that nobody can access my information | &check; |
| As a Site User | I can edit my login and email so that I can update up-to-date information about me | &check; |
| As a Site User | I can sign in / sign up with social account so that I can get access to all advantages of authenticated user faster | &check; |
| As a Site User | I can connect social account to my account so that I can login easily | &check; |

### Staff Member

|  | | |
|:-------:|:--------|:--------|
| As a Staff Member | I can view list of draft posts so that I can choose which post to publish | &check; |
| As a Staff Member | I can view list of draft connects so that I can choose which connect to publish | &check; |
| As a Staff Member | I can view list of draft comments so that I can choose which comment to publish | &check; |
| As a Staff Member | I can view/edit/delete/publish draft post so that I can secure high quality of the post content for the Site Users | &check; |
| As a Staff Member | I can view/edit/delete/publish draft connect so that I can secure high quality of the connect content for the Site Users | &check; |
| As a Staff Member | I can delete/publish draft comment so that I can secure a safe environment for the Site Users | &check; |

### Site Admin

|  | | |
|:-------:|:--------|:--------|
| As a Site Admin | I can approve or disapprove post comments so that I can filter out objectionable comments | &check; |
| As a Site Admin | I can create, read, update and delete posts so that I can manage my blog content | &check; |
| As a Site Admin | I can create, read, update and delete connects so that I can manage my connect content | &check; |
| As a Site Admin | I can create draft posts so that I can finish writing the content later | &check; |
| As a Site Admin | I can create draft connects so that I can finish writing the content later | &check; |
| As a Site Admin | I can access an admin area so that I can get a general understanding of logged in users, number of likes and number of posts | &check; |

[Back to top](<#contents>)

## Site Structure

The 'United' site is split up in two parts: **Blog** for **posts** and **Connect** for **game connects**.

The functionality is alo different **when the user is logged out** and **when the user is logged in**. Depending on login status different pages is available for the user. When the user is logged out the pages: *Sign In*, *Blog*, and *Connect* are avaliable. When the user is logged in: dropdown menu with username (*My account*, *My games* or/and *My posts*, *Sign Out*), *Add game* or *Add post*, *Blog*, and *Connect* are available. If you are logged in as an administrator or staff member an *admin area* is available: *Publish connects* or *Publish comments* with *Publish posts*. The site has an minimalistic, clean and intuitive design that makes the site easy to navigate for the user.

Read more about the different choices in the [Features](<#features>) section.

[Back to top](<#contents>)

## Design Choices

* ### Color Scheme

The color scheme chosen for the 'United' site is based on the Bootstrap 4.6 default colours. The colors are chosen in such a way that the background contrasts with the elements with which you can interact, the color of the buttons reflects their purpose, and the use of the functionality is as intuitive as possible. All colors are very clean and they create a professional look together and offers a good readability and contrast as well. I used the online service [Coolors](https://coolors.co/) to choose the color scheme.

![Color Palette image](readme/images/main_colors.png)

* ### Typography
The fonts used for the site are the most popular fonts, depends on the operating system. Fallback font for all of them is sans-serif.

* "BlinkMacSystemFont": This is a system font specific to Apple devices, used by the Blink rendering engine on macOS.
* "Segoe UI": This is a font commonly used on Microsoft Windows systems.
* Roboto: This is a popular font developed by Google and commonly used in material design.
* "Helvetica Neue": This is a widely used font that is similar to Helvetica but introduced by Apple.
* Arial: This is a widely available font that is commonly used on both Windows and macOS.
* "Noto Sans": This is a font developed by Google that supports a wide range of scripts and languages.
* "Liberation Sans": This is a font designed to replace Arial on Linux systems.
* sans-serif: This is a generic font family that refers to a sans-serif font available on the system.

[Back to top](<#contents>)

# **Features**
The features of the site are listed below.

## **Existing Features**

### **Navigation**
The navigation bar is very clean and straight forward. Depending if you are logged in or not different menus are visible for the site user. An extra menu item is visible if you are logged in as an administrator / staff member.

*Links that are visible to logged out users*

* Sign In - Gives the user the opportunity to sign in or sign up if not ready a registered user at United.
* Blog - Lists all posts.
* Connect - Lists all game connects.

<details><summary><b>Navigation Desktop - User Signed Out</b></summary>

![Navigation Desktop - User Signed Out](readme/images/navbar_desktop_signed_out.png)
</details><br/>

<details><summary><b>Navigation Mobile - User Signed Out</b></summary>

![Navigation Mobile - User Signed Out](readme/images/navbar_mobile_signed_out.png)
</details><br/>

*Links that are visible to logged in users*

* Username dropdown list:
    * My account - Shows logged in users profile page.
    * My posts / My games - Lists all posts or game connects created by the logged in user depending on which section of the site the user is in.
    * Sign out - Logs out the user.
* Add post / Add game - Lets the user create a new post or game connect depending on which section of the site the user is in.
* Blog - Lists all posts.
* Connect - Lists all game connects.

<details><summary><b>Navigation Desktop Blog - User Signed In</b></summary>

![Navigation Desktop Blog - User Signed In](readme/images/navbar_desktop_blog_signed_in.png)
</details><br/>

<details><summary><b>Navigation Desktop Connect - User Signed In</b></summary>

![Navigation Desktop Connect - User Signed In](readme/images/navbar_desktop_connect_signed_in.png)
</details><br/>

<details><summary><b>Navigation Mobile Blog - User Signed In</b></summary>

![Navigation Mobile Blog - User Signed In](readme/images/navbar_mobile_blog_signed_in.png)
</details><br/>

<details><summary><b>Navigation Mobile Connect - User Signed In</b></summary>

![Navigation Mobile Connect - User Signed In](readme/images/navbar_mobile_connect_signed_in.png)
</details><br/>

*Link that is visible if user is administrator / staff member*

All of the links above plus the ones below.

* Blog section:
    * Publish comments - Lists all draft post comments to approve.
    * Publish posts - Lists all draft posts to approve.
* Connect section:
    * Publish games - Lists all draft g ame connects to approve.

<details><summary><b>Navigation Desktop Blog - Admin / Staff Logged In</b></summary>

![Navigation Desktop Blog - Admin / Staff Logged In](readme/images/navbar_desktop_blog_admin_signed_in.png)
</details><br/>

<details><summary><b>Navigation Desktop Connect - Admin / Staff Logged In</b></summary>

![Navigation Desktop Connect - Admin / Staff Logged In](readme/images/navbar_desktop_connect_admin_signed_in.png)
</details><br/>

<details><summary><b>Navigation Mobile Blog - Admin / Staff Logged In</b></summary>

![Navigation Mobile Blog - Admin / Staff Logged In](readme/images/navbar_mobile_blog_admin_signed_in.png)
</details><br/>

<details><summary><b>Navigation Mobile Connect - Admin / Staff Logged In</b></summary>

![Navigation Mobile Connect - Admin / Staff Logged In](readme/images/navbar_mobile_connect_admin_signed_in.png)
</details><br/>

### **Search**
The heart of this project is the search. This is a convenient way to search for game connects and posts of interest. It's available on the pages showing the list of games and posts (*Blog*, *My posts*, *Connect*, *My games* - for all users, and additionally *Publish posts* and *Publish games* - for administrator and staff member). The search does not require submission and refreshes output after each character input or deletion.

<details><summary><b>Search</b></summary>

![Search](readme/images/search.png)
</details><br/>

### **Blog**
This page lists all the posts that has been made at United | Blog. For signed in and not signed in users this page looks the same. The page shows 12 cards before a pagination mechanism kicks in.

<details><summary><b>Blog</b></summary>

![Blog](readme/images/blog.png)
</details><br/>

### **Connect**
This page lists all the game connects that has been made at United | Connect.

<details><summary><b>Connect</b></summary>

![Connect](readme/images/connect.png)
</details><br/>

If the user is not signed in there is a sign in button in each open accordeon card view with the text: "Sign In to Connect or to Create a Connect".

<details><summary><b>Connect - User Signed Out</b></summary>

![Connect - User Signed Out](readme/images/connect_user_signed_out.png)
</details><br/>

If the user is logged in a *Connect* option gets visible on the game connect open accordeon card view.

<details><summary><b>Connect - User Signed In</b></summary>

![Connect - User Signed In](readme/images/connect_user_signed_in.png)
</details><br/>

If the user is logged in is a author of the game connect: an *Edit* option gets visible at open accordeon card view.

<details><summary><b>Connect - Author Signed In</b></summary>

![Connect - Author Signed In](readme/images/connect_author_signed_in.png)
</details><br/>

### **Account**
On this page the user can view and update their own username and email.

<details><summary><b>Account</b></summary>

![Account](readme/images/account.png)
</details><br/>

### **Social Account**
On this page the user can add or remove 3rd party accounts (Google and GitHub).

<details><summary><b>Social Account</b></summary>

![Social Account](readme/images/social_account.png)
</details><br/>

### **My Posts**
This page lists all the posts that has been made at United by signed in user. If the user is not logged in this page is forbidden. Here the user can see which of the posts have already been published and which are still avaiting approval.

<details><summary><b>My Posts</b></summary>

![My Posts](readme/images/my_posts.png)
</details><br/>

### **My Games**
This page lists all the game connects that has been made at United by signed in user. If the user is not logged in this page is forbidden. Here the user can see which of the game connects have already been published and which are still avaiting approval.

<details><summary><b>My Games</b></summary>

![My Games](readme/images/my_games.png)
</details><br/>

### **Post Detail View**
The post detail shows the details about the post that the user has chosen in the blog view. Depending on if the user is signed in and if the user is a post author the view looks a little bit different. If the user is logged in they get the possibility to like the post and also can see if it published and edit or delete it if they have written it. A signed in user can also leave a comment.

<details><summary><b>Post Detail View - User Logged Out</b></summary>

![Post Detail View - User Logged Out](readme/images/post_detail_logged_out.png)
![Post Detail View Comment - User Logged Out](readme/images/post_detail_comment_logged_out.png)
</details><br/>

<details><summary><b>Post Detail View - User Logged In</b></summary>

![Post Detail View - User Logged In](readme/images/post_detail_logged_in.png)
![Post Detail View Comment - User Logged In](readme/images/post_detail_comment_logged_in.png)
</details><br/>

<details><summary><b>Post Detail View - Author Logged In</b></summary>

![Post Detail View - Author Logged In](readme/images/post_detail_author_logged_in.png)
![Post Detail View Comment - Author Logged In](readme/images/post_detail_author_comment_logged_in.png)
</details><br/>

### **Create Post**
On this page the registered and signed in user can create their own post. When they have created it in 'United' needs to approve it, until it's approved it will not be visible for the public.

<details><summary><b>Create Post</b></summary>

![Create Post](readme/images/create_post.png)
</details><br/>

### **Create Game Connect**
On this page the registered and signed in user can create their own game connect. When they have created it in 'United' needs to approve it, until it's approved it will not be visible for the public.

<details><summary><b>Create Game Connect</b></summary>

![Create Game Connect](readme/images/create_game_connect.png)
</details><br/>

### **Edit Post**
On this page the registered and logged in user can edit their own post. When they have updated it in 'United' needs to re-approve it, until it's re-approved it will not be visible for the public.

<details><summary><b>Edit Post</b></summary>

![Edit Post](readme/images/edit_post.png)
</details><br/>

### **Edit Game Connect**
On this page the registered and logged in user can edit their own game connect. When they have updated it in 'United' needs to re-approve it, until it's re-approved it will not be visible for the public.

<details><summary><b>Edit Game Connect</b></summary>

![Edit Game Connect](readme/images/edit_game_connect.png)
</details><br/>

### **Publish Posts**
This page lists all the draft posts avaiting approval that has been made at 'United' by signed in users. This page available only for administrator or staff member. If the user is not logged in this page is forbidden. Here the admin / staff member can choose the post to approve or delete.

<details><summary><b>Publish Posts</b></summary>

![Publish Posts](readme/images/publish_posts.png)
</details><br/>

### **Publish Connects**
This page lists all the draft game connects avaiting approval that has been made at 'United' by signed in users. This page available only for administrator or staff member. If the user is not logged in this page is forbidden. Here the admin / staff member can choose the g ame connect to approve or delete.

<details><summary><b>Publish Connects</b></summary>

![Publish Connects](readme/images/publish_connects.png)
</details><br/>

### **Draft Post Detail View**
The draft post detail shows the details about the draft post that the administrator / staff member has chosen in the publish posts view. Depending on if the administrator / staff member is a post author the view looks a little bit different. If the author of the post is a signed in admin / staff member, there will be no possibility to publish this post, only edit it.

<details><summary><b>Draft Post Detail View</b></summary>

![Draft Post Detail View](readme/images/draft_post_detail.png)
</details><br/>

<details><summary><b>Draft Post Detail View - Admin / Staff member is Author</b></summary>

![Draft Post Detail View - Admin / Staff member is Author](readme/images/draft_post_detail_author.png)
</details><br/>

### **Draft Game Connect Detail View**
The draft game connect detail shows the details about the draft game connect that the administrator / staff member has chosen in the publish connects view. Depending on if the administrator / staff member is a game connect author the view looks a little bit different. If the author of the game connect is a signed in admin / staff member, there will be no possibility to publish this game connect, only edit it.

<details><summary><b>Draft Game Connect Detail View</b></summary>

![Draft Game Connect Detail View](readme/images/draft_connect_detail.png)
</details><br/>

<details><summary><b>Draft Game Connect Detail View - Admin / Staff member is Author</b></summary>

![Draft Game Connect Detail View - Admin / Staff member is Author](readme/images/draft_connect_detail_author.png)
</details><br/>

### **Publish Post Confirmation**
On this page admin / staff member can edit draft post before publishing.

<details><summary><b>Draft Post Publish Confirmation</b></summary>

![Draft Post Publish Confirmation](readme/images/draft_post_publish_confirm.png)
</details><br/>

### **Publish Game Connect Confirmation**
On this page admin / staff member can edit draft game connect before publishing.

<details><summary><b>Draft Game Connect Publish Confirmation</b></summary>

![Draft Game Connect Publish Confirmation](readme/images/draft_connect_publish_confirm.png)
</details><br/>

### **Publish Comments**
This page lists all the draft comments avaiting approval that has been made at 'United' by signed in users. This page available only for administrator or staff member. If the user is not logged in this page is forbidden. Here the admin / staff member can approve or delete draft comments.

<details><summary><b>Publish Comments</b></summary>

![Publish Comments](readme/images/publish_comments.png)
</details><br/>

### **Admin Page**
This page is available only by for superusers by url [/admin](https://www.uniteds.games/admin/). On this page the administrator (or other superuser decided by 'United') can *approve* / *delete* / *publish* / *unpublish* and *delete* posts, connects and comments. General information about *number of users*, *number of comments*, *number of posts*, *number of connects*, *unapproved comments / posts / connects* is also being showed on the page.

<details><summary><b>Admin Page</b></summary>

![Admin Page](readme/images/admin_page.png)
</details><br/>

### **Sign Up**
If the site visitor has no registered user at 'United' they can sign up. They can also sign in with social account (Google or GitHub).

<details><summary><b>Sign Up</b></summary>

![Sign Up](readme/images/sign_up.png)
</details><br/>

### **Sign In**
On this page the user can sign in to 'United'.

<details><summary><b>Sign In</b></summary>

![Sign In](readme/images/sign_in.png)
</details><br/>

### **Sign Out**
When the user clicks sign out in the dropdown menu a confirmation page is being showed so that the user don't accidently sign out.

<details><summary><b>Sign Out</b></summary>

![Sign Out](readme/images/sign_out.png)
</details><br/>

### **Footer**
The footer area includes name of the creator and links to relevant resources.

<details><summary><b>Footer</b></summary>

![Footer](readme/images/footer.png)
</details><br/>

### **Flash Messages**
The sites incorporates flash messages when an action has been performed (i.e. create/update/delete actions). Examples of this in the screenshots below.

<details><summary><b>Confirmation Messages</b></summary>

![Comment Added](readme/images/comment_added.png)
![Connect Deleted](readme/images/connect_deleted.png)
![Signed In](readme/images/signed_in.png)
![Signed Out](readme/images/signed_out.png)
</details><br/>

### Features Left to Implement

* Add automated testing
* Add comments to the game connect open accordeon view
* Add likes to the game connects
* Add ajax functionality to post likes
* Add ajax functionality to post comments
* Add likes functionality to the Blog view
* Add more 3rd party social account providers (Facebook, Twitter, etc)
* Add editing and deliting comments for comment authors

[Back to top](<#contents>)
