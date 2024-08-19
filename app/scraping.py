import requests
from bs4 import BeautifulSoup
from utils.retry import retry
from config import *
import re

class Scraper:
    def __init__(self, pages, proxy, cache, db):
        self.pages = pages
        self.proxy = proxy
        self.cache = cache
        self.db = db

    @retry
    def scrape_page(self, url):
        response = requests.get(url, proxies={"http": self.proxy, "https": self.proxy})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            product_divs = soup.find_all('div', class_='product-inner clearfix')

            products = []

            for product in product_divs:
                title = product.find('h2', class_='woo-loop-product__title').get_text(strip=True)
                
                price_container = product.find('span', class_='price')
                if price_container:
                    price_ins = price_container.find('ins') or price_container.find('span', class_='woocommerce-Price-amount amount')
                    if price_ins:
                        price = price_ins.get_text(strip=True)
                        price = float(re.sub(r'[^\d.]', '', price))
                    else:
                        price = -1
                else:
                    price = -1

                image_tag = product.find('img', class_='attachment-woocommerce_thumbnail')
                image_url = image_tag.get('data-lazy-src', image_tag.get('src')) if image_tag else None

                products.append({
                    "product_title": title,
                    "product_price": price,
                    "path_to_image": image_url
                })
            return products
        return []

    def scrape(self):
        data = []
        for page in range(1, self.pages + 1):
            url = BASE_URL + str(page)
            data.extend(self.scrape_page(url))
        return data

    def save_data(self, products):
        for product in products:
            cached_price = self.cache.get(product['product_title'])
            if cached_price != str(product['product_price']) and product['product_price'] != -1:
                self.db.save_product(product)
                self.cache.set(product['product_title'], product['product_price'])

    def notify(self, products):
        print(f"{len(products)} products scraped and saved.")
