net_prices = [100, 200, 300, 400, 500]
#gross_prices = []

#for i in net_prices:
#    gross_prices.append(i * 1.27)
#    print(gross_prices)

gross_prices = [i * 1.27 for i in net_prices]
print(gross_prices)