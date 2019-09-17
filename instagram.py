from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from random import randint, choice
from ElemFunctions import Email, Name, Username, Password 

# options = ChromeOptions()

# options.add_argument("--incognito")

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.ssl_proxy = '217.29.62.211:47979'

capabilities = webdriver.DesiredCapabilities.CHROME

prox.add_to_capabilities(capabilities)

driver = Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe', desired_capabilities=capabilities)
#options=options)

driver.get('https://2ip.ru/')

a = input()

driver.quit()
