from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

#open the website
website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
#path = 'C:/Users/asusa/Downloads/chromedriver-win64 (1)/chromedriver-win64'
driver = webdriver.Chrome() #don't use chromedriver path, because selenium can detect automatically
driver.get(website)

all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()

#extract table
driver.implicitly_wait(10)
matches = driver.find_elements(By.TAG_NAME,'tr')

date=[]
home_team=[]
score=[]
away_team=[]

for match in matches:
    date.append(match.find_element('xpath','./td[1]').text)
    home = match.find_element('xpath','./td[2]').text
    home_team.append(home)
    print(home)
    score.append(match.find_element('xpath','./td[3]').text)
    away_team.append(match.find_element('xpath','./td[4]').text)
driver.quit()

#save to dataframe
df=pd.DataFrame({'date':date,'home_team':home_team,'score':score,'away_team':away_team})
df.to_csv('football_data.csv',index=False)
print(df)