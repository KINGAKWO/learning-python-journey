import pytest

from inventory_system import product_catalog, lookup_product, add_product, update_product, remove_product, display_inventory


def test_lookup_product():
    # Test the lookup function with a SKU that exists in the catalog
    assert lookup_product("SKU123") == {
        "name": "Widget A",
        "price": 19.99,
        "quantity": 50
    }
    
    # Test the lookup function with a SKU that does not exist in the catalog
    assert lookup_product("SKU987") is None

def test_add_product():
    # Test adding a new product to the catalog
    add_product("SKU000", "New Widget", 29.99, 30)
    
    # Verify that the product was added correctly
    assert product_catalog["SKU000"] == {
        "name": "New Widget",
        "price": 29.99,
        "quantity": 30
    }
    
    # Test adding a product with an existing SKU
    with pytest.raises(ValueError):
        add_product("SKU123", "Updated Widget", 25.99, 40)

def test_update_product():
    # Test updating the name of a product
    update_product("SKU789", name="Gizmo C (2nd Gen)")
    
    # Verify that the name was updated correctly
    assert product_catalog["SKU789"]["name"] == "Gizmo C (2nd Gen)"
    
    # Test updating the price of a product
    update_product("SKU456", price=30.95)
    
    # Verify that the price was updated correctly
    assert product_catalog["SKU456"]["price"] == 30.95
    
    # Test updating the quantity of a product
    update_product("SKU123", quantity=45)
    
    # Verify that the quantity was updated correctly
    assert product_catalog["SKU123"]["quantity"] == 45
    
    # Test attempting to update non-existent item
    with pytest.raises(KeyError):
        update_product("SKU000", name="New Widget")
    
    # Test updating a product with invalid SKU
    with pytest.raises(ValueError, match=r"❌  SKU not found"):
        update_product("INVALID_SKU", name="Invalid Product", price=0.00, quantity=0)
        
    # Test updating a product with invalid price
    with pytest.raises(ValueError, match=r"❌  Invalid price provided.*"):
        update_product("SKU321", price=-10.00)
        
    # Test updating a product with invalid quantity
    with pytest.raises(ValueError, match=r"❌  Invalid quantity provided.*"):
        update_product("SKU123", quantity=-5)
        
    # Test updating a product with invalid name
    with pytest.raises(ValueError, match=r"❌  Name cannot be empty.*"):
        update_product("SKU456", name="")
    
    # Test updating a product with invalid name (including Unicode characters)
    with pytest.raises(ValueError, match=r"❌  Name cannot contain special characters or numbers.*"):
        update_product("SKU789", name="Gizmo C (2nd Gen)", price=11.49, quantity=80)

def test_remove_product():
    # Test removing a product from the catalog
    remove_product("SKU123")
    
    # Verify that the product was removed correctly
    assert "SKU123" not in product_catalog
    
    # Test attempting to remove a non-existent product
    with pytest.raises(KeyError, match=r"❌  SKU not found"):
        remove_product("SKU000")

def test_display_inventory():
    # Test displaying an empty inventory
    display_inventory()
    
    # Verify that the inventory is displayed correctly when it's not empty
    add_product("SKU987", "Another Widget", 15.99, 20)
    display_inventory()

    # Test displaying the initial inventory with some products
expected_output = (
    "\n📋 Current Inventory:\n"
    "-" * 60
    f"{'SKU':<10} {'Product Name':<20} {'Price':>8} {'Qty':>6}\n"
    "-" * 60
    f"{'SKU123':<10} {'Widget A':<20} ${19.99:>7.2f} {50:>6}\n"
    f"{'SKU456':<10} {'Gadget B':<20} ${34.95:>7.2f} {25:>6}\n"
    f"{'SKU789':<10} {'Gizmo C (2nd Gen)':<20} ${9.99:>7.2f} {100:>6}\n"
    "-" * 60
)  # <--- Corrected indentation here
# Use a regular expression to match the expected output with actual output
assert display_inventory() == expected_output