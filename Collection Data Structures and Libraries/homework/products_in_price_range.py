"""
Write a program to read a large collection of products (name + price)
and efficiently find the first 20 products in the price range
[a…b] ordered by price.
Test for 500 000 products and 10 000 price searches.
"""
from sortedcontainers import sorteddict

class Product:
    def __init__(self, product, cost: float):
        self.product = product
        self.cost = cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __hash__(self):
        return hash(self.cost)

    def __str__(self):
        return '{product} - ${cost}'.format(product=self.product, cost=self.cost)


def main():
    n = int(input())
    sorted_products = fill_set(n)
    cost_range_start, cost_range_end = [float(part) for part in input().split()]
    for idx in sorted_products.irange(minimum=cost_range_start, maximum=cost_range_end):
        for product in sorted_products[idx]:
            print('{cost} {prod}'.format(cost=product.cost, prod=product.product))


def fill_set(count: int):
    products = sorteddict.SortedDict()
    for _ in range(count):
        product, price = input().split()
        price = float(price)
        if price not in products.keys():
            products[price] = []
        products[price].append(Product(product, price))
    return products

if __name__ == '__main__':
    main()