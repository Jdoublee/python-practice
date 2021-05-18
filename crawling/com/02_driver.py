from selenium import webdriver

driver = webdriver.Chrome(executable_path="../webdriver/chromedriver")
    #executable_path="{}/chrome/chromedriver".format(rootPath),options = chrome_options

url = "https://www.instagram.com/explore/tags/달고나커피/"
driver.get(url)

#driver.close()