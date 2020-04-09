'''
random number from list of random numbers
'''
# Import random below:
import random
import numbers

# Create random_list below:
random_list = [random.randint(1,100) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print (randomer_number)

'''
Plot 12 random numbers
'''
from matplotlib import pyplot as plt
import random

# Add your code below:
numbers_a = range(1,13)
numbers_b = random.sample(range(1000),12)

plt.plot(numbers_a,numbers_b)
plt.show()

'''

'''
