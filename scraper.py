import requests
import lxml.html as html

HOME_URL = 'http://books.toscrape.com/'

CATEGORY_BOOK_NAME = '//ul[@class="nav nav-list"]/li/ul/li/a/text()'
CATEGORY_LINK = '//ul[@class="nav nav-list"]/li/ul/li/a/@href'


response = requests.get(HOME_URL)

if response.status_code == 200:
    home = response.content.decode('utf-8')
    parsed = html.fromstring(home)
    link_book = parsed.xpath(CATEGORY_LINK)
    book_name = parsed.xpath(CATEGORY_BOOK_NAME)

    

print(book_name.replace)
