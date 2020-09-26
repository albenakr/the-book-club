Photos:

Photo by Stanislav Kondratiev on Unsplash
Photo by Jaredd Craig on Unsplash

Filtering on books - currently doesn't take into account french letters, to fix - try unicode

Search is working, but when you add a filter on top of it, it stops working..

Building filter functionality:
https://www.youtube.com/watch?v=n1_MQiSXyxw&list=PLLRM7ROnmA9EGO3TOlWLgrc46EhTgj1Ih&index=6
https://github.com/justdjango/djfilter/blob/master/core/views.py

https://www.youtube.com/watch?v=G-Rct7Na0UQ


Another way of doing the filtering to explore:
That's correct. You could store the original queryset though each time you filter so that you have the last queryset from before the filter was applied. However in order to do this without refreshing the page every time you would need Ajax or some sort of JavaScript
My advice would be to return the entire queryset to the template, and filter everything with JavaScript.
You would want a JavaScript function that takes in your entire list of products that was returned from The view, and returns a subset of those products based on filtering through them. You don't even really need to make another call to the database. Just return all products by default and then whatever filters the user selects on the front-end can be applied with your JavaScript function

Comment multiple Lines
Shift + Alt + A


https://github.com/ckz8780/boutique_ado_v1

lsof -t -i tcp:8000 | xargs kill -9

4242 4242 4242 4242


Plan image:
<span>Photo by <a href="https://unsplash.com/@sincerelymedia?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Sincerely Media</a> on <a href="https://unsplash.com/s/photos/books?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>
Photo by Sincerely Media on Unsplash


****************************to fix**************

***********styling**************

to review allauth formatting from Code Institute in base.css(the main one)

Shop Books Button is moving in weird ways

update styling in stripe_elements.js

********functionality************

>> fix admin for order

>> fix admin for plans


>> put max length on book description model

>> when people are clicking on 'See book' or the photo for 'book email' from custom plan - add button on book_detail page to point to custom_plan instead of 'Keep shopping'

>> Back to Top Button for Community/Reviews page


OrderLiteItem model - currently both book and plan are not compulsory, so someone could submit an order without either

>> fix redirect on add_plan_to_bag


SERIOUS ONES

>>Reviews Section - it's not throwing error messages properly

>>iterate through plan books on profile.html page

>> Reviews - function to calculate average rating





Add max dimensions to reviews cards, so they're not too big if the comment is long
