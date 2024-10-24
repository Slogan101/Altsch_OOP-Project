import math
import datetime as dt

class Product ():
    def __init__(self, name: str, price: float, stock: int, weight: float) -> None:
        self.name = name
        self.price = price
        self.stock = stock
        self.weight = weight


    def get_info(self):
        return f"Product Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, weight: {self.weight}kg"
    
    def apply_discount(self, discount_percentage):
        percent = discount_percentage / 100
        discount_value = percent * self.price
        new_price = math.ceil(self.price - discount_value)
        self.price = new_price
        return f"${self.price}"
    
    def check_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return f"Order {quantity} units of {self.name}: Successful, stock Left: {self.stock}."
        else:
            return f"{self.name} is out of stock."
        
    def calculate_shipping_cost(self):
        ship_cost = math.ceil(self.weight * 10)
        return f"Shipping cost for {self.name}: ${ship_cost}"
    

class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, stock: int, weight: float, warranty_years: int, brand: str) -> None:
        super().__init__(name, price, stock, weight)
        self.warranty_years = warranty_years
        self.brand = brand

    def get_info(self):
        return f"Electronic Product: {self.name}, Brand: {self.brand} Price: ${self.price}, Warranty: {self.warranty_years} years, Stock: {self.stock}, weight: {self.weight}kg"
        
    def calculate_warranty_extension(self, extra_years: int):
        new_warranty = self.warranty_years + extra_years
        return f"Extended warranty for {self.name}: {new_warranty} years."
    
class GroceryProduct(Product):
    def __init__(self, name: str, price: float, stock: int, weight: float, expiration_date: str, is_perishable: bool) -> None:
        super().__init__(name, price, stock, weight)
        self.expiration_date = expiration_date
        self.is_perishable = is_perishable

    def get_info(self):
        return f"Grocery Product: {self.name}, Price: ${self.price}, Expiration Date: {self.expiration_date}, Stock: {self.stock}, weight: {self.weight}kg, Perishable: {self.is_perishable}"
    
    def check_if_expired(self, current_date):
        if self.expiration_date > current_date:
            return f"{self.name} Not expired"
        else:
            return f"{self.name} expired"

        