from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


def hemisphere_scrape():
    # 1. Use browser to visit the URL 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.accordian', wait_time=1)

    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # 3. Write code to retrieve the image urls and titles for each hemisphere.

    # There are four search results in this page. Set for loop to run for four iterations.
    for i in range(0,4):
        search_link = browser.find_by_css('a.itemLink h3')[i].click()

        open_full_image = browser.find_by_id('wide-image-toggle').click()

        # Set up html parser with BS4
        html = browser.html
        hem_soup = soup(html,'html.parser')

        full_img_src = hem_soup.find('a',text='Sample').get('href')
        img_title = hem_soup.find('h2',class_='title').get_text()

        # Append to urls dictionary with image title as key and link as value
        hemisphere_image_urls.append({'title':img_title, 'img_url': full_img_src})

        browser.back()


    # 4. Print the list that holds the dictionary of each image url and title.
    hemisphere_image_urls

    # 5. Quit the browser
    browser.quit()

    return hemisphere_image_urls
