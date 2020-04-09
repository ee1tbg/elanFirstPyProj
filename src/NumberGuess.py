'''
Created on Nov 10, 2018

@author: Winterberger

1. Roll a pair of dice
2. Add the values
3. Ask for a guess
4. Compare guess to value
5. Determine winner
'''
import random
from time import sleep

def roll_result(num_sides):
    print ("rolling..")
    sleep(1)
    
    return random.randint(1,num_sides)

def compare_results(guess, actual, attempt):
    if int(guess) == int(actual):
        print ("You win!!")
        return True
    elif attempt > 1:
        print ("I win!! (Took you more than 1 try)")
        return True
    else:
        print ("Let me help you narrow it down..")
        return False

def try_2(guess, actual):
    if guess > actual:
        print("Guess lower.")
    else:
        print("Guess higher.")
    return input("New guess: ")

    
def main():
    i = 0
    result = False
    num_sides = int(input("How many sides do you want the dice to have? \n Sides: "))
    roll_1 = roll_result(num_sides)
    roll_2 = roll_result(num_sides)
    roll_sum = int(roll_1 + roll_2)
    
    human_guess = int(input("Guess the number from 2 rolled dice (2.." + str(2 * num_sides) + "): "))
    
    while (False == result):
        
        result = compare_results(human_guess, roll_sum, i)
        if False == result:
            human_guess = int((try_2(human_guess, roll_sum)))
        i += 1
    
    print ("You got it in " + str(i) + " tries.")

        
main()