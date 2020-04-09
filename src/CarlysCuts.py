'''
Created on Jan 5, 2019

@author: Winterberger
'''
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
new_prices = [i-5 for i in prices]

total_price = 0
for i in new_prices:
    total_price += i
    #print(total_price)
average_price = total_price / len(prices)
print("Average Haircut Price:\n%0.2f \n" % average_price)

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
    #print(total_revenue)
print("Total Revenue: %0.2f" % total_revenue)
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue: %0.2f" % average_daily_revenue)

cuts_under_30 = [i for i in new_prices if i < 30]
print(cuts_under_30)
