"""
A large trade company has millions of products, each described by id (unique), title, supplier and price.
Implement a data structure to store them that allows:

Add new product (if the id already exists, the new product replaces the old one)
Remove product by id – returns true or false

Find products in given price range [x…y] – returns the products sorted by id
Find products by title – returns the products sorted by id

Find products by title + price – returns the products sorted by id
Find products by title + price range – returns the products sorted by id

Find products by supplier + price – returns the products sorted by id
Find products by supplier + price range – returns the products sorted by id
"""
from sortedcontainers import SortedDict, SortedSet


class Product:
    def __init__(self, id, title: str, supplier: str, price: int):
        self.id = id
        self.title = title
        self.supplier = supplier
        self.price = price

    def __str__(self):
        return "{title} from {supplier} at ${price} with ID {id}".format(
            title=self.title, supplier=self.supplier, price=self.price, id=self.id
        )

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __gt__(self, other):
        return self.id > other.id

    def __lt__(self, other):
        return self.id < other.id


#  You are now entering Memory Waste City
class ProductCollection:
    def __init__(self):
        self.products = {}
        self.products_by_title = {}
        self.products_by_price = SortedDict()
        self.products_by_price_and_title = {}
        self.products_by_price_and_supplier = {}

    def add(self, product):
        self._add_to_products_by_id(product)
        self._add_to_products_by_title(product)
        self._add_to_products_by_price(product)
        self._add_to_products_by_price_and_title(product)
        self._add_to_products_by_price_and_supplier(product)

    def remove(self, _id):
        if _id not in self.products:
            return False
        product = self.products[_id]
        self._remove_from_products(product)
        self._remove_from_products_by_title(product)
        self._remove_from_products_by_price(product)
        self._remove_from_products_by_price_and_title(product)
        self._remove_from_products_by_price_and_supplier(product)

    def find_products_in_price_range(self, start_price, end_price):
        if start_price < 0 or start_price > end_price:
            raise Exception('Invalid price range!')
        prices = self.products_by_price.irange(start_price, end_price)
        return (product for price in prices for product in self.products_by_price[price])

    def find_products_by_title(self, title: str):
        if title not in self.products_by_title:
            return []
        return (product for product in self.products_by_title[title])

    def find_products_by_title_and_price(self, title, price):
        if title not in self.products_by_price_and_title or price not in self.products_by_price_and_title[title]:
            return []

        return (product for product in self.products_by_price_and_title[title][price])

    def find_products_by_title_and_price_range(self, title, start_price, end_price):
        if title not in self.products_by_price_and_title:
            return []
        if start_price < 0 or start_price > end_price:
            raise Exception('Invalid price range!')

        prices = self.products_by_price_and_title[title].irange(start_price, end_price)
        return (product for price in prices for product in self.products_by_price_and_title[title][price])

    def find_products_by_supplier_and_price(self, supplier, price):
        if (supplier not in self.products_by_price_and_supplier
           or price not in self.products_by_price_and_supplier[supplier]):
            return []

        return (product for product in self.products_by_price_and_supplier[supplier][price])

    def find_products_by_supplier_and_price_range(self, supplier, start_price, end_price):
        if supplier not in self.products_by_price_and_supplier:
            return []
        if start_price < 0 or start_price > end_price:
            raise Exception('Invalid price range!')

        prices = self.products_by_price_and_supplier[supplier].irange(start_price, end_price)

        return (product for price in prices for product in self.products_by_price_and_supplier[supplier][price])

    def _add_to_products_by_id(self, product):
        self.products[product.id] = product

    def _remove_from_products(self, product):
        del self.products[product.id]

    def _add_to_products_by_title(self, product):
        if product.title not in self.products_by_title:
            self.products_by_title[product.title] = SortedSet()
        self.products_by_title[product.title].add(product)

    def _remove_from_products_by_title(self, product):
        self.products_by_title[product.title].remove(product)

    def _add_to_products_by_price(self, product):
        if product.price not in self.products_by_price:
            self.products_by_price[product.price] = SortedSet()

        self.products_by_price[product.price].add(product)

    def _remove_from_products_by_price(self, product):
        self.products_by_price[product.price].remove(product)

    def _add_to_products_by_price_and_title(self, product):
        if product.title not in self.products_by_price_and_title:
            self.products_by_price_and_title[product.title] = SortedDict()
        if product.price not in self.products_by_price_and_title[product.title]:
            self.products_by_price_and_title[product.title][product.price] = SortedSet()
        self.products_by_price_and_title[product.title][product.price].add(product)

    def _remove_from_products_by_price_and_title(self, product):
        self.products_by_price_and_title[product.title][product.price].remove(product)

    def _add_to_products_by_price_and_supplier(self, product):
        if product.supplier not in self.products_by_price_and_supplier:
            self.products_by_price_and_supplier[product.supplier] = SortedDict()
        if product.price not in self.products_by_price_and_supplier[product.supplier]:
            self.products_by_price_and_supplier[product.supplier][product.price] = SortedSet()
        self.products_by_price_and_supplier[product.supplier][product.price].add(product)

    def _remove_from_products_by_price_and_supplier(self, product):
        self.products_by_price_and_supplier[product.supplier][product.price].remove(product)




plushiesh = Product(id="213", title="Plushyy", supplier="Memory foam Ood", price=33)
bears = Product(id="214", title="Plushyy", supplier="Memory foam Ood", price=34)
foam = Product(id="200", title="Foam", supplier="Memory foam Ood", price=1000)
king = Product(id="111", title="santa", supplier="Some", price=1)

products = ProductCollection()
products.add(plushiesh)
products.add(bears)
products.add(foam)
products.add(king)

print(list(products.find_products_by_supplier_and_price("Memory foam Ood", 34)))
print(list(products.find_products_by_supplier_and_price_range("Memory foam Ood", 30, 35)))

print(list(products.find_products_by_title("Plushyy")))

print(list(products.find_products_by_title_and_price("Plushyy", 33)))
print(list(products.find_products_by_title_and_price_range("Plushyy", 33, 34)))

print(list(products.find_products_in_price_range(1, 33)))

# remove them
products.remove(plushiesh.id)
products.remove(bears.id)
products.remove(foam.id)
products.remove(king.id)

# should return empty arrays
print(list(products.find_products_by_supplier_and_price("Memory foam Ood", 34)))
print(list(products.find_products_by_supplier_and_price_range("Memory foam Ood", 30, 35)))

print(list(products.find_products_by_title("Plushyy")))

print(list(products.find_products_by_title_and_price("Plushyy", 33)))
print(list(products.find_products_by_title_and_price_range("Plushyy", 33, 34)))

print(list(products.find_products_in_price_range(1, 33)))