#!/usr/bin/env python
# coding: utf-8

# In[27]:


# Dependencies
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


# In[28]:


from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[29]:


mars_info = {}


# In[30]:

def Mars_News():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html=browser.html
    time.sleep(2)
    soup = bs(html, 'html.parser')
    titles = soup.find_all('div', class_="content_title")
    mars_info['title']  = titles[0]
    # for index in (range(len(titles))):
    #     print(titles[index].getText())
    time.sleep(2)
    paragraph = soup.find_all('div', class_="article_teaser_body")
    mars_info['news_paragraph'] = paragraph[0].text
    return mars_info
# In[31]:


#mars_info['news title'] =titles[0].text
#mars_info


# In[32]:


#paragraph = soup.find_all('div', class_="article_teaser_body")
#paragraph[0]
# for index in (range(len(paragraph))):
#     print(paragraph[index].getText())


# In[33]:


#mars_info['news_paragraph'] = paragraph[0].text
#mars_info


# In[34]:

def Mars_Images():
    url= "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser .visit(url)
    html=browser.html
    time.sleep(2)
    soup = bs(html,'html.parser')
    featured_image_url = soup.findAll('a',{'class':'fancybox'})[0]['data-fancybox-href']
    # find_all("img", class_="image_and_description_container")
    print("https://www.jpl.nasa.gov"+featured_image_url)
    mars_info['Images'] = "https://www.jpl.nasa.gov"+featured_image_url
    time.sleep(2)
    return mars_info

# In[36]:


# Twitter 
### Mars Weather
def Mars_Weather():
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    time.sleep(2)
    html=browser.html
    soup=bs(html, 'html.parser')
    data = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_info['weather_tweet'] = data[1].text
    return mars_info


# In[38]:


#Mars_Weather_Display = Mars_Weather()
#Mars_Weather_Display


# In[ ]:


# Mars facts
def Initialize(url):
    browser.visit(url)
    html=browser.html
    time.sleep(2)
    return html

def Mars_Facts():
    soup=bs(Initialize("http://space-facts.com/mars/"), 'html.parser')
    tabledata =soup.find('table', class_="tablepress tablepress-id-mars")
    keys=[]
    values=[]
    coloum1 =tabledata.findAll("td", class_="column-1")
    coloum2 =tabledata.findAll("td", class_="column-2")

    for key in coloum1:
        keys.append(key.text)    

    for value in coloum2:
        values.append(value.text)
    mars_facts = pd.DataFrame({
        "key":keys,
        "Value":values
        })
    mars_facts_html = mars_facts.to_html(header=False, index=False)
    mars_info['mars_facts'] = mars_facts_html
    return mars_info


# In[ ]:


#mars_facts_display = Mars_Facts()


# In[ ]:


#mars_facts_display


# In[ ]:


# Get hemisphere images




# In[ ]:


def mars_hemsiphere(): 
    soup=bs(Initialize("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"), 'html.parser')
    time.sleep(4)
    Image_Title = soup.findAll("h3")
    imgsrc = soup.find_all('img', class_="thumb")
    dict_MarsHemisphere = {}
    list_MarsHemisphere = []
    count=0
    for header in Image_Title:
        p = browser.find_by_text(header.text) 
        p.click()
        time.sleep(3)
        back = browser.find_link_by_partial_text("Back")
        back.click()
        time.sleep(3)
        print("title: "+header.text)
        url = "https://astrogeology.usgs.gov"+imgsrc[count]['src']
        list_MarsHemisphere.append({"title:" : header.text , "img_url" : url })
        #dict_MarsHemisphere[hearder.text]=url]
        print("img: "+url)
        count+=1
        mars_info['hiu'] = list_MarsHemisphere
    return mars_info   


# In[ ]:


#d = mars_hemsiphere()


# In[11]:





# In[ ]:




