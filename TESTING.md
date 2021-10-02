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

<details><summary>- Have the ability to sort products alphabetically and by price.</summary>

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

content
<br/>

### Bag items displaying on unrelated toast success message : <span style="color: green;">Resolved</span>
content
<br/>

### Dropdown menu overflowing on small screens : <span style="color: green;">Resolved</span>
content
<details><summary>Click here to display image</summary>

![image](./readme_images/dropdown-menu.PNG)
</details>
<br/>

### Big difference in product image heights : <span style="color: green;">Resolved</span>
content
<details><summary>Click here to display image</summary>

![image](./readme_images/product-heights.PNG)
</details>
<br/>

### Occasional slow loading of dog kennel images on the locations page : <span style="color: red;">Unresolved</span>
content
<details><summary>Click here to display image</summary>

![image](./readme_images/slow-load.PNG)
</details>
<br/>

### Small section of Orange background colour appearing during page scroll for mobile devices : <span style="color: green;">Resolved</span>
content
<details><summary>Click here to display image</summary>

![image](./readme_images/background-bug.jpg)
</details>
<br/>