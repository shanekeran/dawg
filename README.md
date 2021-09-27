# Dawg
<i>The cool new dog supplies store</i>

Dawg is a full-stack application that contains CRUD functinality and built in stripe functionality to purchase products.

[View the live project by clicking here](http://shanekeran-dawg.herokuapp.com/)

![mockup of the website on different devices](wireframes/amiresponsive.png)

<span id="top"></span>

## Table of Contents
>1. [User Experience](#ux)
>2. [Database](#database)
>3. [Technology](#tech)
>4. [Testing](#testing)
>5. [Deployment](#deployment)
>6. [Credits](#credits)

<span id="ux"></span>
## User Experience (UX)
___
### **Overview**

I used user stories and the five planes of user experience design as a framework for planning, creating and refactoring the project.

### **User Stories**

*As a site user, I want to*

- clearly understand the purpose of the site upon entering for the first time.
- easily navigate the site so that I can find the pages and products I want quickly and with ease.
- have the ability to sort products alphabetically and by price.
- view the current total of shopping bag at any time and have the option to update or delete items.
- be able to create an account to save shipping information and view previous orders.
- contact dawg incase I have any questions or concerns.
- easily recover my password in the likely event that I forget it.
- receive a confirmation email when I have placed an order.

*As a site owner, I want to*

- give super users a straightforward process for adding or making changes to products on the site.
- easily add new store location information as the company expands throughout Ireland.
- store contact form submissions.
- only display the pages that are currently accessible to the user navigating the site.


### **Strategy**





### **Scope**

Features to be included on the website are:
- 

Features to be introduced at a later date:
- Connect the Google Maps API to the Locations page to pinpoint each store's location.
- Add a testimonials and FAQ (returns / shipping information) app in addition to my current two custom models.

### **Structure**

Dawg is a multi-page website, with certain pages only accessible to users that are logged in and features only available to super users.

1. Home

    The Home section contains a large logo and icons for each product category.

2. Products

    

3. Bag

    

4. Checkout

    

5. Login / Register

    

6. Profile (Logged In users only)

    

7. Product Management (Super users only)


8. Locations



9. Contact Us

    


### **Skeleton**

I used Balsamiq to create a wireframe for each device.

[Wireframe - Home page](wireframes/filename.png)

[Wireframe - Product](wireframes/filename.png)

[Wireframe - Contact](wireframes/filename.png)

[Wireframe - Location](wireframes/filename.png)

### **Surface**

#### Colour

My main colour theme is a mix of #F37A4D, #00000 and #FFFFFF.

![Main colour 1](wireframes/colours/color1.PNG)
![Main colour 2](wireframes/colours/color2.PNG)
![Button colour](wireframes/colours/color3.PNG)

#### Typography

I chose the Shrikhand font for my logo text because of its "groovy" and alternative feel, which I feel matches the tone of the site.

<a href="#top">Back to top.</a>
<span id="database"></span>

## Database
___
For this project I used postgres as my Database

### **Database schema**


<span id="tech"></span>

## Technologies Used
___

### **Languages**

- HTML5
- CSS3
- JavaScript
- Python

### **Frameworks, Libraries & Programs used**

1. Git

    Used for Version control.

2. GitHub

    Project files were pushed from Git to GitHub.

3. Gitpod

    I used Gitpod's dev environment to write the code for my project.

4. Bootstrap v4.4.1

    Bootsrap was heavily used throught the site to speed up development time. Most notably on the navigation bar, buttons, grid layout on each page, card components for the products page and various alignment / styling classes applied to elements on each page to minimise custom css needed.

5. Google Fonts

    Google Fonts was used to access the Shrikhand font.

6. Font Awesome

    Font Awesome was used to display various icons throughout the site.

7. Adobe Creative Suite

    This was used to create the home page dawg image, category images and the kennel images for the locations page.

8. Balsamiq

    Balsamiq was used to create the wireframes.

9. Am I Responsive?

    Used to create the image at the beginning of this readme, with the website displayed on various devices.

10. Heroku

    The live project was deployed to Heroku.

11. AWS

    AWS was used to store the static files for the deployed site.

12. Hover.css

    Hover.css classes were used to apply custom hover effects on the home page.

<a href="#top">Back to top.</a>
<span id="testing"></span>

## Testing
___

Please find all testing documentation in my [TESTING.md file](/TESTING.md)

<span id="Deployment"></span>

## Deployment
___

### **How to clone Dawg**

To clone this project from its [GitHub repository](https://github.com/shanekeran/dawg):

1. From the repository, click **Code**
2. In the **Clone >> HTTPS** section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2

```console
git clone https://github.com/shanekeran/dawg.git
```

6. Press Enter. Your local clone will be created
7. Create a file called env.py to hold your app's environment variables, which should contain the following:

```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<app secret key></app>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database name>")
os.environ.setdefault("EMAIL_ADDRESS", "<sender email address>")
os.environ.setdefault("PASSWORD", "<email address password></email>")
```
8. env.py must be listed in your .gitignore file to prevent your environment variables being pushed publicly
9. The app can now be run locally using

```console
python3 app.py
```

### **Heroku**

How I deployed the application on Heroku:

1. I navigated to [Heroku](https://www.heroku.com/)
2. Signed into my existing Heroku account. 
3. Selected "New" on the dashboard and then "Create new application" option as below:
4. Selected a name for my application, selected "Europe" as the region and clicked "Create app".
5. With the "Deploy" tab selected, "GitHub - Connect to GitHub" was chosen as the deployment method.
6. Making sure my GitHub profile was displayed, I clicked "connect" next to the GitHub repository for this project.
7. Then I navigated to the "Settings" tab and clicked on "Reveal Convig Vars".
8. Added in my configuration variables to Heroku.
9. Navigated back to the "Deploy" tab and selected "Enable Automatic Deploys" with the master branch selected from the dropdown box.
10. Then clicked on "Deploy Branch" also with master selected.
11. Site is deployed and any changes are automatically deployed each time they are updated and pushed to GitHub during development.

<a href="#top">Back to top.</a>
<span id="credits"></span>

## Credits
___

### **Code**

- W3Schools

    * [How to flip an image in CSS](https://www.w3schools.com/howto/howto_css_flip_image.asp)

- Hover.css

    * [Hover grow-rotate, skew-forward and float-shadow effects](https://ianlunn.github.io/Hover/)


- Code Institute

    * I heavily relied on the Boutique Ado walkthrough project to build the basics of this application


### Acknowledgements

- Fatima from Tutor support in the Code Institute for helping me transfer my data from my local database to my live database.

- My fellow students on Slack for their inspiration and help.

<a href="#top">Back to top.</a>