from inventory import *

# Sample test cases
add_product(inventory, "P001", "Laptop", 799.99, 10, "Electronics")
add_product(inventory, "P002", "Coffee Mug", 9.99, 100, "Kitchenware")
update_product(inventory, "P001", price=749.99, quantity=8)
delete_product(inventory, "P002")

print("Product P001:", get_product(inventory, "P001"))
print("Electronics Category:", list_by_category(inventory, "Electronics"))
