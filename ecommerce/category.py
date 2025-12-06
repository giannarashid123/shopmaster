class Category:
    all = []

    def __init__(self, name):
        self.name = name
        Category.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or value.strip() == "":
            raise ValueError("Category name must be a non-empty string")
        self._name = value

    def products(self):
        """Return all products belonging to this category."""
        from .product import Product
        return [p for p in Product.all if p.category == self]

    def __repr__(self):
        return f"Category('{self.name}')"
