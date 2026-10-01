#: Inventory & Order Management System
products = [
    {
        "id": 101,
        "name": "Laptop",
        "price": 120000,
        "stock": 10,
        "categories": ("electronics", "computer")
    },
    {
        "id": 102,
        "name": "Mouse",
        "price": 2500,
        "stock": 25,
        "categories": ("electronics", "accessories")
    },
    {
        "id": 103,
        "name": "Keyboard",
        "price": 5000,
        "stock": 15,
        "categories": ("electronics", "accessories")
    }
]
def show_products(products):
    for product in products:
        print(
            f'ID: {product["id"]} | '
            f'Name: {product["name"]} | '
            f'Price: {product["price"]} | '
            f'Stock: {product["stock"]}'
        )

def add_product(products, product):
    products.append(product)
    print("Product added successfully.")


def search_product(products, product_name):
    for product in products:
        if product["name"].lower() == product_name.lower():
            return product
    return None

def update_stock(products, product_id, new_stock):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = new_stock
            print("Stock updated successfully.")
            return
    print("Product not found.")
def delete_product(products, product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product deleted successfully.")
            return
    print("Product not found.")
def calculate_inventory_value(products):
    total = 0
    for product in products:
        total += product["price"] * product["stock"]
    return total
show_products(products)
new_product = {
    "id": 104,
    "name": "Headphones",
    "price": 7000,
    "stock": 20,
    "categories": ("electronics", "audio")
}
add_product(products, new_product)
result = search_product(products, "Laptop")
print("Search Result:")
print(result)
update_stock(products, 101, 20)
delete_product(products, 102)
total = calculate_inventory_value(products)
print("Total Inventory Value:", total)
print("Final Products:")

show_products(products)
#(1)simple project 
