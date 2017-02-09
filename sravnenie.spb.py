import urllib.request
from bs4 import BeautifulSoup

URL_1 = 'http://mir-kvestov.ru/quests'
URL_2 = 'http://kvest-komnata.net/vse-kvest-komnati-v-moskve/'
FILE_NAME = 'sravnenie.csv'

def save(result1, result2, path):
	f = open(path, 'w')
	f.write('Мир Квестов; ; ; ;Квест Комната\n')
	f.write('Название;Статус;Ссылка;;Название;Ссылка\n')
	exitstring1 = ''
	
	for jumper in result1:
		exitstring1 = jumper['Name'] + ';' + jumper['Status'] + ';' + jumper['URL'] + ';;'
		exitstring2 = ''
		for jumper2 in range(0,len(result2)-1):
			if jumper['Name'].lower() ==  result2[jumper2]['Name'].lower():
				exitstring2 = result2[jumper2]['Name'] + ';' + result2[jumper2]['URL']
				del(result2[jumper2])
				break
			
		f.write(exitstring1 + exitstring2 + '\n')
	if len(result2) != 0:
		for jumper2 in result2:
			f.write(' ; ; ; ;' + jumper2['Name'] + ';' + jumper2['URL'] + '\n')
	f.close

def gethtml(url):
	resp = urllib.request.urlopen(url)
	return resp.read()

def parse_mk(html):
	result = []
	soup = BeautifulSoup(html, "html.parser")
	allquests = soup.find('div', class_='row')
	quests = allquests.find_all('h4')

	for jumper in quests:
		name = jumper.a.text
		try:
			closed = jumper.span.text
		except:
			closed = 'OPEN'
	
		result.append({
			'Name':name,
			'Status':closed,
			'URL': URL_1 + jumper.a.get('href')[7:]
			})
	return result

def parse_kk(html):
	result = []
	soup = BeautifulSoup(html, "html.parser")
	allquests = soup.find('div', class_='cont catalog list-catalog')
	quests = allquests.find_all('h3')
	for jumper in quests:
		name = jumper.a.text.strip()
		result.append({
			'Name':name[6:],
			'URL': jumper.a.get('href')
			})
	return result

	


def main():
	mk = []
	kk = []
	mk = parse_mk(gethtml(URL_1))
	kk = parse_kk(gethtml(URL_2))

	save(mk, kk, FILE_NAME)



if __name__ == '__main__':
	main()