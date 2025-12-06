class OrderItem:
    all = []

    def __init__(self, order, product, quantity):
        self.order = order
        self.product = product
        self.quantity = quantity
        OrderItem.all.append(self)

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, val):
        from .order import Order
        if not isinstance(val, Order):
            raise TypeError("Order must be an Order instance")
        self._order = val

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self, val):
        from .product import Product
        if not isinstance(val, Product):
            raise TypeError("Product must be a Product instance")
        self._product = val

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, val):
        if not isinstance(val, int) or val < 1:
            raise ValueError("Quantity must be a positive integer")
        self._quantity = val

    def __repr__(self):
        return f"OrderItem({self.product}, qty={self.quantity})"
