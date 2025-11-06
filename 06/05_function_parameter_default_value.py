def calculate_gross_price(price, vat_percent=27):
    return price * (1 + vat_percent / 100)

print(calculate_gross_price(2000)) 
print(calculate_gross_price(2000)) 
print(calculate_gross_price(2000, 5)) 

def add_item_to_basket(item, basket=None ):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item_to_basket("apple"))
print(add_item_to_basket("banana"))
print(add_item_to_basket("orange"))