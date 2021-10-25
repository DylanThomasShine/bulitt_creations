<h1 text-align="center"><strong>Bulitt</strong> Creations</h1>

![Portfolio website](/media/bulittcreationslogoweb.jpg) 



# Intro


<p align="center">This task is the final project for the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course. 
This project is an eCommerce shop front to host my graphic design and artistic capabilities. The name chosen for the website is Bulitt Creations, which is the name I have used to create any art since I was 20 years old</p>

<p align="center">The site is worked within Django structure, sent live on Heroku, utilizes AWS S3 to have media and static records. Locally, it utilizes the inherent Django Db.sqlite3 information base, though when conveyed live it uses Heroku's Postgres information base. Authentication functionality is provided by Django's Allauth: administrator superuser can add and alter things in the Products and Categories applications, while visiting clients can enlist and login, accessing vestige depictions and their request history in the Checkout and Profile applications.</p>


- [Goals](#goals)
- [Target Audience](#target-audience)
- [Business Goals](#business-goals)
- [Customer goals](#customer-goals)
- [User Stories](#user-stories)
    + [Viewing and Navigation](#viewing-and-navigation)
    + [Registration and User Accounts](#registration-and-user-accounts)
    + [Sorting and searching](#sorting-and-searching)
    + [Admin and Store Management](#admin-and-store-management)
- [Design](#design)
    + [Font](#font)
    + [Color Scheme](#color-scheme)
    + [Wireframes](#wireframes)
- [Product Features](#product-features)
- [Users Features](#users-features)
- [User Stories Testing](#user-stories-testing)
- [Error pages testing](#error-pages-testing)
    - [404](#404)
    - [500](#500)
- [Requirements](#requirements)
- [Local deployment](#local-deployment)
- [Deployment on Heroku](#deployment-on-heroku)
    

<p><h1 align="center">USER EXPERIENCE</h1></p>

# Goals

<p>The main goal of Bulitt Creations is to showcase and sell my artwork.<br>
   The user can request a design, creation, portrait from the designer.<br>
   Also, through the website, a user may be inspired to create their own work from some of mine.</p>

# Target Audience

- Users aged 8 to 80
- Users interested in creativity and design.
- Users with interest in collecting adn displaying works of art and creations.

# Business Goals

- To create a platform that enables the prospective client to find and purchase the product they like.
- Offer a portrait or a design feature to encourage the user to interact more with the designer.
- In order to increase people's interest, encourage users to register.
- Offer a presentable design of the website. 
- Offer a simple and easy to use and navigate interface to attract the user to return for future visits.

# Customer goals

- Finding creations they would love to keep.
- Buy a creation through an easy payment flow system.
- Register their account to take requests for designs they may like me to produce.
- See their previous purchases.
- Connect their own social media account to one they have created here.

# User Stories

### Viewing and Navigation		
- As a shopper I want to be able to view the list of creations with the option to purchase them.
- As a shopper I want to be able to view individual product details to identify the price and description.
- As a shopper I want to be able to quickly identify special offers and new work/creations to take advantage of special savings on products I'd like to buy.
- As a shopper I want to be able to easily view the total of my purchases at any time to see the history of my purchases and how much I spent.

### Registration and User Accounts  
- As a registered shopper I want to be able to easily register for an account so I can have a personal account, be able to see what I purchased.
- As a registered shopper I want to be able to easily login or logout so I can access my personal account information.
- As a registered shopper I want to be able to easily recover my password in case I forget it so I can recover access to my account.
- As a registered shopper I want to be able to receive an email confirmation after registering so I can verify that my account registration was successful.
- As a registered shopper I want to be able to have a personalised user profile so I can view my personal order history and order confirmations and save my payment information.

### Sorting and searching  
- As a shopper I want to be able to sort the list of available products so I can easily identify the best rated, best priced and categorically sorted creations  
- As a shopper I want to be able to sort a specific category of products so I can find best priced or best rated product in a specific category or sort the product in that category by name
- As a shopper I want to be able to sort multiple categories of products simultaneously so I can find the best priced or best rated products across board categories.
- As a shopper I want to be able to search for a product by name or description so I can find a specific product I'd like to purchase.

### Purchasing and Checkout  
- As a registered shopper I want to be able to easily select quantity of a product when purchasing it so I can ensure I am selecting correct product and a correct quantity.
- As a registered shopper I want to be able to view items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive.
- As a registered shopper I want to be able to adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout.
- As a registered shopper I want to be able to easily enter my payment information so I can check out quickly and with no hassle.
- As a registered shopper I want to be able to feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase.
- As a registered shopper I want to be able to view an order confirmation after checkout so I can verify that I have not made any mistakes.
- As a registered shopper I want to be able to receive an email confirmation after checking out so I can keep the records of my purchases.

### Admin and Site Management  
- As the site owner I want to be able to add a new creation as this would enable me to add new items to my site.
- As the site owner I want to be able to Edit/Update product to apply any changes, be it in price, description, image or any other criteria.
- As the site owner I want to be able to delete a product and remove a product if they are no longer available.

# Design

## Font

Throughout the project there is only one font used, which is Lato. The aim is to make this website as minimalist and clean as possible, I used shadows in CSS and HTML to make certain headings stand out more.

## Color Scheme

The main color used throughout the page is pale and light, almost white, as this ensures best effectivens of the design style. Black and gray is used to highlight Titles, headings and general top page information. Other grey and black colours used were to create the frame surrounding each picture. The remaining colours are used for hovers, warnings and small buttons such as edit or remove.

![Colur Chart](/media/colour_chart.jpg) 

## Wireframes
<br>

<details><summary>Mobile Tablet and Desktop</summary>
<br>
 
[Bulitt Creations Wireframes](https://github.com/DylanThomasShine/bulitt_creations/blob/main/Bulitt%20Creations%20Wireframes.pdf)
</details>
<br><br>

## Technologies
<br>

[![Gitpod](https://img.shields.io/badge/IDE-Gitpod-blue)](https://www.gitpod.io/)<br>
[![CSS](https://img.shields.io/badge/Styling-CSS-blueviolet)](https://www.w3schools.com/css/)<br>
[![AWS Services](https://img.shields.io/badge/AWS%20-Services-orange)](https://aws.amazon.com/)<br>
[![JavaScript](https://img.shields.io/badge/JS%20Functionality-JS-darkgreen)](https://jquery.com/)<br>
[![HTML](https://img.shields.io/badge/Mark%20up%20text-HTML-yellow)](https://www.w3schools.com/html/html_intro.asp)<br>
[![Heroku](https://img.shields.io/badge/App%20Hosting-Heroku-%237B68EE)](https://www.heroku.com/home)<br>
[![Github](https://img.shields.io/badge/Remote%20code-Github-white)](https://github.com/)<br>
[![Balsamiq](https://img.shields.io/badge/Wireframes-Balsamiq-Orange)](https://balsamiq.com/wireframes/)<br>
[![Photoshop](https://img.shields.io/badge/Photoediting-Photoshop-lightblue)](https://www.adobe.com/ie/products/photoshop.html)<br>
[![Django](https://img.shields.io/badge/Microframework-Django-%238B0000)](https://www.djangoproject.com/)<br>
[![Shields](https://img.shields.io/badge/Readme%20Badges-Shields-lightgrey)](https://shields.io/)<br>
[![JShint](https://img.shields.io/badge/JS%2FjQuery%20Validator-JSHint-%23008e94)](https://jshint.com/)<br>
[![SQlite3](https://img.shields.io/badge/SQLite-Production%20Database-yellowgreen)](https://www.sqlite.org)<br>
[![Bootstrap](https://img.shields.io/badge/Design%20Framework-Bootstrap-%23F5A4A7)](https://getbootstrap.com/)<br>
[![Pep8 Online](https://img.shields.io/badge/Python%20Validator-PEP8%20online-white)](http://pep8online.com/)<br>
[![Python](https://img.shields.io/badge/Back%20end%20programming-Python-%09%23008000)](https://www.python.org/)<br>
[![W3C CSS Validator](https://img.shields.io/badge/CSS%20Validator-W3C%20CSS%20Validator-darkred)](https://jigsaw.w3.org/css-validator/)<br>
[![W3C HTML Validator](https://img.shields.io/badge/HTML%20Validator-W3C%20HTML%20Validator-red)](https://validator.w3.org/)<br>

<br><br>

## Features

- Products to purchase through an ecommerce system
- Administration panel so superuser can add, edit and delete products
- Profile page where registered user can see their order purchase history


All pages share navigation bar with logo to the left, which once clicked on, takes you home from any page.

In the middle there are four call to action buttons:
<br>
-  View Options- Option that returns a dropdown list with Items sorted in accordance to price, rating, alphabetically and All.
- View Catagories -  Upon clicking on this option the user will be able to choose from Portraits, Paintings, Photography, Macro, 2000AD, Sketches, Caracatures and finally all Creatioins. 
- View New Catagories - By clicking on this the user will be faced with three choices, Recently Added, Special Offers and All Creations.
- Request Creation - this dropdown contains only position, which let's the User order a creation, from a Portrait of themselves to a sketch of a favourite, charatcter, hero etc..
<br>

To the right corner in the Main view there are two CTA buttons: My Account and a Shopping Bag.
<br>
- My Account:
For the registered and while logged in user that is not a superuser, they will be able to Check out their Profile, which contains history of purchases. By clicking on this option, the logged in user will be able to log out from their session.
For the regisered and logged in as a superuser, the user will be able to do all of the above plus Manage the main creations of the ecommerce. 
- Shopping Bag.
This option is available to both logged in and not logged in users. The difference is, only logged in user will be able to successfully check out with the items, as this option is for the time being only made available to the logged in user.
<br>

## Future Features

- Request from a User to ask for a creation for themselves.
- The ability to contact the superuser directly through a simple contact form.

<br><br>

# Testing
<br>

## Product Features
<br>

|  Feature |  Action | Effect |
|---|---|---|
| Logo (upper left corner)  |  Hover over |  <ul><li>The address on hover is showing as home page</li></ul> |
| Search bar  |  Entered "Lord of the Rings", |<ul><li> one creation is listed under this name - correct</li><li>The summary shows message "1 Creation(s) found for "Lord of the Rings"</ul>|
|  Explore Creations, bringing to all creations page|  Click on Explore Creations button |  <ul><li>Linked correctly</li></ul>  |
| View Options  |  Click on By Price |  <ul><li>Items appear sorted ascending, from low price to high</li></ul> |
|   |  Click on By Rating |  <ul><li>Items appear sorted descending, from high rating to low</li></ul> |
|   |  Click on Alphabetically |  <ul><li>Categories of Items become sorted alphabetically</li></ul> |
|   |  Click on All|  <ul><li>All items are displayed, sorted by SKU</li></ul> |
| View Catagories  |  Click on Portraits |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul> |
|   |  Click on Paintings|  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul>|
|   |  Click on Photography |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul>|
|   |  Click on Macros |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul> |
|   |  Click on 2000AD |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul> |
|   |  Click on Sketches |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul> |
|   |  Click on Caricatures |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul> |
|   |  Click on All Creations| <ul><li>All Creations are displaying</li></ul> |
| View New Creations |  Click on Recently Added |  <ul><li>New creations are displayed, the badge on top of the page states same.</li></ul> |
|   |  Click on Special Offers |  <ul><li>Special Offers are displayed, along with badge</li></ul> |
|   |  Click on All Creations |  <ul><li>bringing to all creations page, heading shows "CREATIONS""</li></ul> |
| Request Creation |  Click on Request Creation |  <ul><li>Request a Creation form is displayed along with "REQUEST MANAGEMENT" heading</li></ul> | 
|   
| My Account  |  Click on Register |  <ul><li>Sign up form appears</li><li>Form sends</li><li>Confirmation email appears in the email box</li><li>Clicked on the confirmation email - Confirm email address page appears</li><li>Logged in with newly created account - the success message appears and I am now logged in</li><li>Upon clicking Confirm, a success message appears and a signing page is returned</li></ul> |
|   |  <h3>Click on Login</h3> |  <ul><li>The address on hover is showing as home page</li></ul> |
| Bag  |  Bag empty |  <ul><li>Click on Continue Browsing button, brings me back to all Creations page</li></ul> |
|   |  <h3>Bag with Content</h3>  | <ul><li>Increase and Decrease quantity buttons work</li><li>Price updates when Update option is clicked</li><li>Price in Grand total Updates over the 10% Delivery</li><li>Free Delivery threshold is calculated correctly and called back to user</li></ul> |
| Footer  |  Test all of the Social Media/Contact links  |  <ul><li>All open in a separate tabs and bring the user to the said website</li></ul> |
| | <h3>Home Page</h3> | |
| Explore Creations button  |  Clicked on |  <ul><li>Brings me to a page with all creations</li></ul> |
| | <h3>All Creations Page</h3>  | |
| View Options Dropdown  |  Sort testing each Condition |  <ul><li>Price (low to high) - sorts according to price, from cheapest to dearest</li><li> Price (high to low) - sorts according to price, from dearest to cheapest</li><li>Rating (low to high) - sorts rating from lowest</li><li>Rating (high to low) - sorts rating from highest.</li><li>Name (A-Z) - sorts Products alphabetically</li><li>Name (Z-A) - sorts products reverse-alphabetically</li><li>Category (A-Z) - sorts Categories of products alphabetically</li><li>Category (Z-A) - sorts Products by Categories sorted reverse-alphabetically</li></ul> |
| Superuser - editing the creation details  |  Click on the Edit option underneath one of the creations |  <ul><li>A Manage Creations Edit a Creation form is rendered and a warning message is triggered in upper right corner</li><li>Changed Category and Name,saved</li><li>Name and Category successfully changed, confirmed with a success toast rendered in upper right corner </li></ul> |
|   |  Click on the Delete option |  <ul><li>Product is immediately deleted and a success toast confirming deletion is rendered in the upper right corner of the page </li></ul>|
| Adding a Creation to the bag  |  Click on the Creation and click Add to Bag |  <ul><li>Bag total updates to the correct amount, success toast confirms the Creation was added to the bag </li></ul> |
| Navigating from Creation Detail back to All Creations |  Click on the Continue Browsing button |  <ul><li>A page with all the Creations is rendered</li></ul> |
| Checking out  |  Click on the Shopping Bag, click on Secure Checkout |  <ul><li>Non registered user - a sign in page renders with option to register, if user is not yet registered</li><li>Registered User - A Checkout page is rendered with most information saved as per users account. User can also see the Order Summary to the right of the form</li><li>Entered card details and name, after which clicked on the Complete Transaction button</li><li>A thank you page is rendered, with a summary of order as well as the success toast renders in upper right corner</li><li>Confirmation email arrives to the email box</li></ul> |

### For testing the Stripe checkout use the following:

```bash
 Card number: 4242 4242 4242 4242
 CVC_: any 3 digits
 Card expiry date: any future date
 ZIP/Postcode: any 5 digits
``` 

