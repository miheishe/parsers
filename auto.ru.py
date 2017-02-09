import urllib.request
from bs4 import BeautifulSoup

URL = 'http://auto.ru'


def save(result, path):
    f = open(path, 'w')
    f.write('Название;Статус;Ссылка\n')
    for jumper in result:
        f.write(jumper['Name'] + ';' + jumper['Status'] + ';' + jumper['URL'] + '\n')
    f.close()


def gethtml(url):
    resp = urllib.request.urlopen(url)
    return resp.read()


def parse(html):

    # result = []
    soup = BeautifulSoup(html, "html.parser")
    print(soup)
    # allquests = soup.find('div', class_='row')
    # quests = allquests.find_all('h4')
    #
    # for jumper in quests:
    #     name = jumper.a.text
    #     try:
    #         closed = jumper.span.text
    #     except:
    #         closed = 'OPEN'
    #
    #     result.append({
    #         'Name': name,
    #         'Status': closed,
    #         'URL': MIR_KVESTOV_URL + jumper.a.get('href')[7:]
    #     })
    return result


def main():
    parse(gethtml(URL))


if __name__ == '__main__':
    main()