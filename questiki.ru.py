import urllib.request
from bs4 import BeautifulSoup

MAIN_URL = 'http://questiki.ru/list/page'


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
    #allquests = soup.find('table')

    quests = soup.find_all('div', class_='QstDivName')
    for jumper in quests:
        name = jumper.a.text.strip()
        result.append({
            'Name': name,
            'URL': 'questiki.ru' + jumper.a.get('href')
        })
    return result


def main():
    qq = []
    for i in range(12):
        qq.extend(parse(gethtml(MAIN_URL + str(i))))
    save(qq, 'questiki.ru--29_11_2016.csv')


if __name__ == '__main__':
    main()