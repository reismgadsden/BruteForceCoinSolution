"""
Brute force algorithm to calculate the most efficient change.

author: Reis Gadsden
version: 19/01/2022
class: CS-5531 @ Appalachian State University
"""
import re
import numpy as np

NUM_PATTERN = re.compile("^[0-9]*$")

def main():
    #get and validate user input for desired value
    val = 0
    user_input = ""
    while True:
        user_input = input("Please enter the currency value: ")
        if re.fullmatch(NUM_PATTERN, user_input.strip()) is not None: # regex to make sure its a number
           val = int(user_input)
           break
        else:
            print("Invalid input! Try again.")

    # get, validate, and order user input for denominations
    currency = []
    print("Please enter the denominations of your coins. Enter 'q' when finished.")
    while True:
        user_input = input("Please enter the denomination value: ").strip()
        if re.fullmatch(NUM_PATTERN, user_input) is not None:
            user_input_converted = int(user_input)
            if len(currency) != 0:
                counter = 0
                for i in currency:
                    if user_input_converted > i:
                        currency.insert(counter, user_input_converted)
                        break
                    if user_input_converted == i:
                        print("Denomination was already entered.")
                    counter += 1
                if counter == len(currency):
                    currency.append(user_input_converted)
            else:
                currency.append(user_input_converted)
        elif user_input == 'q' or user_input == 'Q':
            break
        else:
            print("Invalid input! Try again.")

    # open results.txt and append output with it
    f = open("results.txt", "a")
    f.write("Desired Value: " + str(val) + "; Denominations: " + str(currency) + "; Best possible change: " + str(bruteForceChange(val, currency)) + "\n")
    f.close()


# runs through all possible configurations and returns the configurations with the least coins that matches the value
def bruteForceChange(val, currency):
    max_val = getMaxVal(currency)
    smallest_number = np.inf
    best_change = None

    for i in range(0, max_val + 1):
        # gets the coins that match a corresponding configuration and calculates the actual coin value of such a
        # configuration
        coins = convertToChange(i, currency)
        coin_value = getTotalValue(currency, coins)

        if coin_value == val:
            num_coins = 0
            # finds the smallest amount of coins by comparing to a previous smallest number
            for x in coins:
                num_coins += x
            if num_coins < smallest_number:
                smallest_number = num_coins
                best_change = coins

    return best_change



# converts a specific value (configuration #) to the corresponding configuration
def convertToChange(val, currency):
    counter = 1
    max_val = val
    max_converted = []
    while True:
        # converts a given value to a configuration relating to the given denominations
        mod_val = max_val % (currency[-counter] + 1)
        max_val = max_val // (currency[-counter] + 1)
        max_converted.insert(0, mod_val)
        if max_val == 0 or max_val == -1:
            break
        counter += 1
        if counter > len(currency):
            counter = 1

    # for values less then (1, ..., 0)
    # fills in the leading digits with 0
    while len(max_converted) != len(currency):
        max_converted.insert(0, 0)

    return tuple(max_converted)


#gets the maximum value (max configuration #) of a given denomination set
def getMaxVal(currency):
    # calculates a max value for the given array
    max_val = 1
    for i in currency:
        max_val *= (i + 1)
    return max_val - 1


#calculates the total value of a configuration
def getTotalValue(currency, num_coins):
    counter = 0
    sum = 0

    for x in num_coins:
        sum += currency[counter] * x
        counter += 1
    return sum


# executes the main method if the file is not being imported elsewhere
if __name__ == "__main__":
    main()