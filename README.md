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
* I want to be able to choose a specific treatment category.
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

13. 404.html
    * Redirects the user back to the home page to prevent them having to press the browser back button for better experience.

    ![404 error page](docs/404.png)

### General features on each page

All pages on the website are responsive and have:

* A favicon in the browser tab.

![Favicon](docs/favicon.png)

* All pages on the website have:
  * Logo

    ![logo](docs/logo.png)

  * To the right of the navigation bar are the links to the websites login pages and the basket. 

    ![Nav](docs/nav.png)

  * In the center navigation bar sits links to the rest of the website.

    ![Nav Spa Treatments](docs/nav_spa.png)

    or collapsed for tablets and mobiles.

    ![Mobile Nav](docs/mobilenav.png)

    ![Mobile Nav](docs/mobilenav2.png)

  * Toasts messages on all pages for different messages. An example below:

    ![Toasts](docs/toasts.png)

  * A footer which contains social media icon links to Facebook, Instagram and Twitter. 

    ![Footer](docs/footer.png)

### Future Implementations

* Add calendar and staff members to make the purchase a complete booking.

* Give the user an opportunity to by the membership throught the shop.

* Add an online community for the members o view in their profile.

### Accessibility

 * I have made sure there is colour contrast on the site. 
 
 * I have used a hover state on all buttons on the site to make it clear to the user if they are hovering over a button.

## Technologies Used

### Languages Used

* HTML, CSS, JavaScript and Python were used to create this website.

### Frameworks, Libraries & Programs Used

* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.

* [Git](https://git-scm.com/) - For version control.

* [Github](https://github.com/) - To save and store the files for the website.

* [GitPod](https://gitpod.io/) - IDE used to create the site.

* [Google Fonts](https://fonts.google.com/) - To import the fonts used on the website.

* [Heroku](https://id.heroku.com/login) - Hosting Website

* [jQuery](https://jquery.com/) - A JavaScript library.

* [Django](https://www.djangoproject.com/) - Used as the Python framework for the site together with the Jinja template.

* [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) - Used as the non-relational database management with Django.

* [Amazon AWS](https://aws.amazon.com/) - Used for storing static and media files.

* [Stripe](https://stripe.com/gb) - Used for secure checkout.

* [Google Developer Tools](https://developers.google.com/web/tools) - To troubleshoot and test features, solve issues with responsiveness and styling.

* [Bootstrap 4](https://getbootstrap.com/docs/4.1/getting-started/introduction/) - Used for the layout of the site.

* [FontAwesome](https://fontawesome.com/) - Used to create some of the icons on the site.

* [TinyPNG](https://tinypng.com/) - To compress image.

* [Image Resizer](https://imageresizer.com/) - To resize image.

* [Favicon.io](https://favicon.io/) - To create favicon.

* [Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.

* [Webpage Spell-Check](https://chrome.google.com/webstore/detail/webpage-spell-check/mgdhaoimpabdhmacaclbbjddhngchjik/related) - A google chrome extension that allows you to spell check your webpage. Used to check the site and the readme for spelling errors.

## Deployment & Local Development

The site was deployed using GitHub and is hosted on Heroku and was deployed as follows:

### Deployment 

Github Pages was used to deploy the live website. The instructions to achieve this are below:

1. Log in to Github.
2. Find the repository for this project, luxe_retreat.
3. Click on the Settings button.
4. Click on the Pages button in the left hand side bar.
5. In the Source section, choose main from the drop down select branch menu. Select Root from the drop down select folder menu.
6. Click Save. Your live Github Pages site is now deployed at the URL shown.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

To fork luxe_retreat repository:

1. Log in to Github.
2. Go to the repository for this project, CharlieBurton10/luxe_retreat
3. Click the Fork button at the top of the page between Watch and Starred.

#### How to Clone

To clone luxe_retreat repository:

1. Log in to Github.
2. Go to the repository for this project, CharlieBurton10/luxe_retreat
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then enter.
6. Then paste link from step 3 ($ git clone https://github.com/CharlieBurton10/luxe_retreat) and then press enter.

### Creating an App with the Heroku :

1. Navigate to [Heroku.com](https://www.heroku.com/).
2. Create a new account or login.
3. Click the **New** button, then **Create New App** button.
4. Choose your app name and the region and click **Create App**.

#### Connecting your Heroku account to your Github repository :

1. In your app choose **Deploy** tab and choose *Github* as your deployment method. 
2. Enter the GitHub repository name and click on *Search*.
3. Once the correct repository is found, click on *Connect*.

#### Setting you enviroment variables :

![Heroku Config Vars](/docs/heroku.png)

Navigate to **Settings** tab and click on *Reveal Config Vars* and set following variables :

- DATABASE_URL : URL to your databse
- DEBUG : Can be set to true but **ONLY** during development. It's extremely important to change it to false once development process is over.
- IP : 0.0.0.0
- PORT : 5000
- SECRET_KEY : Your custom secret key.

**PLEASE NOTE THAT YOU SHOULD NEVER SHARE ABOVE DETAILS WITH ANYONE DUE TO THE SECURITY REASONS!**

**IMPORTANT** *In order to successfully deploy your project to Heroku, you must include requirements.txt and Procfile files.* 

The following commands in the Gitpod CLI will create the relevant files :

`pip3 freeze --local > requirements.txt`

`echo web: python app.py > Procfile`

## Testing

Testing has been on going throughout the build with Chrome developer tools.

### W3C Validator

The W3C validator was used to validate the HTML on all pages of the website. It was also used to validate CSS in the style.css file.

[Home Page HTML](docs/testing/w3chome.png) - Passed

[Facilities Page HTML](docs/testing/w3cfacilities.png) - Passed

[Membership Page HTML](docs/testing/w3cmembership.png) - Passed

[Treatments Page HTML](docs/testing/w3ctreatments.png) - Passed

[Treatments-Add Page HTML](docs/testing/w3ctreatments-add.png) - Passed

[Treatments-Edit Page HTML](docs/testing/w3ctreatments-edit.png) - Passed

[Profile Page HTML](docs/testing/w3cprofile.png) - Passed

[Bag Page HTML](docs/testing/w3cbag.png) - Passed

[Checkout Page HTML](docs/testing/w3ccheckout.png) - Passed

[Checkout Success Page HTML](docs/testing/w3ccheckout_success.png) - Passed

[SignUp Page HTML](docs/testing/w3csignup.png) - Passed

[Login Page HTML](docs/testing/w3clogin.png) - Passed

[Logout Page HTML](docs/testing/w3clogout.png) - Passed

[CSS Page HTML](docs/testing/w3ccss.png) - Passed

JQuery Validator

[JQuery Stripe Elements Page HTML](docs/testing/jquerycountryfield.png) - Passed

[JQuery Country Field Page HTML](docs/testing/jquerycountryfield.png) - Passed

### Testing User Stories

#### First Time Visitor Goals

* I want to be able view a list of treatments.
  * The Spa Treatments page shows the treatments that have been added.

  ![Treatments](docs/treatments.png)

* I want to be able to navigate the site easily to find information about Luxe Retreat.
  * Site navigation is in the top right corner and in the center on every page of the website.

  ![Nav](docs/nav.png)

  ![Center Nav](docs/nav_spa.png)

* I want to be able to view the total of my purchases at any time.
  * As items are add to the basket, the total updates in the basket nav.

  ![Updated Basket](docs/basket_success.png)

* I want to be able to find their social media pages.
  * In the footer on every page sits links to the social media pages.

  ![Social Media links](docs/footer.png)

* I want the website to be responsive to whichever device I am using.
  * I have checked that the website is responsive on multiple devices.

* I want to be able to register for an account.
  * The user can register and then add their own event.

  ![Register](docs/register.png)

#### Returning/Frequent Visitor Goals

* I want to be able to log in and log out of my account.
  * I have added a log in page so returning visitors can log back in.

  ![Log In](docs/login.png)

  ![Logout](docs/logout.png)

* I want to be able to recover my password.
  * They can reset their password by using their email address.

  ![Password Reset](docs/password.png)

* I want to be able to receive an email confirmation after registering.
  * When a user resgisters it will send an email to verify the users email address.

  ![Verify](docs/verify.png)

  ![Email](docs/email.png)

  ![Confirm](docs/confirm.png)

* I want to be able to have a user profile.
  * Once login users can view their personal profile and past purchases.

  ![Profile](docs/profile.png)


####  Shopper
* I want to be able to choose a specific treatment category.
  * They can choose whether they want a facial or back massage.

  ![Spa](docs/nav_spa.png)

* I want to be able to search by treatment name or description and see the search results.
  * Users can use the search bar to find specific treatments.

  ![Back Search](docs/back-search.png)

* I want to be able to select the treatment quantity and then be able to adjust the quantity in the basket.
  * Users can edil quantity of treatment before adding to the basket and after in the basket.

  ![Treatment Quantity](docs/quantity.png)

* I want to be able to view the items in my basket.
  * By clicking the basket icon in the nav, users can view their basket of treatments.

  ![Basket](docs/basket.png)

* I want to be able to enter my payment information  and feel that it is safe and secure.
  * I have used Stripe to give users a secure checkout with their payment information.

  ![Checkout](docs/checkout.png)

* I want to be able to view a confirmation order and be able to view it in my profile.
  * Once checkout is completed they get a confirmation it has been successful and then sits in their profile.

  ![Checkout Confirmation](docs/thankyou.png)

  ![Profile](docs/profile.png)

#### Admin
* I want to be able to add the treatments.
  * Admin can add treatments in Treatment Management. 

  ![Admin](docs/admin.png)

  ![Add Treatment](docs/add.png)

* I want to be able to edit/update the treatments.
  * Admin can edit treatments in All Spa Treatments. 

  ![Edit](docs/editdelete.png)

  ![Edit Treatment](docs/edit.png)

* I want to be able to delete the treatments.
  * Admin can delete treatments in All Spa Treatments. 

  ![Delete](docs/editdelete.png)

### Performance Testing

[PageSpeed Insights](https://pagespeed.web.dev/) was used to measure the performance and speed of the main website pages. There were also a few performance suggestions which could be implemented in future iterations.



|     Page      |     Mobile    |    Desktop    |
| ------------  | ------------- | ------------- |
|  index.html  |    [Result](docs/testing/pagespeed-insights/indexmobile.png)   |    [Result](docs/testing/pagespeed-insights/indexdesktop.png)  | 
|  facilities.html  |    [Result](docs/testing/pagespeed-insights/facilitiesmobile.png)   |    [Result](docs/testing/pagespeed-insights/facilitiesdesktop.png)  | 
|  membership.html  |    [Result](docs/testing/pagespeed-insights/membershipmobile.png)   |    [Result](docs/testing/pagespeed-insights/membershipdesktop.png)  | 
|  treatments.html  |    [Result](docs/testing/pagespeed-insights/facilitiesmobile.png)   |    [Result](docs/testing/pagespeed-insights/facilitiesdesktop.png)  | 
|  signin.html  |    [Result](docs/testing/pagespeed-insights/signinmobile.png)   |    [Result](docs/testing/pagespeed-insights/signindesktop.png)  | 
|  bag.html  |    [Result](docs/testing/pagespeed-insights/basketmobile.png)   |    [Result](docs/testing/pagespeed-insights/basketdesktop.png)  | 
|  404.html  |    [Result](docs/testing/pagespeed-insights/404mobile.png)   |    [Result](docs/testing/pagespeed-insights/404desktop.png)  | 

### Further Testing

 * The website was tested on Google Chrome, Safari and Microsoft Edge browsers.
 * The website was tested on multiple devices: Desktop, Mackbook 14inch, iPad Pro and iPhone 14.
 * All browsers and devices were tested on all pages to make sure all the pages and links are working properly.

 ### Manual Testing

#### All pages
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Nav links:hover | Background colour when links are hovered | Hovered over each header link | Colour changed | Pass |
| Nav links| Launches / resets nav links | Clicked the nav links| Links clicked and correct pages launched | Pass |
| "Login / Register" Buttons | Log thems in and allows them to access there profile| Clicked button | Log thems in and shows their profile in the nav links | Pass |
| Social Media links | Text change colour when links are hovered | Hovered over each header link | Colour changed | Pass |

#### index.html
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Button links:hover | Background colour when links are hovered | Hovered over each header link | Colour changed | Pass |
| Button links| Launches correct pages | Clicked the button links | Links clicked and correct pages launched | Pass |

#### facilities.html
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| Photo:hover | Photo description appears | Hovered over each Photo | Text appeared | Pass |

#### treatments.html
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| "Search" Button | Launches the search | Entered text to the search bar and clicked "Search" button | Search results appear on the page | Pass |
| Adjust Quantity | Quantity number to plus and minus when +/- are pressed | Increased and descreased the number | Could adjust the quantity | Pass |
| "Add to Basket" Button | Treatment to be added to Basket | Added a treatment to the Basket | Treatment appeared in the Basket with a toast confirmation | Pass |

#### bag.html
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| "Update/Delete" Buttons | To Update or Delete treatment from the basket | Updated and Deleted Treatments | Basket adjusted after an Update or Delete was clicked| Pass |
| Button link | Launches correct page | Clicked the button links | Link clicked and correct page launched | Pass |
| "Secure Checkout" Button | Leads to checkout.html to start checkout | Checkout to commence | checkout.html launched for users details to be added | Pass |

#### checkout.html
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| User Checks out their Basket | Checkout to be successfull | Completed checkout form and clicked "Complete Order" button | Confirmation of sucessfull order | Pass |

#### profile.html
Feature | Expected Outcome	| Testing Performed |	Result	| Pass/Fail |
| --- | --- | --- | --- | --- |
| "Update Information" Button | Contact detail information is updated | Changed some contact detail information and then submitted it | Contatc information was updated| Pass |


## Credits

### Code Snippets

* [Facilities Gallery](https://tutorialzine.com/2018/03/3-amazing-bootstrap-4-gallery-templates) on Tutorialzine.

### Tutorials

*  Processes from the CI Project - Boutique Ado was used to help create this website - [Project - Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSF_102+4/courseware/4201818c00aa4ba3a0dae243725f6e32/d3188bf68530497aa5fba55d07a9d7d7/).


### Images

- [Holker Hall & Gardens Photo](https://unsplash.com/photos/brown-concrete-building-near-green-trees-under-blue-sky-during-daytime-9UE0xs9FvYg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Jonny Gios on Unsplash
- [Big swimming Photo](https://unsplash.com/photos/a-large-indoor-swimming-pool-with-a-view-of-the-trees-ls2i2Mh0M4Q?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Patrick Robert Doyle on Unsplash
- [Spa pool Photo](https://unsplash.com/photos/a-large-indoor-swimming-pool-in-a-house-xX0MKVVhHR4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Antonio Araujo on Unsplash
- [Lounge area Photo](https://unsplash.com/photos/brown-leather-couch-beside-brown-wooden-table-GM7cm1IC6Ss?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Jennifer Latuperisa-Andresen on Unsplash
- [Jacuzzi Photo](https://unsplash.com/photos/brown-leather-couch-beside-brown-wooden-table-GM7cm1IC6Ss?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Jennifer Latuperisa-Andresen on Unsplash
- [Sauna Photo](https://unsplash.com/photos/brown-and-white-floral-round-table-K65M3GbRYq8?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by HUUM on Unsplash
- [Lounge2 Photo](https://unsplash.com/photos/black-metal-framed-beige-padded-sofa-set-inside-room-XTC538P_eWk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Mateo Fernández on Unsplash
- [Food Photo](https://unsplash.com/photos/sliced-bread-on-black-ceramic-plate-beside-clear-drinking-glass-uyRK0Bt7mQo?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Matheus Frade on Unsplash
- [Studio Photo](https://unsplash.com/photos/group-of-women-doing-yoga-gJtDg6WfMlQ?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by bruce mars on Unsplash
- [Spa Photo](https://unsplash.com/photos/a-couple-of-chairs-sitting-next-to-each-other-in-a-room-npE_I2GzpHY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Sherzod Gulomov on Unsplash
- [Cafe Photo](https://unsplash.com/photos/brown-and-gray-concrete-store-nmpW_WwwVSc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Shawn on Unsplash
- [Gym Photo](https://unsplash.com/photos/black-and-gray-treadmill-m27OTMegUyA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by gina lin on Unsplash
- [Breathe Photo](https://unsplash.com/photos/and-breathe-neon-sign-on-tre-buymYm3RQ3U?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by Max van den Oetelaar on Unsplash
- [Cloakroom Photo](https://unsplash.com/photos/a-room-with-a-row-of-clothes-on-the-wall-0Ik0xzhUTZw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by K F on Unsplash

- [Favicon](https://www.vecteezy.com/free-vector/lr-logo") by Lr Logo Vectors by Vecteezy
  
###  Acknowledgments

 * Tutor Support at Code Institute.