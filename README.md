# Mission To Mars - Berkeley DA
Yae Jin Park\
Module 10

## Overview
With Python and its modules, Splinter and Beautiful Soup, I was able to web scrape for latest news of Mars and four images of its hemispheres. These results are stored in a MongoDB database and then rendered on the index.html page.

### Running the Code
Please make sure to download MongoDB Community first (this project used Version 4.4.8: https://www.mongodb.com/try/download/community

Scraped data are NOT hosted as this project is mainly for educational purposes, and users will be required to create their own databases on their local machines. Create a database named 'mars_app' on local machines before running the app (please refer to this link for information on how to create a database with MongoDB: https://www.mongodb.com/basics/create-database).

After successfully downloading MongoDB and creating the 'mars_app' database, keep MongoDB running on one terminal window and run 'python app.py' on a new window.

Access the rendered page through http://127.0.0.1:5000/

## Bootstrap Customization
Two simple modifications have been made for Bootstrap elements: 

1. The 'Scrap New Data' button has been shrunk and color changed to light blue
2. Thumbnail images of the Mars hemisphere pictures have been changed from squares to circles, resulting in "cropping out" of the black background the planet had. Here are the before and after images for comparison.

![Before Change](https://github.com/yaejinpark/mission-to-mars/blob/main/resources/before_change.png)
![After Change](https://github.com/yaejinpark/mission-to-mars/blob/main/resources/after_change.png)
