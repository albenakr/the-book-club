
<div class="row">
   <div class="col">
      <div class="table-responsive-md">
         <table class="table">
            <thead>
               <tr class="orange-background">
                  <th>Order Number</th>
                  <th>Date</th>
                  <th>Items</th>
                  <th>Order Total</th>
               </tr>
            </thead>
            <tbody>
               {% for order in orders %}
               <tr>
                  <td>
                     <a
                        href="{% url 'order_history' order.order_number %}"
                        title="{{ order.order_number }}"
                        >
                     {{ order.order_number|truncatechars:6 }}
                     </a>
                  </td>
                  <td>{{ order.date }}</td>
                  <td>
                     <ul class="list-unstyled">
                        {% for item in order.lineitems.all %}
                        <li class="small">
                           {% if item.book != None %}
                           <p >
                              <strong>"{{ item.book.title }}"</strong> (book)
                              <br>
                              <a
                                 class="p-1 mt-1 border"
                                 href="{% url 'write_review' item.book.id %}"
                                 >Review Book</a
                                 >
                           </p>
                              {% else %}
                           <p>
                              <strong> "{{ item.plan.name }}"</strong> (plan)
                                                            <br>

                              <a
                                 class="p-1 mt-2 border"
                                 data-toggle="collapse"
                                 href="#collapsePlanBooks{{item.plan.id}}"
                                 role="button"
                                 aria-expanded="false"
                                 aria-controls="collapsePlanBooks{{item.plan.id}}"
                                 >
                              Plan Details
                              </a>
                           </p>
                           <!--  Collapsable to display the books in each plan-->
                           <div
                              class="collapse"
                              id="collapsePlanBooks{{item.plan.id}}"
                              >
                              <div class="card card-body">
                                 <ul class="list-unstyled">
                                    {% for book in item.plan.books.all %}
                                    <li>
                                       <p>
                                          <strong>{{ book.title }}</strong>
                                          <a
                                             class="p-1 mt-1 border"
                                             href="{% url 'write_review' book.id %}"
                                             >Review Book</a
                                             >
                                       </p>
                                    </li>
                                    {% endfor %}
                                 </ul>
                              </div>
                           </div>
                           {% endif %}
                        </li>
                        {% endfor %}
                     </ul>
                  </td>
                  <td>€{{ order.order_total }}</td>
               </tr>
               {% endfor %}
            </tbody>
         </table>
      </div>
   </div>
</div>


TO DO:
User Stories
Wireframes
tests
Take out comms page
Styling profile page
Bug fixing






****************************to fix**************

***********styling**************


update styling in stripe_elements.js

FIX links on top of profile page

********functionality to fix************

>> fix admin for order


>> zadig is twice in books

> Depending on navbar check reviews section on book_datail

SERIOUS ONES

update small buttons with this throughout the app: p-2 mt-2 border






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


## Features
In this section, you should go over the different parts of your project, and describe each in a sentence or so.

### Existing Features
 Browsing, searching and filtering books 
        This functionality is mostly contained within the 'products' app. It allows a user to view all books currently available, filter through them by Genre and Language, as well as alphabetical order, price etc. Additionally, a user can see all details of a book displayed (book_details.html)
2.  Building Custom Plans
        Functionality is within the 'plans' app. This feature automatically generates a list of books (plan) and price, based on the criteria a user has picked. The criteria a user can pick are genres, languages and the plan duration (considering they receive 1 book per month, depending on the plan duration, they are signing up for 3, 6 or 12 months/books). The custom_plans view builds a plan for them, based on a randomized set of books matching their criteria. In case the database doesn't contain enough books matching their criteria, the plan is automatically adjusted to the number of books available, so that a user is not overcharged. The price is calculated at 10 EUR per book in a plan, and the plan overview a user sees also displays how much they're saving by going for the plan, instead of individual books. 
3.  Writing Reviews
        Registered and logged in users have the possibility to write reviews for books('reviews' app). This includes a rating on a scale of 1 to 5 (average of which is displayed when rendering book details, if available), a overview title of the review and space for comments. On their profile page, a user can see all the reviews they've personally left and delete some.
4.  Checkout
        Add to Bag ('bag' app) and Chechout ('checkout' app) functionality, allowing the user to buy individual books, plans or a combination of books and plans. The checkout functionality is fully integrated with Stripe (test version), allowing for users to pay quickly and efficiently. 
5. User Profiles
        User profiles functionality ('profiles' app), which renders a user's order history, delivery details and reviews left on books. It was desinged in a way that's enabling them to interact with their history with the website - whether it's to review orders, review books or go through past reviews.

### Features Left to Implement

With more time, the possibilities to expand this project are endless. Those are some of the features I would like to implement next:
- Filtering functionality, based on reviews ratings. This was considered for this first version of the project, but since the reviews are user-generated, rather than pre-uploaded, there isn't enough data to make it viable at this stage.
- More dynamic filtering of books on the Shop Books page through Ajax
- Expand the community page to allow for more interactivity - allow comment threads on individual reviews, functionality to like and upvote comments, possibility to ask questions and post comments outside of reviews alone.
- Re-design the bag functionality, so that the bag contents are saved if a user is registered and logged in. 
- Automated testing.

## Technologies Used
*HTML
    Templates Structure
*CSS
    Template Styling
*JQuery
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
<!-- In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

Contact form:
Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here. -->

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
SECRET_KEY: {your django secret key}
AWS_ACCESS_KEY_ID: {You can get it from Amazon}
AWS_SECRET_ACCESS_KEY: {You can get it from Amazon}
DATABASE_URL: {from Postgres Add-on in Heroku}
EMAIL_HOST_PASS: {from email provider}
EMAIL_HOST_USER: {email you're using}
STRIPE_PUBLIC_KEY: {from Stripe}
STRIPE_SECRET_KEY: {from Stripe}
STRIPE_SECRET_KEY: {from Stripe}
USE_AWS: True

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


