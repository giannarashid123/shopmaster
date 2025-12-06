class Product:
    all = []

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        Product.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not isinstance(val, str) or val.strip() == "":
            raise ValueError("Product name must be a non-empty string")
        self._name = val

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, val):
        if not isinstance(val, (int, float)) or val <= 0:
            raise ValueError("Price must be a positive number")
        self._price = val

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, val):
        from .category import Category
        if not isinstance(val, Category):
            raise TypeError("category must be a Category instance")
        self._category = val

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"
