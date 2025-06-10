# messy code..
def a(x):
    if x > 10:
        return x * 1.5
    else:
        return x + 2




# clean code..
def calculate_discounted_price(price):
    """
    Apply a discount if price is above 10.
    """
    if price > 10:
        return price * 1.5
    return price + 2

