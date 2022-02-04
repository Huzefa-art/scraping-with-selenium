#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from selenium.webdriver.common.by import By


# In[3]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans")


# In[4]:


userid_element = driver.find_elements_by_xpath('//*[@id="Comment_1726631"]/div/div[2]/div[1]/span[1]/a[2]')[0]
userid = userid_element.text


# In[5]:


userid


# In[6]:


user_date = driver.find_elements_by_xpath('//*[@id="Comment_1726631"]/div/div[2]/div[2]/span[1]/a/time')[0]
date = user_date.get_attribute('title')


# In[7]:


date


# In[8]:


user_message = driver.find_elements_by_xpath('//*[@id="Comment_1726631"]/div/div[3]/div/div[1]')[0]
comment = user_message.text


# In[9]:


comment


# In[10]:


elements = driver.find_elements(By.XPATH, '//*[@id="Comment_1726631"]/div/div[2]/div[1]/span[1]/a[2]')[0]


# In[11]:


userid = elements.text
userid


# In[12]:


ids = driver.find_elements(By.XPATH, "//*[contains(@id,'Comment_')]")
comment_ids = []
for i in ids:
    comment_ids.append(i.get_attribute('id'))
    
comment_ids
int(driver.find_elements(By.XPATH, "//*[contains(@title,'Next Page')] /preceding-sibling::a[1]")[0].text)


# In[51]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans"
driver.get(url)
all_data = []

comments = pd.DataFrame(columns = ['Date','user_id','comments']) 
ids = driver.find_elements(By.XPATH, "//*[contains(@id,'Comment_')]")
comment_ids = []
for i in ids:
    comment_ids.append(i.get_attribute('id'))

for x in comment_ids:
    def getData():
        user_date = driver.find_elements(By.XPATH,'//*[@id="' + x +'"]/div/div[2]/div[2]/span[1]/a/time')[1].get_attribute('title')
        userid_element = driver.find_elements(By.XPATH,'//*[@id="' + x +'"]/div/div[2]/div[1]/span[1]/a[2]')[2].text
        user_message = driver.find_elements(By.XPATH,'//*[@id="' + x +'"]/div/div[3]/div/div[1]')[3].text
        comments.loc[len(comments)] = [date,userid,comment]
        return comments
    
    number_of_pages = 10
    for j in range(number_of_pages - 1):
        all_data.extend(getData())
        next_page = driver.find_elements(By.XPATH, "//*[contains(@title,'Next Page')]")[0].click()
        time.sleep(1)
    driver.get(url)
driver.quit()


# In[ ]:


comments.head()


# In[ ]:


next_page =driver.find_elements(By.XPATH, "//*[contains(@title,'Next Page')]")
next_page


# In[ ]:


number_of_pages = int(driver.find_elements(By.XPATH, "//*[contains(@title,'Next Page')] /preceding-sibling::a[1]")[0].text)


# In[14]:


number_of_pages


# In[16]:


def main():
 all_data = []
 select = Select(driver.find_element_by_xpath("//select[@class='formitem' and @id='selWeek']"))
 list_options = select.options

 for item in range(len(list_options)):
    select = Select(driver.find_element_by_xpath("//select[@class='formitem' and @id='selWeek']"))
    select.select_by_index(str(item))
    driver.find_element_by_css_selector("input.formbutton#csbtnSearch").click()
    number_of_pages = int(driver.find_element_by_xpath("//a[contains(text(),'Next')]/preceding-sibling::a[1]").text)
    for j in range(number_of_pages - 1):
      all_data.extend(getData())
      driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
      time.sleep(1)
    driver.get(url)

 with open( 'wiltshire.json', 'w+' ) as f:
    json.dump( all_data, f )
 driver.quit()


# In[ ]:


def getData():
  data = []
  rows = driver.find_element_by_xpath id="form1"]/table/tbody').find_elements_by_tag_name('tr')
 for row in rows:
    app_number = row.find_elements_by_tag_name('td')[1].text
    address =  row.find_elements_by_tag_name('td')[2].text
    proposals =  row.find_elements_by_tag_name('td')[3].text
    status =  row.find_elements_by_tag_name('td')[4].text
    data.append({"CaseRef": app_number, "address": address, "proposals": proposals, "status": status})
print(data)
return data


# In[4]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://forums.edmunds.com/discussion/2864/general/x/entry-level-luxury-performance-sedans"
driver.get(url)

comments = []
def getData():
    
    
    ids = driver.find_elements(By.XPATH, "//*[contains(@id,'Comment_')]")
    comment_ids = []
    for i in ids:
        comment_ids.append(i.get_attribute('id'))
        
    for x in comment_ids:
        user_date = driver.find_elements(By.XPATH,'//*[@id="' + x +'"]/div/div[2]/div[2]/span[1]/a/time')[0]
        date = user_date.get_attribute('title')
        userid_element = driver.find_elements(By.XPATH,'//*[@id="' + x +'"]/div/div[2]/div[1]/span[1]/a[2]')[0]
        userid = userid_element.text
        user_message = driver.find_elements(By.XPATH,'//*[@id="' + x +'"]/div/div[3]/div/div[1]')[0]
        comment = user_message.text
        comments.append({"Date":date, "user_id":userid, "comments":comment})
        return comments

all_data = []    
def main():
  
    number_of_pages =  int(driver.find_elements(By.XPATH, "//*[contains(@title,'Next Page')] /preceding-sibling::a[1]")[0].text)
    for j in range(number_of_pages - 1):
        
        all_data.extend(getData()) 
        driver.find_elements(By.XPATH, "//*[contains(@title,'Next Page')]")[1].click()
        time.sleep(1)
    driver.get(url)
    
    driver.quit() 
    
if __name__ == "__main__":
    main()


# In[32]:


df = pd.DataFrame(comments)


# In[33]:


df


# In[6]:


df = pd.DataFrame(all_data)
df


# In[9]:


df.to_csv("selenium_pagination_scraping")


# In[ ]:





# In[ ]:




