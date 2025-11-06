price = 1000
vat_percent = 27
gorss_price = 0

def calculate_gross_price():
    gross_price = price + (price * vat_percent / 100)

calculate_gross_price()

