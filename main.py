import bs4
import requests


class Web_Scp():
    '''класс только в качестве тренировки ООП'''

    def __init__(self):
        self.URL = 'https://habr.com' # для удобства создания ссылок в дальнейшем
        self.direct = '/ru/all/'
        self.KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'для'] # добавил "для", так как бывает нет совпадений


    def _text_page(self) -> str:
        response = requests.get(url=self.URL+self.direct, timeout=10)
        return response.text


    def pars_text(self) -> list: # список полученных статей в формате "дата-название-ссылка"
        link_ls = []
        elements = []
        soup = bs4.BeautifulSoup(self._text_page(), 'html.parser')
        for coin in soup.find_all('article'):
            datatime = coin.time['title']
            name_article = coin.find(class_='tm-article-snippet__title-link').span.text
            link = f"{self.URL + coin.find(class_='tm-article-snippet__title-link')['href']}"
            coin_ = set(name_article.split()) & set(self.KEYWORDS)
            if len(coin_) > 0:
                elements.append(f'{datatime} - {name_article} - {link}')
                link_ls.append(link)
        return (link_ls, elements)


    def show_ls(self):
        print(self.pars_text()[1])


    def text_page(self) -> str:
        question = input('Show link text? y/n: ')
        if question == 'n':
            exit()
        elif question == 'y':
            number_article = int(input('Enter number article: '))
            if 0 <= number_article <= len(self.pars_text()[0]):
                response = requests.get(self.pars_text()[0][number_article], timeout=5)
                soup = bs4.BeautifulSoup(response.text, 'html.parser')
                for article in soup.find_all(id='post-content-body'):
                    text_page = article.findNext('div').text # текст ссылки, далее ищем всё что душа пожелает
                print(text_page)
                return text_page
            else:
                print('Number is not found')
                self.text_page()
        else:
            self.text_page()
        return


if __name__ == '__main__':
    test = Web_Scp()
    test.show_ls()
    test.text_page()