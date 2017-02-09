import urllib.request
from bs4 import BeautifulSoup

MAIN_URL = 'http://kvest-komnata.net/vse-kvest-komnati-v-moskve/'

def save(result, path):
	f = open(path, 'w')
	f.write('Название;Ссылка\n')
	for jumper in result:
		f.write(jumper['Name'] + ';' + jumper['URL'] + '\n')
	f.close()

def gethtml(url):
	resp = urllib.request.urlopen(url)
	return resp.read()

def parse(html):
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
	print(result)
	return result

	


def main():
	save(parse(gethtml(MAIN_URL)),'kvest-komnata_msk--14_11_2016.csv')
	


if __name__ == '__main__':
	main()