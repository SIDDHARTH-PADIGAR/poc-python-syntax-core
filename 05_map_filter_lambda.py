from typing import NamedTuple, Iterable


#  mock input: Inventory Data 

class Product(NamedTuple):
    id: int
    name: str
    price: float
    in_stock: bool


products: list[Product] = [
    Product(1, "Keyboard", 1500.00, True),
    Product(2, "Monitor", 7999.99, False),
    Product(3, "Mouse", 699.00, True),
    Product(4, "Laptop Stand", 1299.50, True),
    Product(5, "Webcam", 3499.00, False)
]

#  use case 1: Apply discounts using map + lambda 

apply_discount = lambda p: Product(p.id, p.name, round(p.price * 0.9, 2), p.in_stock)
discounted_products = list(map(apply_discount, products))


#  use case 2: Filter in-stock items 

in_stock_products = list(filter(lambda p: p.in_stock, products))


#  use case 3: Check if any product is under ₹1000 

has_cheap_items = any(p.price < 1000 for p in products)

#  use case 4: Ensure all products have names 

all_named = all(bool(p.name.strip()) for p in products)

#  use case 5: Aggregate price of in-stock items 

def total_stock_value(items: Iterable[Product]) -> float:
    return sum(p.price for p in items if p.in_stock)


if __name__ == "__main__":
    print("Original Prices:", [p.price for p in products])
   
