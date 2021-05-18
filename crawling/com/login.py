from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../webdriver/chromedriver")

url = "https://www.instagram.com/accounts/login/"

driver.get(url)
time.sleep(0.5)

driver.find_element_by_name("username").send_keys("") # id
driver.find_element_by_name("password").send_keys("") # password
time.sleep(0.5)

driver.find_element_by_name("password").submit() # login button click
