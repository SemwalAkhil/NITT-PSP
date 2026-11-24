# 5. Write a function to generate a product ID and store product details using default and keyword arguments.
# Input: (101 Keyboard 1500.0), (102 Mouse 500.0)
# Output: {'PROD0101': {'name': 'Keyboard', 'price': 1500.0}}, {'PROD0102': {'name': 'Mouse', 'price': 500.0}}

def addProduct(catalog: dict, prod_num: int = 1, name: str = "Unknown", price: float = 0.0):
    pid = f"PROD{prod_num:04d}"
    catalog[pid] = {"name": name, "price": price}
    return catalog

if __name__ == "__main__":
    products = {}
    p_num = int(input("Enter product number: "))
    p_name = input("Enter product name: ")
    p_price = float(input("Enter product price: "))
    addProduct(products, prod_num=p_num, name=p_name, price=p_price)
    print(products)
