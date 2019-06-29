import datetime
import os
import random
from bs4 import BeautifulSoup
import requests


class DBBooks_Spider():
    url = "http://book.douban.com/top250?start=0"
    page_num = 0
    top_num = 1
    headers = [
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'},
        {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
        {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'},
        {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0'},
        {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/44.0.2403.89 Chrome/44.0.2403.89 Safari/537.36'}
    ]
    file_path = ("Books/")

    def spider_man(self):
        page_request = requests.get(self.url + str(self.page_num * 25), headers=random.choice(self.headers))
        page_bsObj = BeautifulSoup(page_request.text, 'html.parser')
        books_items = page_bsObj.find_all("a")
        for item in books_items:
            if 'title' in item.attrs:
                self.flash_man(item.attrs['href'])
                self.top_num += 1

    def flash_man(self, book_url):
        print("book_url is: " + book_url)
        rep = requests.get(book_url, headers=random.choice(self.headers))
        if rep.status_code == 200:
            book_bsObj = BeautifulSoup(rep.text, 'html.parser')
            title = book_bsObj.h1.span.text
            book_info = book_bsObj.find('div', {'id': 'info'})
            with open('book.txt', 'a', encoding='utf-8') as f:
                f.write('\n------------------------------------------')
                f.write('\n【' + title.strip() + '】\n')
                info_text = book_info.text.split(' ')
                for info in info_text:
                    if info != '\n' and info != '':
                        f.write(info.strip())

    def __init__(self):
        while (self.page_num <= 9):
            self.spider_man()
            self.page_num += 1


sp = DBBooks_Spider()
