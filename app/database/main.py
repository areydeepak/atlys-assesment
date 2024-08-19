import json
from pathlib import Path

class Database:
    def __init__(self, file_path="products.json"):
        self.file_path = Path(file_path)

    def save_product(self, product):
        products = self.load_products()
        products.append(product)
        with open(self.file_path, "w") as file:
            json.dump(products, file, indent=4)

    def load_products(self):
        if self.file_path.exists():
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []
