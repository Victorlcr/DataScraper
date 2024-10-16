import requests
from bs4 import BeautifulSoup

def get_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup

def get_total_pages():
    soup = get_soup("https://books.toscrape.com/catalogue/page-1.html")

    total_pages = soup.find('li',class_ = 'current').text
    total_pages = total_pages.split()[-1]

    return int(total_pages)

def fetch_books(page_number):
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    # outra forma "https://books.toscrape.com/catalogue/page-"+page_number+".html"

    soup = get_soup(url)

    books = []

    book_items = soup.find_all('article', class_ = 'product_pod')

    for book_item in book_items:
        title = book_item.h3.a.get('title')
        price = book_item.find('p', class_ = 'price_color').text
        rating = book_item.find('p', class_ = 'star-rating').get('class')[1]
        #seleciona o segundo elemento da classe 'star-rating', o numero de estrelas
        stock = book_item.find('p', class_ = 'instock availability').text
        stock = stock.strip()

        books.append({'Title':title, 'Price':price, 'Star Rating':rating, 'In Stock':stock})

        print(books)

def main():
    for i in range(1, get_total_pages() + 1):
        print(f'Page: {i}')
        fetch_books(i)


main()