from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from random import randint, choice
from ElemFunctions import Email, Name, Username, Password 

# options = ChromeOptions()

# options.add_argument("--incognito")

# prox = Proxy()
# prox.proxy_type = ProxyType.MANUAL
# prox.ssl_proxy = '189.187.184.232:8080'

# capabilities = webdriver.DesiredCapabilities.CHROME

# prox.add_to_capabilities(capabilities)

driver = Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')#, desired_capabilities=capabilities)
#options=options)

driver.get('https://www.instagram.com/')

sleep(5)

elem = driver.find_element_by_name('emailOrPhone')
elem.send_keys(Email())

sleep(5)

elem = driver.find_element_by_name('fullName')
elem.send_keys(Name())

sleep(5)

name_consol = driver.find_element_by_name('username')
name_consol.send_keys(Username())

a = input()

driver.quit()
