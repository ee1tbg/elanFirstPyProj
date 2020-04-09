'''
Created on Dec 29, 2018

@author: Winterberger
'''
premium_cost = 125.
ground_flat = 20.
drone_flat = 0.

ground_U2 = 1.5
ground_U6 = 3.
ground_U10 = 4.
ground_Heavy = 4.75

drone_U2 = 4.5
drone_U6 = 9.
drone_U10 = 12.
drone_Heavy = 14.25


def main():
    #prompt for weight
    weight = float(input("Enter your package's weight in lbs: "))
    
    #initialize to premium
    cost = premium_cost
    
    drone_rate = drone_U2
    ground_rate = ground_U2
    
    #Check weight starting low
    if weight > 2.:
        drone_rate = drone_U6
        ground_rate = ground_U6
    if weight > 6.:
        drone_rate = drone_U10
        ground_rate = ground_U10
    if weight > 10:
        drone_rate = drone_Heavy
        ground_rate = ground_Heavy
        
    drone_cost = round(drone_flat + drone_rate * weight,2)
    ground_cost = round(ground_flat + ground_rate * weight,2)
    
    print("Ground: %0.2f \n Drone: %0.2f \n Premium: %0.2f" % (ground_cost, drone_cost, premium_cost))
    cost = min(premium_cost, drone_cost, ground_cost)
    if cost == drone_cost:
        method = 'drone'
    elif cost == ground_cost:
        method = 'ground'
    else:
        method = 'premium'
        
    method += " shipping."
    print("Best price is %0.2f by shipping via %s" % (cost, method))
    #return cost
    return cost

main()