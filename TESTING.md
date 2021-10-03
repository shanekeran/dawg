# Dawg: Testing
<span id="top"></span>

## Testing the User Stories
___

### Site User


<details><summary>Clearly understand the purpose of the site upon entering for the first time.</summary>

When a first time user lands on the home page, they'll see the main dawg logo and images depicting various products (one for each category). With this imagery and the shopping cart icon on the top right, it will be immediately evident that the site sells dog products.
</details>

<details><summary>Easily navigate the site so that I can find the pages and products I want quickly and with ease.</summary>

- The Home page is designed to allow the user to go directly to the product type they are interested in.
- The navigation menu provides easy access to all pages on the site and a search bar to find a specific item.
- On pages likely to involve some vertical scrolling, a back to top arrow has been placed to easily allow the user to return to the top of the page.
</details>

<details><summary>Have the ability to sort products alphabetically and by price.</summary>

- A sorting dropdown menu is featured on the product page allowing users to sort by price (low/high), catergory or alphabetically. This will be increasingly important as more products are added to the database.
- The lower navigation menu also gives users the option to go directly to All Products by price or by category, bypassing the need to use the sort dropdown menu.
</details>

<details><summary>View the current total of shopping bag at any time and have the option to update or delete items.</summary>

- On large screens, the shopping cart icon on the navigation menu will display the current total while the user is browsing anywhere on the site.
- A user on any device can click the shopping cart icon which will take them to their bag which shows the price of each item, delivery fee if applicable and the grand total cost. From this page the user can increase/decrease the quantity of a particular item or remove it from their bag all together.
</details>

<details><summary>Be able to create an account to save shipping information and view previous orders.</summary>

- Users can click the account logo and select register to create their own profile. On the profile page they cant save their personal information and view their order history.
- If a user proceeds to checkout and they are not logged in, they'll be presented with an option to create an account or to sign in. If the user is signed in, they'll be able to save the inputted information to their profile for future use.
</details>

<details><summary>Contact dawg incase I have any questions or concerns.</summary>

- Under the About section, there is a link to the Contact Us page where users can submit any questions or concerns to Dawg via the form.
</details>

<details><summary>Easily recover my password in the likely event that I forget it.</summary>

- There is a link on the login page for any user who has difficulty accessing their account, this link will take them to password reset page where they can input the email address associated to their account.
</details>
<br>

### Site Owner

<details><summary>Give site admins a straightforward process for adding or updating products on the site.</summary>

- Superusers can access the django admin panel by navigating to /admin but to make the process easier, I have included a product management page where they can add/edit products from the regular dawg interface.
- Super users can edit/delete specific products using the options available to them while on the product page. An edit and delete link has been put below each product card.
</details>

<details><summary>Easily add new store location information as the company expands throughout Ireland.</summary>

- I created a custom locations model within the locations app which allows superusers to add new stores to the locations page when they open. When the required details have been entered in the django admin panel, the new store will automatically appear on the locations page.
</details>

<details><summary>Store contact form submissions.</summary>

- Users can submit queries using the form on the Contact Us page. These submissions will automatically save to the database. Superusers can view these queries from the Django admin panel, where they will be displayed with the most recent queries at the top (Sorted by the date_sent value)
</details>

<details><summary>Only display the pages that are currently accessible to the user navigating the site.</summary>

When a User is not logged in:
- They can access all pages except the profile, product management or sign out page.


When a User is logged in:

- They can access all pages except the sign up page.
- They can only access the Product management page if they are a superuser.
</details>
<br>

## Issues and Bugs during development
___

### Images not loading after upload to AWS : <span style="color: green;">Resolved</span>

After setting up AWS S3 for the deployed version of my site, I noticed that 3 or 4 product images were not loading, even though the correct URL was present and the image was uploaded to AWS. After spending some time on it I discovered that after the upload, some images containing two words such as pup-harness, were stripped of their hyphen. The result was the file name containing a space "pup harness.jpg" which was the cause of my issue. I resolved this by renaming the file and adding the hyphen back in.
<br/>

### Bag items displaying on unrelated toast success message : <span style="color: green;">Resolved</span>
During testing I discovered that when users do certain actions such as submitting the contact form or signing in, the toast success message would also include the bag items. I felt this was unncessary and distracting from the actual success message. To remedy this I added a value of "non_product_page = True" to the context of the home page and within the toast_success file I added some logic to only include the bag items if there is no value for non_product page. Now when users submit the contact form or sign in, when they get redirected to the home page the toast success message only displays the relevant message. When a user adds a product to their bag while browsing the product page, the toast_success message will include the bag items.
<br/>

### Dropdown menu overflowing on small screens : <span style="color: green;">Resolved</span>
On smaller screens the dropdown menus for the About section were spilling over the edge of the screen. To remedy this I added left: -65px to override the existing left: 0px code being placed on the element. Since the below screenshot was taken I also adjusted the background color back to white and added a thin border.
<details><summary>Click here to display image</summary>

![dropdown menu partially off-screen](./readme_images/dropdown-menu.PNG)
</details>
<br/>

### Big difference in product image heights : <span style="color: green;">Resolved</span>
One the first issues I faced, was when I began adding products to my database. After loading all the product images and displaying them on the website, I noticed certain products had a major difference in height. I resolved this by adding a maximum height and width. The product cards with smaller images were then misaligned with those that had larger images so I added flex-grow to the card to prevent this.
<details><summary>Click here to display image</summary>

![products of varying height and misaligned](./readme_images/product-heights.PNG)
</details>
<br/>

### Occasional slow loading of dog kennel images on the locations page : <span style="color: red;">Unresolved</span>
During testing, I noticed an intermittent issues that occured very infrequently and randomly which was the dog kennel images not loading on the locations page. I imagine this was likely a result of clearing my cache and slow internet speed. Refreshing the page fixed the issue in the moment but I haven't been able to find a clear resolution yet for this problem. The image element contains alt text in case this occurs for the user viewing the page.
<details><summary>Click here to display image</summary>

![screenshot showing kennel images not loading](./readme_images/slow-load.PNG)
</details>
<br/>

### Small section of #F37A4D background colour appearing during page scroll for mobile devices : <span style="color: green;">Resolved</span>
While conducting responsive testing, I discovered while vertically scrolling on mobile devices, a small portion of #F37A4D background would appear for a couple of seconds at the bottom of page. I imagined this was due to the fact that the white background is applied on the overlay div, with the actual background colour of the whole page underneath being #F37A4D. To remedy this I added a class of bg-white to the body container.
<details><summary>Click here to display image</summary>

![screenshot depicting background color bug](./readme_images/background-bug.jpg)
</details>
<br/>

### Minimum and maximum product quantity can be bypassed by manual entry : <span style="color: red;">Unresolved</span>
When using the plus and minus buttons to increment/decrement product quantities, the buttons will be disabled for values less than 1 or greater than 99. If the user manually inputs a number outside of the minimum/maximum allowed value, while on the product detail page it won't accept the value but if done on the bag page, it will allow it.
<br/>

<a href="#top">Back to top.</a>

## Manual Testing
___


## Validation
___

The W3C Markup Validator, W3C CSS Validator and JSHint were used to validate my code to ensure no syntax errors were overlooked. For my Python code, I used the flake8 command within GitPod to make sure it met PEP8 standards.

<details><summary>Click here to view testing document</summary>

![Code validation test results](./readme_images/validation.PNG)
</details>
<br/>

- HTML Validator

    Overall, the HTML code passed after some minor refactoring. However 1 warning and two errors remain. The errors can be seen here:
    ![html validator error](./readme_images/product-management-error.PNG).
    These errors are related to the feature allowing users to add/update the product image from the product management page. As this is dynamically added by Django, I'm unable to access the label or id of id_image to change it so this error will remain. The warning is due to the empty heading elment on the checkout page (h1 class="text-light logo-font loading-spinner"). This contains the loading icon and due to time constraints I have chosen to skip this warning in favour of submitting this project on time.

- CSS Validator

    Base.css passed with 0 errors and 0 warnings.

-  JSHint

    JSHint revealed 0 errors. Initially it showed various missing semicolon warnings, these have now been applied.

- PEP8 / flake8

    Inputting the "python3 -m flake8" command will suggest multiple fixes required for migration files which can be ignored. It also flags the following for settings.py:
    +   ./dawg/settings.py:139:80: E501 line too long (88 > 79 characters)
    +   ./dawg/settings.py:142:80: E501 line too long (81 > 79 characters)
    +   ./dawg/settings.py:145:80: E501 line too long (82 > 79 characters)
    +   ./dawg/settings.py:148:80: E501 line too long (83 > 79 characters)

    These are strings such as 'django.contrib.auth.password_validation.MinimumLengthValidator' and I'll be leaving them as they are based on advice from the code institute slack community [here](https://code-institute-room.slack.com/archives/C7HS3U3AP/p1605890486174200).

    It also suggests removing the following:
    +   ./checkout/apps.py:8:9: F401 'checkout.signals' imported but unused
    +   ./checkout/webhooks.py:28:5: F841 local variable 'e' is assigned to but never used
    +   ./checkout/webhooks.py:31:5: F841 local variable 'e' is assigned to but never used

    I decided to also ignore these suggestions as I believe most likely they are needed but due to time constraints I havent got the time to test the site's functionality without them included.

## Responsive Testing
___

I used [Responsively](https://responsively.app/download/) and the chrome developer tools to test Dawg on a variety of screen sizes and orientations. All tests were successful, with the site retaining its function and design across the different device simulations.

## Browser Testing
___

Google Chrome was used throughout the development process. I tested Dawg on the latest versions of Microsoft Edge, Firefox and Safari(From iPad device only). The site functions well on all the browsers tested.

On Microsft Edge, the #F37A4D background colour appears if you click and drag the page upwards while at the bottom of the page. I demonstrated this within a short loom video [here](https://www.loom.com/share/b55e5a090bbb46f6b5bc102434671386). This only occurs on the Edge browser and is something I'll look into in the future.

## Google Lighthouse
___

Google lighthouse was ran on the main pages of the website. Overall I'm pleased with the results on desktop but the performance is lacking on mobile. The main cause for this is related to images. I plan on compressing the images further to alleviate this in the future to try bring these scores up and have the page speed improved for mobile.

<details><summary>Click here to view lighthouse scores</summary>

![Google lighthouse scores](./readme_images/lighthouse.PNG)
</details>
<br/>

<a href="#top">Back to top.</a>
