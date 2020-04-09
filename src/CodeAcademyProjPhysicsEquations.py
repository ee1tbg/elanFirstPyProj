'''
Created on Nov 16, 2018

@author: Winterberger
'''
train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
    c_temp = 5/9 * (f_temp - 32)
    return c_temp
f100_in_celsius = f_to_c(100)
print (f100_in_celsius)

def c_to_f(c_temp):
    f_temp = c_temp * 9/5 + 32
    return f_temp
c0_in_fahrenheit = c_to_f(0)
print (c_to_f(c0_in_fahrenheit))
print (c_to_f(f100_in_celsius))
print (f_to_c(c0_in_fahrenheit))

def get_force(mass, acceleration):
    return mass*acceleration
train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies %f Newtons of force." % train_force)

def get_energy(mass,c=3*10**8):
    return mass*(c**2)
bomb_energy = get_energy(bomb_mass)
print ("A 1kg bomb supplies %f Joules." % bomb_energy)

def get_work(mass, acceleration, distance):
    force = get_force(mass,acceleration)
    return force*distance
train_work = get_work(train_mass,train_acceleration,train_distance)
print("The GE train does %f Joules of work over %f meters." % (train_work, train_distance))