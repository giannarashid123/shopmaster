from ecommerce import Category, Product, Order

# Create categories
electronics = Category("Electronics")
clothes = Category("Clothes")

# Create products
laptop = Product("Laptop", 1200, electronics)
phone = Product("Phone", 800, electronics)
shirt = Product("Shirt", 40, clothes)

# Show category products
print("Electronics products:", electronics.products())
print("Clothes products:", clothes.products())

# Create an order
order1 = Order()
order1.add_product(laptop, 1)
order1.add_product(shirt, 3)

print("Order items:", order1.order_items())
print("Order products:", order1.products())
print("Order total cost:", order1.total_cost())
