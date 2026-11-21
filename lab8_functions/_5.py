def addProduct(catalog: dict, prod_num: int = 1, name: str = "Unknown", price: float = 0.0):
    pid = f"PROD{prod_num:04d}"
    catalog[pid] = {"name": name, "price": price}
    return catalog

if __name__ == "__main__":
    products = {}
    addProduct(products, prod_num=101, name="Keyboard", price=1500.0)
    addProduct(products, 102, "Mouse", 500.0)
    addProduct(products)
    print(products)
