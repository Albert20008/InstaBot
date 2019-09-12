from selenium import webdriver
from random import choice
from time import sleep

def Email():
	driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

	connect = False
	while not connect:
		try:
			driver.get('https://ru.mail-fake.com/')
		except Exception as e:
			continue

		if 'Электронная почта - временная почта, одноразовая почта' in driver.title:
			connect = True
		else:
			driver.quit()

	sleep(2)

	email = driver.find_element_by_id('email_ch_text').text

	driver.quit()

	return email

def Name():
	driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

	link = choice(['http://en.castlots.org/male-name-generator/', 'http://en.castlots.org/famale-name-generator/'])

	connect = False
	while not connect:
		try:
			driver.get(link)
		except Exception as e:
			continue

		if 'Male Name Generator' in driver.title:
			connect = True
		else:
			driver.quit()

	driver.find_element_by_id('random-button-en').click()

	sleep(2)

	name = choice(driver.find_element_by_class_name('name').text.split('\n'))

	driver.quit()

	return name


def Username():
	driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

	connect = False
	while not connect:
		try:
			driver.get('https://genword.ru/generators/nicknames/')
		except Exception as e:
			continue

		if 'Генератор ников' in driver.title:
			connect = True
		else:
			driver.quit()
	
	driver.find_element_by_class_name('btn.btn-info').click()

	username = driver.find_element_by_class_name('result').text.split('\n')

	driver.quit()

	return username


def Password():
	driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')

	connect = False
	while not connect:
		try:
			driver.get('http://en.castlots.org/password-generator-online/')
		except Exception as e:
			continue

		if 'Random Password Generator online' in driver.title:
			connect = True
		else:
			driver.quit()

	sleep(2)

	password = choice(driver.find_element_by_name('text').text.split('\n'))

	driver.quit()

	return password
