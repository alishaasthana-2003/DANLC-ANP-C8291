#Custom Exceptions for Business Logic
#- Create custom exception classes `OutOfStockError` and `InvalidOrderError`. Write a function `process_order` that takes an order (a dictionary with item names and quantities) and a stock (a dictionary with item names and available quantities) as arguments. Use exception handling to manage:
#- Out of stock items (raise `OutOfStockError` with a suitable message).
#- Invalid order quantities (e.g., negative or zero, raise `InvalidOrderError` with a suitable message).
#- Test the function with various orders and stock scenarios.

class OutOfStockError(Exception):
   def __init__(self, item):
        self.message = f"Item '{item}' is out of stock."
        super().__init__(self.message)
class InvalidOrderError(Exception):
    def __init__(self, item, quantity):
        self.message = f"Invalid quantity '{quantity}' for item '{item}'. Quantity must be positive."
        super().__init__(self.message)


def test_process_order():
    stock = {
        'apple': 10,
        'banana': 5,
        'orange': 0,
    }


    orders = [
        {'apple': 5, 'banana': 2},  # Valid order
        {'apple': 0, 'banana': 2},  # Invalid order quantity (zero)
        {'apple': -1, 'banana': 2},  # Invalid order quantity (negative)
        {'apple': 5, 'banana': 6},  # Out of stock (not enough bananas)
        {'orange': 1},  # Out of stock (oranges are zero)
        {'grape': 1},  # Out of stock (item not in stock)
    ]

    for i, order in enumerate(orders):
        print(f"Test case {i + 1}: Order = {order}")
        try:
            updated_stock = test_process_order(order, stock.copy())
            print("Order processed successfully.")
            print("Updated stock:", updated_stock)
        except (OutOfStockError, InvalidOrderError) as e:
            print(e)
        print()


test_process_order()

