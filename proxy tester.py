import requests

with open('Proxy list.txt', 'r') as file:
	proxy = file.read()
	proxy = proxy.split('\n')

link = 'https://www.instagram.com/'

with open('Proxy.txt', 'a') as file:
	for i in range(len(proxy)):
		elem = proxy[i]

		print('\nВсем встать суд идёт')
		defendant = {'ssl': elem}

		try:
			justice = requests.get(url=link, proxies=defendant)
		except Exception as e:
			print('Виновен')
			continue

		print('Присяжные думают')

		justice.close()

		print(justice.status_code)

		if justice.status_code == 200:
			print('Оправдан')
			file.write(f'{elem}\n')

		elif justice.status_code == 429:
			print(f'{i} {elem}')
			print('Судья сдох требуется замена')
			break

		else:
			print('Виновен')
