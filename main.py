import bs4
import requests


class Web_Scp():

    def __init__(self):
        self.URL = 'https://habr.com' # для удобства создания ссылок в дальнейшем
        self.direct = '/ru/all/'
        self.KEYWORDS = ['дизайн', 'фото', 'web', 'python']


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
            elements.append(f'{datatime} - {name_article} - {link}')
        return elements


    def search_coincidence(self):
        article_ls = []
        for name in self.pars_text():
            if name in self.KEYWORDS:
                print(name)
                article_ls.append(name)
        if len(article_ls) == 0:
            print(f"[!] На данный момент нет совпадений по {self.KEYWORDS}.")
        return article_ls

    # у меня получился пустой список так как небыло совпадений


if __name__ == '__main__':
    test = Web_Scp()
    test.search_coincidence()