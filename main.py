import bs4
import requests


class Web_Scp():

    def __init__(self):
        self.URL = 'https://habr.com' # для удобства создания ссылок в дальнейшем
        self.direct = '/ru/all/'
        self.KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'для']


    def text_page(self) -> str:
        response = requests.get(url=self.URL+self.direct, timeout=10)
        return response.text


    def pars_text(self) -> list: # список полученных статей в формате "дата-название-ссылка"
        elements = []
        soup = bs4.BeautifulSoup(self.text_page(), 'html.parser')
        for coin in soup.find_all('article'):
            datatime = coin.time['title']
            name_article = coin.find(class_='tm-article-snippet__title-link').span.text
            link = f"{self.URL + coin.find(class_='tm-article-snippet__title-link')['href']}"
            coin_ = set(name_article.split()) & set(self.KEYWORDS)
            if len(coin_) > 0:
                elements.append(f'{datatime} - {name_article} - {link}')
        print(elements)
        return elements


if __name__ == '__main__':
    test = Web_Scp()
    test.pars_text()