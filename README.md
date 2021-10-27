<p><h1 text-align="center"><strong>BULITT</strong> CREATIONS</h1></p>

![Portfolio website](/media/bulittcreationslogoweb.jpg) 



# Intro


<p align="center">This task is the final project for the 'Full Stack Frameworks with Django' module of the Code Institute Full Stack Software Development course. 
This project is an eCommerce shop front to host my graphic design and artistic capabilities. The name chosen for the website is Bulitt Creations, which is the name I have used to create any art since I was 20 years old</p>

<p align="center">The site is worked within Django structure, sent live on Heroku, utilizes AWS S3 to have media and static records. Locally, it utilizes the inherent Django Db.sqlite3 information base, though when conveyed live it uses Heroku's Postgres information base. Authentication functionality is provided by Django's Allauth: administrator superuser can add and alter things in the Creations and Categories applications, while visiting clients can enlist and login, accessing vestige depictions and their request history in the Checkout and Profile applications.</p>


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
- [Creation Features](#creation-features)
- [Users Features](#users-features)
- [User Stories Testing](#user-stories-testing)
- [Error pages testing](#error-pages-testing)
    - [404](#404)
    - [500](#500)
- [Requirements](#requirements)
- [Local deployment](#local-deployment)
- [Deployment on Heroku](#deployment-on-heroku)
    

<p><h1 align="center"><strong>USER</strong> EXPERIENCE</h1></p>

# Goals

<p>The main goal of Bulitt Creations is to showcase and sell my artwork.<br>
   The user can contact the Creator to leave a message<br>
   The user can request a design, creation, portrait from the designer.<br>
   Also, through the website, a user may be inspired to create their own work from some of mine.</p>

# Target Audience

- Users aged 8 to 80
- Users interested in creativity and design.
- Users with interest in collecting and displaying works of art and creations.

# Business Goals

- To create a platform that enables the prospective client to find and purchase the Creation they like.
- Offer a portrait or a design feature to encourage the user to interact more with the designer.
- Offer a service that will allow the user to request a creation from the Creator.
- In order to increase people's interest, encourage users to register.
- Offer a presentable design of the website. 
- Offer a simple and easy to use and navigate interface to attract the user to return for future visits.

# Customer goals

- Finding creations they would love to keep.
- Buy a creation through an easy payment flow system.
- Register their account to take requests for designs they may like me to produce.
- See their previous purchases.
- Contact the Creator with a personal message.

<p><h1 align="center"><strong>USER</strong> STORIES</h1></p>

### Viewing and Navigation		
- As a shopper I want to be able to view the list of creations with the option to purchase them.
- As a shopper I want to be able to view individual Creation details to identify the price and description.
- As a shopper I want to be able to quickly identify special offers and new work/creations to take advantage of special savings on Creations I'd like to buy.
- As a shopper I want to be able to contact the Creator.
- As a shopper I want to be able to request a personal creation for myself.
- As a shopper I want to be able to easily view the total of my purchases at any time to see the history of my purchases and how much I spent.

### Registration and User Accounts  
- As a registered shopper I want to be able to easily register for an account so I can have a personal account, be able to see what I purchased.
- As a registered shopper I want to be able to easily login or logout so I can access my personal account information.
- As a registered shopper I want to be able to easily recover my password in case I forget it so I can recover access to my account.
- As a registered shopper I want to be able to receive an email confirmation after registering so I can verify that my account registration was successful.
- As a registered shopper I want to be able to have a personalised user profile so I can view my personal order history and order confirmations and save my payment information.

### Sorting and searching  
- As a shopper I want to be able to sort the list of available Creations so I can easily identify the best rated, best priced and categorically sorted creations  
- As a shopper I want to be able to sort a specific category of Creations so I can find best priced or best rated Creation in a specific category or sort the Creation in that category by name
- As a shopper I want to be able to sort multiple categories of Creations simultaneously so I can find the best priced or best rated Creation across board categories.
- As a shopper I want to be able to search for a Creation by name or description so I can find a specific Creation I'd like to purchase.

### Purchasing and Checkout  
- As a registered shopper I want to be able to easily select quantity of a Creation when purchasing it so I can ensure I am selecting correct Creation and a correct quantity.
- As a registered shopper I want to be able to view items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive.
- As a registered shopper I want to be able to adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout.
- As a registered shopper I want to be able to easily enter my payment information so I can check out quickly and with no hassle.
- As a registered shopper I want to be able to feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase.
- As a registered shopper I want to be able to view an order confirmation after checkout so I can verify that I have not made any mistakes.
- As a registered shopper I want to be able to receive an email confirmation after checking out so I can keep the records of my purchases.

### Admin and Site Management  
- As the site owner I want to be able to add a new creation as this would enable me to add new items to my site.
- As the site owner I want to be able to Edit/Update Creationto apply any changes, be it in price, description, image or any other criteria.
- As the site owner I want to be able to delete a Creation and remove a Creation if they are no longer available.

<p><h1 align="center">DESIGN</h1></p>

## Font

Throughout the project there is only one font used, which is Lato. The aim is to make this website as minimalist and clean as possible, I used shadows in CSS and HTML to make certain headings stand out more.

## Color Scheme

The main color used throughout the page is pale and light, almost white, as this ensures best effectivens of the design style. Black and gray is used to highlight Titles, headings and general top page information. Other grey and black colours used were to create the frame surrounding each picture. The remaining colours are used for hovers, warnings and small buttons such as edit or remove.

![Colur Chart](/media/colour_chart.jpg) 

## Wireframes
<br>

<details><summary><strong>Mobile Tablet and Desktop</strong></summary>
<br>
 
## [Bulitt Creations Wireframes](https://github.com/DylanThomasShine/bulitt_creations/blob/main/Bulitt%20Creations%20Wireframes.pdf)
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

- Creations to purchase through an ecommerce system
- Administration panel so superuser can add, edit and delete Creations
- Profile page where registered user can see their order purchase history
- Request page so users can upload an image they would like the Creator to produce for them
- Contact page so users cab reach out to the Creator and ask for a specific image to be created
- The ability to upload an image for the Creator to work from


All pages share navigation bar with logo to the left, which once clicked on, takes you home from any page.

In the middle there are four call to action buttons:
<br>
- Options- Option that returns a dropdown list with Items sorted in accordance to price, rating, alphabetically and All.
- Catagories -  Upon clicking on this option the user will be able to choose from Portraits, Paintings, Photography, Macro, 2000AD, Sketches, Caracatures and finally all Creatioins. 
- New - By clicking on this the user will be faced with three choices, Recently Added, Special Offers and All Creations.
- Contact - this dropdown contains only one position, which let's the User contact the Creator and leave a message.
- Request - this dropdown contains only one position, which let's the User order a creation, from a Portrait of themselves to a sketch of a favourite, charatcter, hero etc..
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

- For users to be able to link a social media page to their profile.
- To offer the User a platform to sell their own creations on the site.

<br><br>

<p><h1 align="center">TESTING</h1></p>

![Testing Images](/media/testimages.jpg) 

## Creation Features
<br>

|  <h2>Feature</h2> |  <h2>Action</h2> | <h2>&nbsp; &nbsp;&nbsp; Effect</h2> |
|---|---|---|
| Logo (upper left corner)  |  Hover over |  <ul><li>The address on hover is showing as home page</li></ul> |
| Search bar  |  Entered "Lord of the Rings", |<ul><li> one creation is listed under this name - correct</li><li>The summary shows message "1 Creation(s) found for "Lord of the Rings"</ul>|
|  Explore Creations, bringing to all creations page|  Click on Explore Creations button |  <ul><li>Linked correctly</li></ul>  |
|  Options  |  Click on By Price |  <ul><li>Items appear sorted ascending, from low price to high or from high price to low</li></ul> |
|   |  Click on By Rating |  <ul><li>Items appear sorted descending, from high rating to low</li></ul> |
|   |  Click on Alphabetically |  <ul><li>Categories of Items become sorted alphabetically</li></ul> |
|   |  Click on All|  <ul><li>All items are displayed, sorted by SKU</li></ul> |
|  Catagories  |  Click on Portraits |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are at.</li></ul> |
|   |  Click on Paintings|  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul>|
|   |  Click on Photography |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul>|
|   |  Click on Macros |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on 2000AD |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Sketches |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on Caricatures |  <ul><li>Creations from that Category are displayed, the badge on top of the page also states what Category we are currently in.</li></ul> |
|   |  Click on All Creations| <ul><li>All Creations are displayed</li></ul> |
|  New |  Click on Recently Added |  <ul><li>New creations are displayed, the badge on top of the page states same.</li></ul> |
|   |  Click on Special Offers |  <ul><li>Special Offers are displayed, along with badge</li></ul> |
|   |  Click on All Creations |  <ul><li>Bringing to all creations page, heading shows "CREATIONS""</li></ul> |
| Order |  Click on Contact Form |  <ul><li>Contact form is displayed along with "CONTACT FORM" heading</li></ul> |
| Request |  Click on Order Form |  <ul><li>Request form is displayed along with "REQUEST FORM" heading</li></ul> |   
| My Account  |  Click on Register |  <ul><li>Sign up form appears</li><li>Form sends</li><li>Confirmation email appears in the email box</li><li>Clicked on the confirmation email - Confirm email address page appears</li><li>Logged in with newly created account - the success message appears and I am now logged in</li><li>Upon clicking Confirm, a success message appears and a signing page is returned</li></ul> |
|   |  Click on Login |  <ul><li>The address on hover is showing as home page</li></ul> |
| Bag  |  Bag empty |  <ul><li>Click on Continue Browsing button, brings me back to all Creations page</li></ul> |
|   |  Bag with Content | <ul><li>Increase and Decrease quantity buttons work</li><li>Price updates when Update option is clicked</li><li>Price in Grand total Updates over the 10% Delivery</li><li>Free Delivery threshold is calculated correctly and called back to user</li></ul> |
| Footer  |  Test all of the Social Media/Contact links  |  <ul><li>All open in a separate tabs and bring the user to the said website</li></ul> |
| | <h3>Home Page</h3> | |
| Explore Creations button  |  Clicked on |  <ul><li>Brings me to a page with all creations</li></ul> |
| | <h3>All Creations Page</h3>  | |
| Options Dropdown  |  Sort testing each Condition |  <ul><li>Price (low to high) - sorts according to price, from cheapest to dearest</li><li> Price (high to low) - sorts according to price, from dearest to cheapest</li><li>Rating (low to high) - sorts rating from lowest</li><li>Rating (high to low) - sorts rating from highest.</li><li>Name (A-Z) - sorts Creations alphabetically</li><li>Name (Z-A) - sorts Creations reverse-alphabetically</li><li>Category (A-Z) - sorts Categories of Creations alphabetically</li><li>Category (Z-A) - sorts Creations by Categories sorted reverse-alphabetically</li></ul> |
| Superuser - editing the creation details  |  Click on the Edit option underneath one of the creations |  <ul><li>A Manage Creations Edit a Creation form is rendered and a warning message is triggered in upper right corner</li><li>Changed Category and Name,saved</li><li>Name and Category successfully changed, confirmed with a success toast rendered in upper right corner </li></ul> |
|   |  Click on the Delete option |  <ul><li>Creation is immediately deleted and a success toast confirming deletion is rendered in the upper right corner of the page </li></ul>|
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



![Checkout Success Images](/media/checkoutimage.jpg)

<br>

# Users Features

|  <h2>Feature</h2> |  <h2>Action</h2> | <h2>&nbsp; &nbsp;&nbsp; Effect</h2> |
|---|---|---|
| Registration  | Click on My Account and My Profile  |  <ul><li>Click on MyAccount and Register</li><li>A Sign Up form is rendered, fill in the blanks</li><li>User Exists - an error is rendered above the user name "User is already registered with this email address"</li><li>Register unregistered email address, press send</li><li>A confirmation email is sent to the provided email address</li></ul> |
| Login  |  Click on My Account and My Profile | <ul><li>Click on MyAccount and Login</li><li>A Sign In form renders</li><li>Wrong Password entered, an error is generated "The username and/or password you specified are not correct"</li><li>Log in with the correct password</li><li>Home page is rendered</li></ul>  |
| Logout  | Click on My Account and My Profile  | <ul><li>Click on MyAccount and Logout</li><li>A page renders confirming "Are you sure you want to sign out"</li><li>Click Sign Out</li><li>A success toast is rendered in upper right corner of the screen</li></ul>  |
| Change Password  |  Click on My Account and My Profile |  <ul><li>Click on MyAccount and Login</li><li>Click Forgot Password</li><li>Enter email you are registered under</li><li>A page renders confirmation "We have sent you an email. Please contact us if you do not receive it within a few minutes"</li><li>When clicked, it returns a change password form</li></ul> |
| View profile  |  Click on My Account and My Profile | <ul><li>Log in and click on MyAccount and My Profile</li><li>My Profile page is rendered with Default Delivery Informaton and history of purchasees</li></ul> |
| Update profile  |  Click on My Account and My Profile |  <ul><li>While in My Profile, fill in the new details and click Update Information</li><li>A success toast is rendered in upper right corner of the screen</li><li>Information is updated</li></ul> |

<p><h1 align="center"><strong>USER</strong> STORIES TESTING</h1></p>

![User Story image](/media/storyimage.jpg)

 | <h2>User Story</h2>                                                                                                                                                                                  | <h2>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Testing<h2>                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| As a shopper I want to be able to view the list of creations to purchase some                                                                                                                 | <ul><li>The list of creations is available as per below</li><li>Home page - click on Explore Creations button.</li></ul>                                                                                                                                                                                                                                                               |
| As a shopper I want to be able to view individual creatioin details to identify the price and description                                                                                      | <ul><li>While at All  click on a sample Creation</li><li>The Price and Description is clearly visible</li></ul>                                                                                                                                                                                                                                                                                                                      |
| As a shopper I want to be able to quickly identify special offers to take advantage of special savings on creations I'd like to buy                                                           | <ul><li>One of the CTA buttons on navbar is marked as New and is visible from every page of the website</li></ul>                                                                                                                                                                                                                                                                                                                |
| As a shopper I want to be able to easily view the total of my purchases at any time to see the history of my purchases and how much I spent                                                  | <ul><li>This feature can be accessed on My Account -> My Profile</li><li>History of orders is visible next to the profile details</li></ul>                                                                                                                                                                                                                                                                                                 |
| As a registered shopper I want to be able to easily register for an account so I can have a personal account, be able to see what I purchased                                                | <ul><li>As soon as the unregistered user is ready to check out and complete a purchase, the site renders a Sign Up call to action page</li><li>By clicking on My Account and Register, the unregistered user may easily register and from then on use account to keep record of their purchases</li></ul>                                                                                                                                   |
| As a registered shopper I want to be able to easily login so I can access my personal account information                                                                                    | <ul><li>By clicking on My Account, user's acount is easily accessible and editable</li></ul>                                                                                                                                                                                                                                                                                                                                                |
| As a registered shopper I want to be able to easily recover my password in case I forget it so I can recover access to my account                                                            | <ul><li>Upon login attempt there is a 'Forgot Password' option</li><li>From there on, the user may request a password resetting email</li><li>Upon receipt of the email, user will be able to click on the link and easily amend or set a new password</li></ul>                                                                                                                                                                            |
| As a registered shopper I want to be able to receive an email confirmation after registering so I can verify that my account registration was successful                                     | <ul><li>Shortly after registration, a confirmation email arrives to the inbox of the email provided</li></ul>                                                                                                                                                                                                                                                                                                                               |
| As a registered shopper I want to be able to have a personalised user profile so I can view my personal order history and order confirmations and save my payment information                | <ul><li>The profile can be accessed through My Account button in upper right corner of the page</li></ul>                                                                                                                                                                                                                                                                                                                                   |
| As a registered shopper I want to be able to request my own personalised design                                                                                                                  | <ul><li>Upload of the Design via Request Form accessible through My Account option</li></ul> |
| As a registered shopper I want to be able to place an order for my personalised creation so I can have my creation made available to me when it's ready                               | <ul><li>This feature is available from Request option on the navbar by clicking on Order Form</li></ul>                                                                                                                                                                                    |
| As a registered shopper I want to be able to easily contact the Creator with any queries I might have so I can ask any questions I may have                                              | <ul><li>The Contact link is available on the main nav bar and accessible from every part of the website.</li><li>The Contact form opens in a separate tab and once message is sent, a confirmation template renders to inform user that someone will be in touch</li></ul>                                                                                                                                                                  |
| As a shopper I want to be able to sort the list of available creations so I can easily identify the best rated, best priced and categorically sorted products                                 | <ul><li>This option is available by accessing 'All' option within the navbar</li></ul>                                                                                                                                                                                                                                                                                                                                               |
| As a shopper I want to be able to sort a specific category of creations so I can find best priced or best rated Creation in a specific category or sort the creation in that category by name   | <ul><li>The sorting option is available on every page in a format of a dropdown.</li></ul>                                                                                                                                                                                                                                                                                                                                                  |
| As a shopper I want to be able to sort multiple categories of creations simultaneously so I can find the best priced or best rated Creations across board categories, such as Portraits or Photography | <ul><li>By clicking on All, user may choose from all available creations. </li><li>Additionally there are badges displayed on top of the All page, to inform what categories are being displayed</li></ul>                                                                                                                                                                                                  |
| As a shopper I want to be able to search for a creation by name or description so I can find a specific creation I'd like to purchase                                                          | <ul><li>The option of a Search bar is available at all times, it returns key words by the creation name or from within a creations description</li></ul>                                                                                                                                                                                                                                                                                      |
| As a registered shopper I want to be able to easily select quantity of a creation when purchasing it so I can ensure I am selecting the correct creation and a correct quantity                    | <ul><li>While adding a creation to the bag, user chooses the quantity of the creation chosen</li><li>While in the bag, and preparing for check out, user can edit the quantity or delete the creation entirely by clicking remove</li></ul>                                                                                                                                                                                                |
| As a registered shopper I want to be able to view items in my bag to be purchased so I can identify the total cost of my purchase and all items I will receive                               | <ul><li>The current total is constantly displayed in upper right corner, under bag.</li></ul>                                                                                                                                                                                                                                                                                                                                            |
| As a registered shopper I want to be able to adjust the quantity of individual items in my bag so I can easily make changes to my purchase before checkout                                   | <ul><li>The quantity can be amended when user is in the bag, preparing for check out</li></ul>                                                                                                                                                                                                                                                                                                                                           |
| As a registered shopper I want to be able to easily enter my payment information so I can check out quickly and with no hassle                                                               | <ul><li>The payment details are entered after clicking Check out</li></ul>                                                                                                                                                                                                                                                                                                                                                                  |
| As a registered shopper I want to be able to feel that my personal and payment information is safe and secure so I can confidently provide the needed informatoin to make a purchase         | <ul><li>The Check out is only possible if the user is logged in. This way user's details, if they choose to save them, are securely stored</li></ul>                                                                                                                                                                                                                                                                                        |
| As a registered shopper I want to be able to view an order confirmation after checkout so I can verify that I have not made any mistakes                                                     | <ul><li>The order confirmation is displayed as well as emailed to the email address provided</li></ul>                                                                                                                                                                                                                                                                                                                                      |
| As a registered shopper I want to be able to receive an email confirmation after checking out so I can keep the records of my purchases                                                      | <ul><li>Email confirmation is sent instantanously after the creation(s) is/are purchased</li></ul>                                                                                                                                                                                                                                                                                                                                           |
| As a store owner I want to be able to add a creation as this would enable me to add new items to my store                                                                                     | <ul><li>This option is available to the superuser and while logged in</li><li>Choose My Account and Manage Creations</li><li>This will render a Creation upload form</li></ul>                                                                                                                                                                                                                                                             |
| As a store owner I want to be able to Edit/Update my creation to apply any changes, be it in price, description, image or other creation criteria                                                 | <ul><li>While logged in as a superuser, go to the creation in question and click edit button on all cretions view or on a creation detail page</li><li>From then on enter any details you want to change, including images</li><li>Upon submitting, a success toast appears</li></ul>                                                                                                                                                         |
| As a store owner I want to be able to delete a creation, remove a creation if they are no longer for sale                                                                                         | <ul><li>Whle logged in as a superuser, click on Delete option by creation that needs to be deleted</li><li>A success toast appears and the creation is gone from the system</li></ul>                                                                                                                                                                                                                                                         |
