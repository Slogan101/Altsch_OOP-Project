from product import Product, ElectronicProduct, GroceryProduct



lap = ElectronicProduct("Laptop", 1500, 10, 2.5, 3, "Dell")
# detailed product information 
print(lap.get_info())
print(lap.apply_discount(15))
print(lap.get_info())
print(lap.check_stock(5))
print(lap.calculate_shipping_cost())
print(lap.calculate_warranty_extension(2))
print("\n")
Milik = GroceryProduct("Milk", 4, 50, 1, "2024-11-15", True)
print(Milik.check_stock(5))
print(Milik.calculate_shipping_cost())
print(Milik.check_if_expired("2024-10-01"))