from dataclasses import dataclass
from typing import Protocol


# Step 1: Define the State Interface
class CheckoutState(Protocol):
    def add_item(self, item): ...
    def review_cart(self): ...
    def enter_shipping_info(self, info): ...
    def process_payment(self): ...



# Step 3: Create the Context Class
class CheckoutContext(Protocol):
    checkout: list[str]

    def set_state(self, state: CheckoutState): ...
    def add_item(self, item): ...
    def review_cart(self): ...
    def enter_shipping_info(self, info): ...
    def process_payment(self): ...
    def show_items(self): ...


# Step 2: Create Concrete State Classes
@dataclass
class EmptyCartState:
    checkout: CheckoutContext
    
    def add_item(self, item):
        print("Item added to the cart.")
        self.checkout.items.append(item)
        return ItemAddedState(self.checkout)

    def review_cart(self):
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        print("Cannot process payment with an empty cart.")


@dataclass
class ItemAddedState:
    checkout: CheckoutContext
    
    def add_item(self, item):
        print("Item added to the cart.")

    def review_cart(self):
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


@dataclass
class CartReviewedState(CheckoutState):
    checkout: CheckoutContext
    
    def add_item(self, item):
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        print("Cart already reviewed.")

    def enter_shipping_info(self, info):
        print("Entering shipping information.")
        return ShippingInfoEnteredState(info)

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")

@dataclass
class ShippingInfoEnteredState(CheckoutState):
    checkout: CheckoutContext
    
    def add_item(self, item):
        print("Cannot add items after entering shipping info.")

    def review_cart(self):
        print("Cannot review cart after entering shipping info.")

    def enter_shipping_info(self, info):
        print("Shipping information already entered.")

    def process_payment(self):
        print("Processing payment with the entered shipping info.")





class Checkout:
    def __init__(self):
        self.current_state = EmptyCartState(self)
        self.items = []

    def set_state(self, state):
        self.current_state = state

    def add_item(self, item):
        self.current_state.add_item(item)

    def review_cart(self):
        self.current_state.review_cart()

    def enter_shipping_info(self, info):
        self.current_state.enter_shipping_info(info)

    def process_payment(self):
        self.current_state.process_payment()

    def show_items(self):
        print("Items in the cart:", self.items)




# Step 4: Example of Usage
if __name__ == "__main__":
    cart = Checkout()

    cart.add_item("Product 1")
    cart.review_cart()
    cart.enter_shipping_info("123 Main St, City")
    cart.process_payment()

    cart.show_items()