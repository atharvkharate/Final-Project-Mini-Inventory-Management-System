import json

FILE_NAME = "inventory.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)


def add_product(data):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    data.append(product)
    save_data(data)
    print("✅ Product added!")


def view_products(data):
    if not data:
        print("No products found.")
        return

    for i, p in enumerate(data):
        print(f"\nID: {i}")
        print(f"Name: {p['name']}")
        print(f"Quantity: {p['quantity']}")
        print(f"Price: ₹{p['price']}")


def update_product(data):
    view_products(data)
    try:
        index = int(input("Enter ID to update: "))
        product = data[index]

        print("Leave blank to keep old value")

        name = input(f"New name ({product['name']}): ") or product['name']
        quantity = input(f"New quantity ({product['quantity']}): ")
        price = input(f"New price ({product['price']}): ")

        data[index] = {
            "name": name,
            "quantity": int(quantity) if quantity else product['quantity'],
            "price": float(price) if price else product['price']
        }

        save_data(data)
        print("✏️ Product updated!")

    except:
        print("Invalid ID")


def delete_product(data):
    view_products(data)
    try:
        index = int(input("Enter ID to delete: "))
        data.pop(index)
        save_data(data)
        print("❌ Product deleted!")
    except:
        print("Invalid ID")


def search_product(data):
    keyword = input("Enter product name to search: ").lower()

    found = False
    for p in data:
        if keyword in p["name"].lower():
            print("\nFound:")
            print(f"Name: {p['name']}")
            print(f"Quantity: {p['quantity']}")
            print(f"Price: ₹{p['price']}")
            found = True

    if not found:
        print("No matching product found.")


def main():
    data = load_data()

    while True:
        print("\n===== Inventory System =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product(data)
        elif choice == "2":
            view_products(data)
        elif choice == "3":
            update_product(data)
        elif choice == "4":
            delete_product(data)
        elif choice == "5":
            search_product(data)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

main()