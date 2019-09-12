from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
from random import randint, choice
from ElemFunctions import Email, Name, Username, Password 


with open('Proxy.txt', 'r') as file:
	PROXY = str(file.read()).split('\n')


####Регистрация
accounts = []

meter = 0
while meter <= 10:

	###Подключение к Инстаграмму
	connect = False
	while not connect:
		options = webdriver.ChromeOptions()

		options.add_argument("--incognito")

		prox = Proxy()
		prox.proxy_type = ProxyType.MANUAL
		prox.ssl_proxy = choice(PROXY)

		capabilities = webdriver.DesiredCapabilities.CHROME

		prox.add_to_capabilities(capabilities)

		driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe', desired_capabilities=capabilities)#, options=options)

		try:
			driver.get("https://www.instagram.com/")
		except Exception as e:
			continue

		if 'Instagram' in driver.title:
			connect = True
		else:
			driver.quit()

	sleep(randint(8, 12))

	###Регистрация аккаунта
	email_consol = driver.find_element_by_name("emailOrPhone")

	email = Email()

	email_consol.send_keys(email)

	sleep(randint(8, 12))

	elem = driver.find_element_by_name('fullName')
	elem.send_keys(Name())

	sleep(randint(5, 10))

	keys = {'Username': Username(),
	'Password': Password()}

	name_consol = driver.find_element_by_name('username')
	name_consol.send_keys(keys['Username'])

	sleep(randint(5, 8))

	elem = driver.find_element_by_name('password')
	elem.send_keys(keys['Password'])

	sleep(randint(1, 5))

	elem.send_keys(Keys.ENTER)

	sleep(2)

	passage = False 
	while not passage:
		try:
			check = driver.find_element_by_id('ssfErrorAlert')
		except Exception as e:
			accounts.append(keys)

			meter += 1

			try:
				years = driver.find_element_by_name('ageRadio')
			except Exception as e:
				pass
			else:
				years.click()

			print(f'{meter} аккаунт готов :>')

			a = input()

			driver.quit()

			passage = True

		else:
			if check.text == f'Другой аккаунт уже использует эл. адрес {email}':
				email = Email()

				email_consol.clear()

				email_consol.send_keys(email)

			elif check.text == 'Это имя пользователя уже занято. Попробуйте другое.':
				keys['Username'] = username()

				name_consol.clear()

				name_consol.send_keys(keys['Username'])

			else:
				print('Неудачная попытка:(')
				passage = True

			elem.send_keys(Keys.ENTER)

	driver.delete_all_cookies()

	driver.quit()

	break

	sleep(randint(20, 120))
#######

###Просмотр истории спомощью InstaPy
set_workspace(path=None)

for i in range(len(accounts)):
	session = InstaPy(username=accounts[i]['Username'], password=accounts[i]['Password'], headless_browser=False)

	with smart_run(session):
		session.follow_by_list(['natsukisubaru2'])

		session.story_by_users(['natsukisubaru2'])
###########
