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

<details><summary><b>Github Board</b></summary>

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

![Database Schema](readme/images/database_schema_small.png)
</details><br/>

<details><summary><b>Database Schema Full</b></summary>

![Database Schema](readme/images/database_schema_full.png)
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

### Staff Member

|  | | |
|:-------:|:--------|:--------|
| As a Staff Member | I can view list of draft posts so that I can choose which post to publish | &check; |
| As a Staff Member | I can view list of draft connects so that I can choose which connect to publish | &check; |
| As a Staff Member | I can view list of draft comments so that I can choose which comment to publish | &check; |
| As a Staff Member | I can view/edit/delete/publish draft post so that I can secure high quality of the post content for the Site Users | &check; |
| As a Staff Member | I can view/edit/delete/publish draft connect so that I can secure high quality of the connect content for the Site Users | &check; |
| As a Staff Member | I can delete/publish draft comment so that I can secure a safe environment for the Site Users | &check; |
| As a Site User | I can connect social account to my account so that I can login easily | &check; |

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

```
source env/bin/activate
```
```
python3 manage.py runserver
```
```
python3 manage.py makemigrations --dry-run
```
```
python3 manage.py showmigrations
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
python3 manage.py collectstatic --no-input
```