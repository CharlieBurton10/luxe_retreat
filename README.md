# Luxe Retreat


![Luxe Retreat Website shown on a range of devices](docs/responsivehome.png)

[View Luxe Retreat Website](https://luxe-retreat-cf96daa6ac2f.herokuapp.com/)


## CONTENTS
* [Rationale](#rationale)
  * [Project Introduction](#project-introduction)
  * [Motivation and Inspiration](#motivation-and-inspiration)
  * [Project Scope and Limitations](#project-scope-and-limitations)

* [User Experience](#user-experience-ux)
  * [Site Goals](#site-goals)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
  * [Database Structure](#database-structure)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)
  * [Creating an App with the Heroku](#creating-an-app-with-the-heroku)

* [Testing](#testing)
  * [W3C Validator](#w3c-validator)
  * [Solved Bugs](#solved-bugs)
  * [Testing User Stories](#testing-user-stories)
  * [Performance Testing](#performance-testing)
  * [Further Testing](#further-testing)
  * [Manual Testing](#manual-testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Tutorials](#tutorials)
  * [Images](#images)
  * [Acknowledgments](#acknowledgments)
  

## Rationale

### Project Introduction
This website is designed to produce a flawless and secure e-commerce shopping experience using Django, CSS, HTML and Javascript. You will also be able to register/login to your account, where you can check previous orders and amend your address.

### Motivation and Inspiration
People's wellbeing is now more important than ever to help improve healthy habits on a daily basis to attain better physical and mental health, and this includes time-out for oneself to relax and unwind. This website gives the opportunity to have a relaxed user friendly spa treatment booking experience.

The inspiration for creating this website is to bring a high-end and luxury look to a Spa shopping experience, which was offereing luxury treatments but was failing on a website to match this level of experience.

### Project Scope and Limitations
The scope of the project includes the creation of a spa treatment database with the features focusing on usability on mulitple devices and accessbility for anyone wanting to go to visit Luxe Retreat.

The known limitation is the Luxe Retreat website currently just allows you to book a treatment without a calendar booking facility. To solve this limitation I would expand to include a calendar booking system with live availbility and also an opportunity for the user to add a specific staff member to the Treatment basket before checking out. 

## User Experience (UX)

### Site Goals
* I want the user to be able to view the site on a range of device.
* I want the site to be attractive, responsive and easy to use for the user.
* I want the site to work as up-to-date on spa treatments at Luxe Retreat.
* I want the site to be user friendly and for all ages.

### User Stories

#### First Time Visitor Goals

* I want to be able view a list of treatments.
* I want to be able to navigate the site easily to find information about Luxe Retreat.
* I want to be able to view the total of my purchases at any time.
* I want to be able to find their social media pages.
* I want the website to be responsive to whichever device I am using.
* I want to be able to register for an account.

#### Returning/Frequent Visitor Goals

* I want to be able to log in and log out of my account.
* I want to be able to recover my password.
* I want to be able to receive an email confirmation after registering.
* I want to be able to have a user profile.

####  Shopper
* I want to be able to sort by a specific treatment category.
* I want to be able to search by treatment name or description and see the search results.
* I want to be able to select the treatment quantity and then be able to adjust the quantity in the basket.
* I want to be able to view the items in my basket.
* I want to be able to enter my payment information  and feel that it is safe and secure.
* I want to be able to view a confirmation order and be able to view it in my profile.

#### Admin
* I want to be able to add the treatments.
* I want to be able to edit/update the treatments.
* I want to be able to delete the treatments.

## Design

### Colour Scheme

![Luxe Retreat Colour Palette](docs/colourpalette.png)

The website uses a palette of white, grey and gold to give a luxury and steamline feel. The colour palette was created using the [Coolors](https://coolors.co/) website.

### Typography

I have used Cormorant Garamond from Google Fonts for this website. I like the smartness of this font to give the website the feel I wanted. It is a Serif font.

![Cormorant Garamond](docs/font.png)

### Imagery

All imagery used within the site has been chosen to showcase the Luxe Retreat. I have credited this at the end.

### Wireframes

Wireframes were created for mobile, tablet and desktop.

![Home Page Wireframe](docs/wireframes/home.png)
![Facilities Page Wireframe](docs/wireframes/facilities.png)
![Membership Page Wireframe](docs/wireframes/membership.png)
![Spa Treatments Page Wireframe](docs/wireframes/spa-treatments.png)
![Sign Up Page Wireframe](docs/wireframes/sign-up.png)
![Sign In Page Wireframe](docs/wireframes/sign-in.png)
![Basket Page Wireframe](docs/wireframes/basket.png)
![Checkout Page Wireframe](docs/wireframes/checkout.png)

### Database Structure

[DB Diagram](https://dbdiagram.io/d) was used to create my database structure.

![Database](docs/database.png)

#### Database Schema

I first created a database structure and from this I decide to use the django internal database and then used PostgreSQL from Code Institute when deployed to Heroku.

![Database Contents](docs/database_contents.png)

#### Database tables

I firstly added json files to gitpod and then pulled them through to django database.

![JSON](docs/json.png)

![Treatments Categories](docs/treatments_categories.png)

![Treatments](docs/treatments_treatments.png)

I then repeated this for memberships.

## Features

The website is comprised of:
1. Home page
    * Shows the Luxe Retreat with links to membership and treatments.

    ![Home](docs/home.png)

2. Register page
    * Allows the user to register.
    * If already registered it sends them to the login page.

    ![Register](docs/register.png)

3. Login page
    * Allows the user to login.
    * If not registered it sends them to the register page.

    ![Login](docs/login.png)

4. Facilities page
    * Shows the user the facilities on offer at Luxe Retreat and when the mouse is hovered over the photos a description appears.

    ![Facilities](docs/facilities.png)

5. Membership page
    * Allows user to view the different memberships on offer. This can be edit in the database.

    ![Membership](docs/membership.png)

6. Spa Treatments page
    * The navigation button for Spa Treatments gives the treatments by categories for the users ease.

    ![Nav Spa Treatments](docs/nav_spa.png)

    * Shows the user all treatments available.

    ![Spa Treatments](docs/treatments.png)

    * Has a search feature.

    ![Search](docs/search.png)

7. Basket page
    * Once the user has selected treatments it will go into their basket.

    ![Basket](docs/basket.png)

8. Checkout page
    * Once the user as clicked on Secure Checkout in the Basket page it will send them through to the Checkout Page.

    ![Checkout](docs/checkout.png)

9. Checkout confirmation page
    * Once the user has checkout, they get sent to this email confirmation page.

    ![Thank You](docs/thankyou.png)

10. My Profile & Treatments page
    * Once the user is login they can view their profile and previous purchases, where the can update their address.

    ![Profile](docs/profile.png)

11. Admin
    * On admin login you get a new button on My Account nav bar, called 'Treatment Management'. Treatment Management allows you to add new treatments.
    
    ![Admin](docs/admin.png)

    ![Add Treatment](docs/add.png)

    * Can only edit/delete as admin.

    ![Edit and Delete](docs/editdelete.png)

    ![Edit Treatment](docs/edit.png)

12. Logout
    * Allows the user to logout.
    
    ![Logout](docs/logout.png)