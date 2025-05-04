# Add the SKU data provided to the product catalog dictionary
product_catalog = {
    "SKU123":{"name": "Widget A","price": 19.99,"quantity": 50},
    "SKU456" : {"name": "Gadget B","price": 34.95,"quantity": 25},
    "SKU789" : {"name": "Gizmo C","price": 9.99,"quantity": 100},
    "SKU321": {"name": "New Widget", "price": 29.99, "quantity": 30}
    
} 
sku_to_lookup = input("Enter the SKU to lookup: ")
if sku_to_lookup in product_catalog:
    price=product_catalog[sku_to_lookup]["price"]
    print(f"The price of {product_catalog[sku_to_lookup]['name']} is ${price}")
else:
    print("SKU not found in catalog.")
    
# Function to add a new product
def add_product(sku, name, price , quantity):
    if sku in product_catalog:
        print("! This SKU already exist. ")
    else:
        product_catalog[sku]={
            "name": name,
            "price": price,
            "quantity": quantity
        }
        print(f"product '{name}' added succesfully!")
        
# Function to update-function design
def update_product(sku: str, *, name: str = None,
                   price: float = None, quantity: int = None) -> None:
    """
    Update one or more fields of a product.

    Parameters
    ----------
    sku : str
        SKU to update.
    name : str, optional
        New product name.
    price : float, optional
        New price.
    quantity : int, optional
        New quantity on hand.

    Returns
    -------
    None
    """
    product = product_catalog.get(sku)
    if product is None:
        print("❌  SKU not found.")
        return

    if name is not None:
        product["name"] = name
    if price is not None:
        product["price"] = price
    if quantity is not None:
        product["quantity"] = quantity

    print(f"✅  {sku} updated → {product}")
# 1. Change price only
update_product("SKU123", price=21.50)

# 2. Change quantity only
update_product("SKU456", quantity=40)

# 3. Change name + price + quantity
update_product("SKU789", name="Gizmo C (2nd Gen)", price=11.49, quantity=80)

# 4. Attempt to update a non‑existent item
update_product("SKU000", price=5.00)
