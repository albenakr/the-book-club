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


add max value to Plans> Models> Plan Duration 

if the default in Plan > plan_duration accurate

    plan_duration = models.ForeignKey('PlanDuration', default='3', on_delete=models.RESTRICT)
