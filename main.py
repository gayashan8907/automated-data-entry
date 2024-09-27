from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
rental = response.text
soup = BeautifulSoup(rental,"html.parser")
prices=soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
addresses = soup.find_all(name="address")
links = soup.find_all(name="a",class_="property-card-link")
price_list = []
address_list = []
links_list = []
for price in prices:
    price_list.append(price.string.strip("$ +/mo"))
print(price_list)
for add in addresses:
    address_list.append(add.string.strip( ))
print(address_list)
for link in links:
    links_list.append(link.get("href"))
print(links_list)

Chrome_options = webdriver.ChromeOptions()
Chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=Chrome_options)
for i in range(len(address_list)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeCl22w5IX7-LgjrzP8gxhpv5Z4tCYAoOuYfXtPv5kwziK9nQ/viewform?usp=sf_link")
    search_add = driver.find_element(By.CSS_SELECTOR,value='input[aria-labelledby="i1"]')
    search_add1 = driver.find_element(By.CSS_SELECTOR,value='input[aria-labelledby="i5"]')
    search_add2= driver.find_element(By.CSS_SELECTOR,value='input[aria-labelledby="i9"]')
    search_add3= driver.find_element(By.CSS_SELECTOR,value='.NPEfkd.RveJvd.snByac')


    search_add.send_keys(address_list[i])
    search_add1.send_keys(price_list[i])
    search_add2.send_keys(links_list[i])
    search_add3.click()
    submit = driver.find_element(By.LINK_TEXT,value="Submit another response")
    submit.click()