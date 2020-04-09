'''
Created on Jun 15, 2019

@author: Winterberger
'''
from nile import get_distance, format_price, SHIPPING_PRICES
from Test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type = 'Overnight'):
    (from_lat, from_lon) = from_coords
    (to_lat, to_lon) = to_coords
    
    # Distance
    distance = get_distance(from_lat, from_lon, to_lat, to_lon)
    
    # Rate
    shipping_rate = SHIPPING_PRICES[shipping_type]
    
    # Price = Distance * Rate
    price = distance * shipping_rate
    #print("Ship {d:0.1f} miles at rate of ${r:0.1f} per mile is ${p:0.2f}".format(d=distance, r=shipping_rate, p=price))
    return format_price(price)

# Test the function by calling
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    
    for driver in drivers:
        driver_time = driver.speed * distance
        #print("Driver_time: {}".format(driver_time))
        price_for_driver = driver_time * driver.salary
        #print("Driver_price: {}".format(price_for_driver))
        cheapest_driver = driver if (cheapest_driver is None or price_for_driver < cheapest_driver_price) else cheapest_driver
        #print("Cheapest_Driver: {}".format(cheapest_driver))
        cheapest_driver_price = price_for_driver if (cheapest_driver_price is None or price_for_driver < cheapest_driver_price) else cheapest_driver_price
        #print("Cheapest_Price: {}".format(cheapest_driver_price))
    return cheapest_driver_price, cheapest_driver
    
# Test the function by calling 
test_function(calculate_driver_cost)

# Define calculate_money_made() here
def calculate_money_made(**trips):
    total_money_made = 0.
    for trip_key, trip in trips.items():
        print("{} Trip nets ${}.".format(trip_key, trip.cost - trip.driver.cost))
        trip_revenue = trip.cost - trip.driver.cost
        total_money_made += trip_revenue
    return total_money_made

# Test the function by calling 
test_function(calculate_money_made)