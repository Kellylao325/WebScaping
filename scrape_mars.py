#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# In[5]:


executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


#NASA Mars News

# visiting webpage
news_url = 'https://mars.nasa.gov/news/'
browser.visit(news_url)


# In[7]:


# Create soup object; parse with 'html.parser'
news_soup = bs( browser.html,"html.parser")


# In[8]:


#title and headline
news_title = news_soup.find('div', class_='content_title').text
news_p = news_soup.find('div', class_='article_teaser_body').text
print(news_title)
print(news_p)


# In[9]:


#JPL Mars Space Images


# In[14]:


# visiting webpage
jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(jpl_url)


# In[17]:


#scrape JPL with html.parser
jpl_soup = bs(browser.html, 'html.parser')


# In[28]:


main_jpl_url = 'https://www.jpl.nasa.gov'
image_url = jpl_soup.find('img', class_= 'fancybox-image')['src']
featured_image_url = main_jpl_url + image_url
print(f'featured_image_url: {featured_image_url}')


# In[29]:


#Mars Weather


# In[38]:


# visiting webpage
mars_url = 'https://twitter.com/marswxreport?lang=en'
browser.visit(mars_url)

# scrape; parse with 'html.parser'
mars_soup = bs( browser.html,"html.parser")


# In[45]:


tweets = mars_soup.find_all('div', class_='js-tweet-text-container')
for tweet in tweets:
    mars_weather = tweet.find('p').text
    if 'InSight sol' in mars_weather:
        print(mars_weather)
        break
    else:
        pass


# In[ ]:


# MARS Facts


# In[60]:


# visiting webpage
facts_url = 'https://space-facts.com/mars/'

table = pd.read_html(facts_url)
facts_table = table[1]
facts_table


# In[62]:


#facts table to html
facts_table.to_html('Mars_facts_table.html', index = False)


# In[63]:


# Mars Hemispheres


# In[66]:


# visiting webpage
hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(hemisphere_url)

# scrape; parse with 'html.parser'
hemi_soup = bs( browser.html,"html.parser")


# In[69]:


main_hemi_url = 'https://pds-imaging.jpl.nasa.gov/'
all_img = hemi_soup.find_all('div', class_='item') 
images_url = []


# In[68]:




# In[ ]:




