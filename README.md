![Home Page Web](https://github.com/albenakr/the-book-club/blob/master/media/home_page.png ) 


# The Book Club E-Commerce

The Book Club e-commerce was created for educational purposes as part of the Code Institute Fullstack Development course.

The purpose behind The Book Club is to provide a wholistic shopping experience and space for book lovers. For many, deciding on what to read can take long. For picky readers, it involves an ongoing research into reviews, comments, and scouting the internet for ideas etc. The Book Club aims to simplify that by offering each reader the experience that would suit their style.

For those, who know what they're after or enjoy browsing through lists of books- they have the possibility to do so. For those open to a new discovery and to be surprised - the website offers bespoke custom plan builder.

## UX

From the owner's perspective, the goal of the platform is:
- To provide seamless user experience, which allows the user to easily find and ultimately buy what they're looking for.
- Build a community of avid readers around the website, which would result in recurring customers. 

From a user's perspective, the goal is to:
- Find the book they're looking for and suitable suggestions for their taste in literature.

Some of the UX considerations behind the design of the website included - finding the right balance between a modern feel of the website itself, but also creating a peaceful and calming feel, which books and reading create. Hence the colour palette was chosen to be relatively neutral and light with small pops of colour. 

Another important aspect was to make sure there is a seemless flow of information and the natural progression of all pages lead the customer towards either checkout or registration, while giving a number of alternative options as well.

### User Stories

1. Viewing and Navigation
    1. As a user, I want to be able to easily navigate between the products and services the Book Club offers, so that I can select what to purchase.
    2. As a user, I want to be able to see the total of my bag at all times, to make sure I stay within my budget.
    3. As a user, I want to be able to quickly search the book title, author or description, so that I can find if what I'm looking for is available.

2. Browsing Products
    1. As a user, I want to be able to see all the books the shop can offer, so that I can make a choice which one to buy.
    2. As a user, I want to be able to simulataneously filter books based on the genres and languages I prefer, so that I can pick from the ones particularly interesting to me.
    3. As a user, I want to be able to sort the books on offer, based on their price, so that I can choose the most economic option.
    4. As a user, I want to be able to sort the books on offer, based on alphabetical order of the author or title, so that I can understand better what's on offer and choose a book.
    5. As a user, I want to be able to see the details of a book, including author, publication year, rating if available, price, and overview, so that I can choose whether to buy it. 

3. Building Plans
    1. As a user I want to understand how plans work, so that I can choose whether this is a good option for me.
    2. As a user, I want to be able to fill in my preferences when it comes to languagues, genres and plan duration, so that I get a plan customized to what I want. 
    3. As a user, I want an overview of the plan created for me, including the books I'll be receiving and the price plan, so that I can choose if I want to buy the plan.
    4. As a user, I want to see how much money I would save by buying the plan instead of the individual books, so that I can see if it's a good investment.
    5. As a user, I want to be able to re-do the survey, so that I can get a different plan if I don't like the selection presented to me.
    
4. Registration, Authentication & Profiles
    1. As a user, I want to be able to easily register for an account, so that I can make purchases, review my profile and leave reviews.
    2. As a registered user, I want to be able to easily login and logout, so that I can access my account. 
    3. As a registered user, I want to be able to recover my password in case I forget it, so that I can re-gain access to my account.
    4. As a user, I want to receive an email after I register, so that I can be sure the registration was successful.
    5. As a registered user, I want to have a personalized user profile with my order history, delivery information and reviews I've written, so that I can keep track of my interactions with the site.
    
5. Bag
    1. As a user, I want to be able to easily add books and plans to my bag, so that I can purchase them.
    2. As a user, I want to be able to see an overview of my bag, including all the items I've added, their quantities, the subtotal cost and the total cost, so that I can make a decision on whether to purchase.
    3. As a user, I want to be able to remove items from my bag, so that I don't have to buy them if I change my mind.
    4. As a user, I want to be able to update the quantity of a book I'm purchasing from my bag, so that I can make sure I buy the right amount.

6. Chechout and purchasing
    1. As a registered user, I want to be able to save my delivery address information, so that it's available and pre-filled for me for my next purchase.
    2. As a registered user, I want to see an overview of my order at checkout stage, so that I can make sure I'm buying the things I want.
    3. As a registered user, I want to be able to quickly and easlily buy what's in my bag with a credit card, so I don't have to spend too much time going through checkout payment steps. 
    3. As a registered user, I want to receive an email that my order (with order number and details) has been processed and confirmed, so I can make sure the process went smoothly.

7. Writing Reviews
    1. As a registered user, I want to be able to quicklu and easily leave reviews for books that I've read, so that I can share my experience with the Book Club community of readers.
    2. As a registered user, I want to be able to rate a book on a scale, as well as share more detailed comments, so that I can express how much I liked or disliked a book.
    3. As a registered user, I want to be able to see other users' reviews for the books I'm considering buying, so that I can form an opinion on whether to buy a book.
    4. As a user, I want to be able to see the average rating for a book, based on the users reviews, so that I can form an opinion on whether to buy a book.


## Features

The databse schema for this project is available ['here'](https://github.com/albenakr/the-book-club/tree/master/database_schema)

### Existing Features


1. Browsing, searching and filtering books 

This functionality is mostly contained within the 'products' app. It allows a user to view all books currently available, filter through them by Genre and Language, as well as alphabetical order, price etc. Additionally, a user can see all details of a book displayed (book_details.html)

![Shop Books Web](https://github.com/albenakr/the-book-club/blob/master/media/shop_books_web.png) 

![Shop Books Mobile](https://github.com/albenakr/the-book-club/blob/master/media/shop_books_mobile.png) 

2.  Building Custom Plans

Functionality is within the 'plans' app. This feature automatically generates a list of books (plan) and price, based on the criteria a user has picked. The criteria a user can pick are genres, languages and the plan duration (considering they receive 1 book per month, depending on the plan duration, they are signing up for 3, 6 or 12 months/books). The custom_plans view builds a plan for them, based on a randomized set of books matching their criteria. In case the database doesn't contain enough books matching their criteria, the plan is automatically adjusted to the number of books available, so that a user is not overcharged. The price is calculated at 10 EUR per book in a plan, and the plan overview a user sees also displays how much they're saving by going for the plan, instead of individual books. 

![Custom Plan Web](https://github.com/albenakr/the-book-club/blob/master/media/custom_plan_web.png) 

![Custom Plan Mobile](https://github.com/albenakr/the-book-club/blob/master/media/custom_plan_mobile.png) 

3.  Writing Reviews

Registered and logged in users have the possibility to write reviews for books('reviews' app). This includes a rating on a scale of 1 to 5 (average of which is displayed when rendering book details, if available), a overview title of the review and space for comments. On their profile page, a user can see all the reviews they've personally left and delete some.

4.  Checkout

Add to Bag ('bag' app) and Chechout ('checkout' app) functionality, allowing the user to buy individual books, plans or a combination of books and plans. The checkout functionality is fully integrated with Stripe (test version), allowing for users to pay quickly and efficiently. 

5. User Profiles

User profiles functionality ('profiles' app), which renders a user's order history, delivery details and reviews left on books. It was desinged in a way that's enabling them to interact with their history with the website - whether it's to review orders, review books or go through past reviews.

### Features Left to Implement

With more time, the possibilities to expand this project are endless. Those are some of the features I would like to implement next:
- Filtering functionality, based on reviews ratings. This was considered for this first version of the project, but since the reviews are user-generated, rather than pre-uploaded, there isn't enough data to make it viable at this stage.
- More dynamic filtering of books on the Shop Books page through Ajax.
- Re-design the bag functionality, so that the bag contents are saved if a user is registered and logged in. 
- Automated testing.

## Technologies Used
* HTML
    Templates Structure
* CSS
    Template Styling
* JQuery
    The project uses JQuery to simplify DOM access and manipulation.
* Bootstrap
        Bootstrap was used for many of the main elements including navigation manus, buttons, cards etc, and the grid system was used for responsiveness.
* Javascript
        JS was used with some of the bootstrap elements, to make elements more dymanic (including quantity update buttons) and improve the UX.
* Python
        The core of this project was build in Python 3.8.3.
* Django
        Django and its additional array of libraries and resources (e.g. allauth, crispy) were heavily used for the overall setup and running of this project.
* Postgres
        Postgres is used as database in the deployed app.
* Heroku
        Heroku is used for hosting the deployed app.
* AWS
        AWS S3 is used for storing media and static files for the deployed project.
* Git
        Git was used for version control.
* Github
        Github was used for code storage.
* Stripe
        Stripe is used as payments processor.


## Testing

The app has been tested for responsiveness across all sizes available throught the Dev Tools, including: Desktop, Moto G4, Galaxy S5, Pixel 2, Pixel 2 XL, iphone %/SE, 6, 7, 8, iPhone 6/7/8 +, iPhone X, iPad, iPad Pro, Surface Duo, Galaxy Fold.

The entire application was tested continuously throughout the development, as well as extensively after deployment in the final stages of this project. 

Tests were predominantly manual and a more detailed write-up of the tests conducted can be found in the folder ['tests'](https://github.com/albenakr/the-book-club/tree/master/tests) within this project. 


## Deployment

The settings.py file is currently set up so that if 'DEVELOPMENT' is in the environment, the code runs locally. 
This includes local sqlite database (db.sqlite3 file), Debug is True and emails are sent to the console, instead of an actual email.

If not, the database is Postgres in Heroku, the emails are handled through the email provider and static and media files are stored and accessed through AWS S3. 

The processes below, whether running locally or deploying to Heroku are based on the current setup in settings.py.

### Running the code locally
To run the project locally:
1. Get repository from github
2. Set up a 'DEVELOPMENT' variable in your environment, equal to True.
3. Install Django
`python3 -m pip install Django`
4. Install Allauth
`pip3 install django-allauth` 
5. Install crispy forms 
`pip3 install django-crispy-forms`
6.Install django countries 
`pip3 install django_countries`
7. Install stripe
`pip3 install stripe`
8. Install pillow 
`python3 -m pip install pillow`
9. Apply migrations
`python manage.py migrate` 
10. Load the data from the fixtures, making sure to load genres and languages before books:
`python3 manage.py loaddata genres`
`python3 manage.py loaddata languages`
`python3 manage.py loaddata books`
10 Create superuser to go have access to admin
`python3 manage.py createsuperuser`

### Deplyment to AWS and Heroku

1. To use Postgres, install dj_database_url, and psycopg2:
`pip3 install dj_database_url`
`pip3 install psycopg2-binary`
2. Install gunicorn:
`pip3 install gunicorn`
3. Create a requirements.txt file. 
`pip3 freeze --local > requirements.txt`
4. Create a Procfile: 
`echo web python3 {app.py or name of python file} > Procfile`
5. Install Heroku:
`npm install -g heroku`
6. Login to Heroku: 
`heroku login`
7. Associate the Heroku application as the master branch, or remote master branch. Command: 
`Heroku git:remote {name of the app on heroku}`
8. Add, commit and push to Git.
9. Push to Heroku. 
`git push heroku master`
10. Set up a bucket in AWS S3 with all static and media files
11. To enable AWS in Django, install boto and django-storages
`Pip3 install boto3`
`pip3 install django-storages`
12. Set up Configuration variables in Heroku:
    * SECRET_KEY: {your django secret key}
    * AWS_ACCESS_KEY_ID: {You can get it from Amazon}
    * AWS_SECRET_ACCESS_KEY: {You can get it from Amazon}
    * DATABASE_URL: {from Postgres Add-on in Heroku}
    * EMAIL_HOST_PASS: {from email provider}
    * EMAIL_HOST_USER: {email you're using}
    * STRIPE_PUBLIC_KEY: {from Stripe}
    * STRIPE_SECRET_KEY: {from Stripe}
    * STRIPE_SECRET_KEY: {from Stripe}
    * USE_AWS: True

You can see the live app here: https://book-club-ecommerce.herokuapp.com/

## Credits

### Content

All books descriptions were taken from the snippet descriptions or the respective Wikipedia pages for each book. It should be noted that for a future version of this website and for any version that is used for anything outside of educational purposes, this content would be updated with propriety custom descriptions.

### Media

The Home page photo: Photo by Kimberly Farmer on [Unsplash](https://unsplash.com/s/photos/books?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

The Plans page photo : Photo by [freestocks](https://unsplash.com/@freestocks) on [Unsplash](https://unsplash.com/s/photos/books?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)


The book cover photos used in this site were obtained primarily from wikipedia results and photos. I do not own the rights to any of them, they're being used here as part of an educational project, which will not be monetized with this content.


### Acknowledgements
This project was largely inspired by the [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1) project presented in the Code Institute course. More specifically, the bag, checkout and web hooks functionality, as well as the Stripe integration were based on this content. They were adjusted to account for The Book Club selling two types of products - individual books and plans.

The filtering functionality was inspired by [this project](https://github.com/justdjango/djfilter/blob/master/core/views.py) and the accompanying [tutorial](https://www.youtube.com/watch?v=n1_MQiSXyxw&list=PLLRM7ROnmA9EGO3TOlWLgrc46EhTgj1Ih&index=6)

Back to Top Button was inspired by this [W3Schools example](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_js_scroll_to_top).

The color palette for the website was inspired by [this palette](https://coolors.co/e63946-f1faee-a8dadc-457b9d-1d3557), suggested by Coolors.co


