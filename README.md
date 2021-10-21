<h1 text-align="center">Bulitt Creations</h1>

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

### Font

Throughout the project there is only one font used, which is Lato. The aim is to make this website as minimalist and clean as possible, I used shadows in CSS and HTML to make certain headings stand out more.

### Color Scheme

The main color used throughout the page is pale and light, almost white, as this ensures best effectivens of the design style. Black and gray is used to highlight Titles, headings and general top page information. Other grey and black colours used were to create the frame surrounding each picture. The remaining colours are used for hovers, warnings and small buttons such as edit or remove.

![Colur Chart](/media/colour_chart.jpg) 

### Wireframes

|[Bulitt Creations Wireframes](/media/wireframes.pdf)|  
<details><summary>All Products - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107297/eCommerce_Web_Design-12_lxaltd.jpg)
</details>

<details><summary>Product Detail - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107297/eCommerce_Web_Design-13_x9sx3z.jpg)
</details>

<details><summary>Register Account - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107296/eCommerce_Web_Design-15_vyz1iw.jpg)
</details>

<details><summary>Sign In - Mobile and PC</summary>
 
![](https://res.cloudinary.com/dugnokxox/image/upload/v1610107297/eCommerce_Web_Design-14_2_onyqe4.jpg)
</details>

<br><br>

