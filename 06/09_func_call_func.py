def calculate_gross_price(price, vat_percent):
    return price * (1 + vat_percent / 100)

def apply_discount(price, discount_percent):
    return price * (1 - discount_percent / 100)

def calculate_final_price(price, vat_percent=27, discount_percent=0):
    discount_percent = price if discount_percent == 0 else apply_discount(price, discount_percent)
    return calculate_gross_price(discount_percent, vat_percent)

print(calculate_final_price(1000))  # No discount
print(calculate_final_price(1000, 5, 10))  # With discount
