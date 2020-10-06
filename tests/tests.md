#Tests

Below is an overview of the testing done on the app. 

The most substantial error found was that the buttons, allowing the user to update quantity were not working as expected in the bag (while they still work well in the product_details page) - Point 4.2 from the tests below. 
This functionality was taken from the Boutique Ado project, where (as also confirmed by the tutors) this error is also present in the completed project. 
To address this issue, I've taken out the functionality for users to update the quantity directly from the bag - now if they want to update the quantity, they are redirected to the book_details page, where they can do so and add to bag with the updated quantity. While not an optimal solution, given the limited amount of time caused by the project deadline, this seems like the best solution to make sure the functionality is reachable without an error. 

1. Home Page and Navigation
    1. Clicked through all buttons on the navigation menu - both large screen and mobile versions to make sure all buttons lead where they're supposed to.
    2. Clicked on the 'Build Your Plan Button' on the Home page to make sure it works.
    3. Search was tested on both the navination manu for large screens and the navigation menu on mobile:
        * Searched for several terms through the search bar on both large and small screens.
        * Searched for author names - both first and last to make sure the search returned correct results in both cases.
        * Searched for words, only mentioned in book descriptions e.g. 'edition' to make sure we got results for these.
        * Searched for words, including non-English characters - e.g. "Honoré".
        * Searched for book titles to ensure those are working.

2. Products App 
    1. Reviewed page to make sure all books are displaying correctly when loaded.
    2. All filters (including genres, languages and the filter menu) were all clicked individually to make sure they display the correct results. 
    3. Extensive testing was done combining the different filters to make sure they work together as well.
    4. Book details page:
        * Reviewed page to make sure all details are displaying correctly.
        * Clicked 'Add to Bag' to make sure functionality works.
        * Tried adding to bag with a quantity of 340, -1 and 100 and got error messages that the quantity must be greater than 1 or below 99 as expected. 
        * Clicked on 'Write Review', which leads to a review form and after a review is completed redirects to the books details page and displays the review as expected.
        * Verified the average rating is calculated and displayed correctly when available; 'No ratings yet' is displayed when there are no reviews.
        * Clicked on 'Keep Shopping', which redirects to the 'Shop Books' page as expected.
        
3. Plans App
    1. Created a Plan multiple times, using different criteria to make sure the books returned match.
    2. Created a 12-month plan in categories with less books to make sure the plan was adjusted to less months if there are not enough books. 
    3. Attempted to create a plan in categories that have no books (English - Novels) to make sure the appropriate error message was displayed and no plan was created. 
    4. Double-checked in the admin that the plans we saved in the database when added to the bag.
    5. Double-checked in the admin that the plan was deleted if removed from the bag.
    6. Calculate several times that the 'savings' value returned by the plan is correct.

4. Bag App
    1. Testing Add to Bag:
        * Added Book to bag.
        * Added a different quantity of the same book to ensure the quantity was updated.
        * Added plan to bag.
    2. Tried to update the quantity to 104 and -4. ERROR found - the quantity buttons not working properly as they allow for values over 100 and below 1 to be submitted. To bypass this error, the functionality was deleted and instead the quantity buttons redirect to the book_details page, where the user can update the quantity without errors.
    3. Removed a plan and a book from the bag to make sure both functions work.
    4. Verified totals and subtotals are calculated correctly.

5. Authentication and Registation
    1. Went through the process of registering for an account several times to verify the process works and an email is sent.
    2. Logged in and out several times to verify the process works.
    3. Went through the process of resetting my password to make sure it works.

5. Checkout
    1. Tried submitting the checkout form without the required fields. As expected, I got a notification the fields are required. 
    2. Tried checking out without entering a card number. As expected, an error message was displayed that the card number is incomplete.
    3. Completed a checkout to verify the process works. 
        * Verified that an email confirmation is received.
        * Verified that the order appears on the user profile. 
        * Verified in Stripe that the webhook attempts were marked as succeeded.
        * Verified that the admin that the order appears there.
    4. Closed the tab while the order was being processed to test the webhooks. As expected, the order was registed in Stripe, the admin and I received an email confirmation.

6. User Profile
    1. Reviewed user profile for user with and without order history to ensure the profiles displayed correctly.    
    2. Reviewed user profile for user with and without and reviews to ensure the profiles displayed correctly. Error in the layout for the reviews section without reviews was found and fixed.
    3. Updated delivery details information to make sure the form updates correctly.

7. Reviews
    1. Submitted a review multiple times.
        * Verified the review is saved through the admin.
        * Verified the review is displaying on the user profile.
        * Verified the review is displaying on the book details page.
        * Verified the average rating is updating correctly.
    2. Tried submitting a review with a title and text above the maximum character limit. Error messages displayed as expected and the review was not submitted.
    3. Deleted reviews from the user profile page to ensure the delete function is working well. 
        * Verified it's deleted in the admin.

8. Additional testing
    1. Tried accessing the checkout as a non-authenticated user by adding 'checkout' to the URL to verify login will be required. I was asked to sign up as expected.
    2. Tried accessing the profile view as a non-authenticated user by adding 'profile' to the URL to verify login will be required. I was asked to sign up as expected.
    3. Tried going to non-existing pages by adding random characters at the end of the URL. As expected, I was redirected to the home page.