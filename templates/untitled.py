profit=0
if len(list_prices)<2:
	return 0
buy_price = list_prices[0]
for value in list_prices:
	sell_price=value
	if value<buy_price:
		buy_price=value
	if sell_price-buy_price>profit:
		profit=sell_price-buy_price
return profit



