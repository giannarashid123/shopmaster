from .order_item import OrderItem

class Order:
    all = []

    def __init__(self):
        Order.all.append(self)

    def order_items(self):
        return [oi for oi in OrderItem.all if oi.order == self]

    def products(self):
        return [oi.product for oi in self.order_items()]

    def add_product(self, product, quantity=1):
        from .product import Product
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")
        OrderItem(self, product, quantity)

    def total_cost(self):
        return sum(oi.product.price * oi.quantity for oi in self.order_items())

    def __repr__(self):
        return f"Order({len(self.order_items())} items)"
