from collections import defaultdict

inventory = {}

def add_product(inventory, product_id, name, price, quantity, category):
    if product_id in inventory:
        print("Error: Product ID already exists.")
    else:
        inventory[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        }

def update_product(inventory, product_id, **kwargs):
    if product_id in inventory:
        for key, value in kwargs.items():
            if key in inventory[product_id]:
                inventory[product_id][key] = value
    else:
        print("Error: Product not found.")

def delete_product(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]
    else:
        print("Error: Product not found.")

def get_product(inventory, product_id):
    return inventory.get(product_id, "Product not found.")

def list_by_category(inventory, category):
    return [p for p in inventory.values() if p["category"] == category]
