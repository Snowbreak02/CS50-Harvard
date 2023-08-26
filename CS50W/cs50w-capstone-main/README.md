# CS50W Final Project - Capstone

- [Demo Video](https://youtu.be/6itl44cE4iA)

## Overview

This web application is a learning platform website for web developers built with [Django] and [Boostrap], JavaScript.

The website has six caategories: book, code, course, document, quiz, and video, each with a designated level of difficulty. There are three degrees of difficulty: basic, intermediate, and advanced. Four languages are supported by the website: Python, JavaScript, HTML, and CSS.

This application is designed as a platform for aspiring coders as well as seasoned coders to learn and share useful knowledge to grow as a community. Once an account has been created, users will be able to publish content to the website, add content to favorites, and add a comment to any content.

## Distinctiveness and Complexity

My web application is unique and not based on the previous CS50W Pizza project and is unlike all the other projects in the course. This website is a learning platform that is discussed in the section titled "Overview". The 'fetch' function is used by this web application to update the page using its API routes. Additonionally, I've implemented a shortcut key for the website and made a customised template filter for my HTML file.

I have built my web app using Django, including four models on the back-end. One of the models has a customized save method. There are three JavaScript files for the front-end of this project. The content page uses JavaScript to manipulate the DOM, so it does not have to reload the whole page and inform the users by updating the URL via the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). 

My web application is mobile-responsive as well. I have used the [viewport meta tag] and [Boostrap] to achieve responsiveness and control layout on mobile browsers. All features and pages are available on the mobile view. I also utilized [Boostrap's Modal] and [CSS Animation] to make the site more responsive.

## What’s contained in each file

- **capstone**
- **webdev** - Application directory.
    - **migrations** 
    - **static/webdev** - Static files (JS and CSS).
        - **index.js** - Fetches content to display it on the page.
        - **resource.js** - Handles user interaction with each resource (including like, favor, and comment).
        - **script.js** - Specifies shortcut keys for the site.
        - **styles.css** - Additional styles and animation.
    - **templates/webdev** - Template files (HTML).
        - **content.html** - Displays categorized content page.
        - **create.html** - A page for adding a new resource.
        - **index.html** - Landing/Search results page.
        - **layout.html** - Base HTML for every page.
        - **login.html** - User authentication page.
        - **register.html** - User registration page.
        - **resource.html** - Displays a full detailed content page (such as an embedded site, comments, etc.).
    - **__init__.py** 
    - **admin.py** 
    - **apps.py** 
    - **forms.py** 
    - **models.py** - Contains four models: `User`, `Comment`, `Language`, and `Resource` with model fields and methods.
    - **tests.py** 
    - **urls.py** - Contains URL paths and API routes for the app.
    - **views.py** - Contains view functions (handle HTTP requests/responses) and a custom template filter for the app.
- **.gitignore** 
- **db.sqlite3** 
- **manage.py** 
- **README.md** 
- **requirements.txt** - List of required Python packages.

## How to run this application

1. Install [Python](https://www.python.org/downloads/) on your system.
2. Change your working directory to `capstone`.
3. Install required packages `pip install -r requirements.txt`.
4. Execute `python manage.py runserver`.
5. Visit the URL in your browser.

## Appendix

- Superuser account

```
    username: Jellom
    password: 1234
```
