#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager






# In[2]:


executable_path = {"executable_path":r"C:\Users\Anthony\.wdm\chromedriver\2.46\win32\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless = False)
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')


# In[3]:


news_title = soup.find('div', class_='content_title').get_text()
print(news_title)
news_p = soup.find('div', class_='article_teaser_body').get_text()
print(news_p)


# In[4]:


# Image 
url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=featured#submit"
browser.visit(url_image)


# In[5]:


#Getting the base url
from urllib.parse import urlsplit
base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url_image))
print(base_url)


# In[6]:


executable_path = {"executable_path":r"C:\Users\Anthony\.wdm\chromedriver\2.46\win32\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless = False)
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)
import time 
browser.click_link_by_partial_text('FULL IMAGE')
time.sleep(3)
browser.click_link_by_partial_text('more info')
time.sleep(3)
browser.click_link_by_partial_text('.jpg')


# In[7]:


html = browser.html
soup = bs(html, 'html.parser')

featured_img_url = soup.find('img').get('src')
print(featured_img_url)


# In[22]:


mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_weather_url)
time.sleep(1)
mars_weather_html = browser.html
mars_weather_soup = bs(mars_weather_html, 'html.parser')

tweets = mars_weather_soup.find('ol', class_='stream-items')
mars_weather = tweets.find('p', class_="tweet-text").text
print(mars_weather)


# In[18]:


url_facts = 'https://space-facts.com/mars/'


# In[23]:


df_mars_facts = table[0]
df_mars_facts.columns = ["Parameter", "Values"]
df_mars_facts.set_index(["Parameter"])


# In[79]:


table = table_df.to_html(classes = 'table table-striped')
print(table)


# In[27]:


# hemispheres
executable_path = {"executable_path":r"C:\Users\Anthony\.wdm\chromedriver\2.46\win32\chromedriver.exe"}
browser = Browser("chrome", **executable_path, headless = False)
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

html = browser.html
soup = bs(html, 'html.parser')



# In[35]:


import time 
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = bs(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=bs(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})


# In[36]:


mars_hemisphere

