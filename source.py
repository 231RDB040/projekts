import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.jauns.lv"
driver.get(url)
time.sleep(2)

find=driver.find_element(By.CLASS_NAME, "css-47sehv")
find.click()
print()
print("·····················································································································")
a = driver.find_elements(By.CLASS_NAME, "streamer")

for elements in a:
    nosaukums = elements.find_element(By.CLASS_NAME, "article-simple__title").text
    links = elements.find_element(By.CLASS_NAME, "article-simple__link").get_attribute("href")
    print(nosaukums)
    print()
    print(links)
    print("·····················································································································")
