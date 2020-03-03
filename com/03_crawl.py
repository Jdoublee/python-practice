from selenium import webdriver
from time import sleep
driver = webdriver.Chrome(executable_path="../webdriver/chromedriver")

url = "https://www.instagram.com/explore/tags/달고나커피/"
driver.get(url) #url enter
sleep(5) # waiting for data 
pageString = driver.page_source #saving source of url page
print(pageString)

driver.close()