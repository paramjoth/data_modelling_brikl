#Data Modeling
#Python Classes:

class Product:
    def __init__(self, id, title, description, price, available_date, stock_quantity, product_images, categories=None):
        self.id =  id
        self.title = title
        self.description =  description
        self.price = price
        self.available_date =  available_date
        self.stock_quantity = stock_quantity
        self.product_images =  product_images
        self.categories = categories if categories else []

class StoreFront:
    def __init__(self, id):
        self.id = id
        self.inventory = []

    def filter_by_category(self, category):
        matches = [item for item in self.inventory if category in item.categories]
        return matches

    def filter_by_oldest(self):
        matches = sorted(self.inventory, key=lambda item: item.available_date)
        return matches

    def filter_by_newest(self):
        matches = sorted(self.inventory, key=lambda item: item.available_date, reverse=True)

    def filter_by_availablity(self, available):
        matches = [item for item in self.inventory if available and item.stock_quantity > 0]
        return matches

class MicroStore:
    def __init__(self, id, store_id, promotional_products):
        self.id = id
        self.store_id = store_id
        self.promotional_products = promotional_products

class User:
    def __init__(selfself, id, user_name):
        self.id = id
        self.user_name = user_name
        self.products = []

class CustomizeProduct(Product):
    def __init__(self, id, title, description, price, available_date, stock_quantity, product_images,categories=None,custom_details):
        super().__init__(id, title, description, price, available_date, stock_quantity, product_images, categories)
        self.custom_details = custom_details

