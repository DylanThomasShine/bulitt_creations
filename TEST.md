<p><h1 align="center"><strong>BULITT</strong> CREATIONS</h1></p>

<br>

 <p><h1 align="center"><strong>TEST</strong> FILES</h1></p>                                                                                                                                                                                

![User Story image](/media/testimages2.jpg)

<br>

<p><h1 align="center"><strong>ERR</strong>ORS</h1></p>

| <h2>Error</h2> | <h2>Resolve</h2>                                                                                                                |
|-------|--------------------------------------------------------------------------------------------------------------------------|
| Navbar not responding properly on mobile view  | Changed padding and visibilty and sizes in CSS               |
|![Navbar Error](/media/navbar_error.png) |![Navbar Resolve](/media/navbar_resolve.png)
| Region error when deploying to heroku  | Region was inputted incorrectly in settings.py |
|![Region Error](/media/region_error.png)|![Region Resolve](/media/region_resolve.png) |
| Not deploying to local server | Added in the Coma that was missing from settings.py for SECRET_KEY |
|![Secret Key Error](/media/secret_key_error.png) | ![Secret Key Resolve](/media/secret_key_resolve.png)
| Webhook not receiving for local server | Created a new endpoint and deleted older one
|![Local webhook Fail](/media/local_fail.png) | ![Local Webhook Resolve](/media/local_success.png)
| Webhook not receiving for heroku server | Created a new endpoint and deleted older one and re-configured the Config Vars
|![Heroku webhook Fail](/media/heroku_fail.png) | ![Heroku Webhook Resolve](/media/heroku_success.png)
<br>

<p><h1 align="center"><strong>PERFORMANCE</strong> TESTING</h1></p>

I used two different testers here to check for performance of the site and although it is not perfect it is my intend to make it so and I did not have the time as I found out too late about these programs that were available.<br> [![SureOak](https://img.shields.io/badge/SureOak-Automated%20Testing-green)](https://www.sureoak.com/)<br>&<br>[![SureOak](https://img.shields.io/badge/Light%20House-Performance%20Tool-blue)](https://developers.google.com/web/tools/lighthouse)

<br>

![Validation Results](/media/performance_results.jpg)


# <strong>Validation</strong> Testing

When testing for html it contained a lot of python code in it and as these results show I filtered the python code that showed as errors in the validator and I was left without any errors in the html code. I did this across the board while testing and when I had errors for the code I was testing I resolved them and the results are as follows. 

<br>

## <strong>Line</strong> too long

<br>

 In order to resolve these errors and in my research to find out how, I found they are classed as a style error and does not affect the code performance. I chose to use the comment <strong>#noqa</strong> only in places where a line break \ didn't work and began to mess up the code  and I dealt with any other errors that arose, from trailing white lines to indents and so on.
<br><br>

## <strong>E6</strong> Syntax

<br>

<strong>Template literal syntax’ is only available in ES6 (use ‘esversion: 6’). (W119)jshint(W119).</strong>
This is a fix I could have applied but to be honest I was nervous to try it and the code didn't have any errors other than this and even though it is an error it DID NOT affect the code or the performance of the site in any way. A way to fix this was to:-<br> Add a file named <strong>.jshintrc</strong> to the project and inside this file type:- <strong>{"esversion": 6}</strong>

<p id="userex"><h1 align="center"><strong>VALIDATION</strong> RESULTS</h1></p>

<br>
<details><summary><strong>BAG</strong> APP</summary>
<br>

![Validation Results](/media/bag_results.jpg)</details>

<br>
<details><summary><strong>BULITT_CREATIONS</strong> APP</summary>
<br>

![Validation Results](/media/bulitt_results.jpg)</details> 

<br>
<details><summary><strong>CHECKOUT</strong> APP</summary>
<br>

![Validation Results](/media/checkout_results.jpg)</details>

<br>
<details><summary><strong>COMMISSION</strong> APP</summary>
<br>

![Validation Results](/media/commission_results.jpg)</details> 

<br>
<details><summary><strong>CONTACT</strong> APP</summary>
<br>

![Validation Results](/media/contact_results.jpg)</details> 

<br>
<details><summary><strong>HOME</strong> APP</summary>
<br>

![Validation Results](/media/home_results.jpg)</details> 

<br>
<details><summary><strong>PRODUCTS</strong> APP</summary>
<br>

![Validation Results](/media/products_results.jpg)</details> 

<br>
<details><summary><strong>PROFILES</strong> APP</summary>
<br>

![Validation Results](/media/profiles_results.jpg)</details> 

<br>
<details><summary><strong>STATIC</strong> CSS</summary>
<br>

![Validation Results](/media/static_css_results.jpg)</details> 

<br>
<details><summary><strong>TEMPLATES/ALLAUTH/INCLUDES</strong> HTML</summary>
<br>

![Validation Results](/media/templates_results.jpg)</details> 

<br>
<details><summary><strong>MANAGE</strong> .PY</summary>
<br>

![Validation Results](/media/manage_results.jpg)</details> 
<br>

<br>
<details><summary><strong>SCREEN SIZE</strong> RESPONSIVNESS</summary>
<br>

![Validation Results](/media/screen_results.jpg)</details> 
<br><br>

<p id="thanks"><h1 align="center"><strong>THANK</strong> YOU</h1></p>
<p><h1 align="center">for<strong> browsing</strong> my <strong>TEST</strong> file.....</h1></p>

## Please click  [HERE](https://github.com/DylanThomasShine/bulitt_creations/blob/main/README.md) to bring you back to the README file.