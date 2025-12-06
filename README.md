
---

## 🛠 Features

### 1. Classes and Relationships
- **Category**: Stores all categories and has a method `products()` to get products in that category.
- **Product**: Belongs to a `Category` and stores product details (name, price).
- **OrderItem**: Represents a product in an order with a specific quantity.
- **Order**: Stores all order items and can calculate total cost.

### 2. Validations
- Ensures names are non-empty strings.
- Prices must be positive numbers.
- Quantity must be a positive integer.
- Relationships are type-checked:
  - Product must belong to a `Category`.
  - OrderItem must belong to an `Order` and `Product`.

### 3. Aggregation and Association Methods
- `Category.products()` → Returns all products in a category.
- `Order.order_items()` → Returns all order items in an order.
- `Order.products()` → Returns all products in an order.
- `Order.total_cost()` → Calculates total cost of the order.

---

## ⚡ How to Run

1. Clone the repository or unzip the project folder.
2. Navigate to the project directory.
3. Run the test script:

```bash
python3 test.py
