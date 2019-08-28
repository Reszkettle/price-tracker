import requests
from bs4 import BeautifulSoup
import re

URL = "https://helion.pl/ksiazki/java-dla-zupelnie-poczatkujacych-owoce-programowania-wydanie-vii-tony-gaddis,javzp2.htm#format/d"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
book_pattern = str(soup.find_all("p", class_="book-price"))
pattern = re.compile(pattern=r"\d+[,.]\d+")
book_prices = pattern.findall(book_pattern)
if len(book_prices) == 4:
    _, book_price, _, ebook_price = book_prices


#book_price, _, ebook_price = book_prices
print(book_prices)
