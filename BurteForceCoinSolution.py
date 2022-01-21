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
    val = 0
    user_input = ""
    while True:
        user_input = input("Please enter the currency value: ")
        if re.fullmatch(NUM_PATTERN, user_input.strip()) is not None:
           val = int(user_input)
           break
        else:
            print("Invalid input! Try again.")

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
    print(bruteForceChange(val, currency))



def bruteForceChange(val, currency):
    max_val = getMaxVal(currency)
    smallest_number = np.inf
    best_change = None

    for i in range(0, max_val + 1):
        coins = convertToChange(i, currency)
        coin_value = getTotalValue(currency, coins)
        if coin_value == val:
            num_coins = 0
            for x in coins:
                num_coins += x
            if num_coins < smallest_number:
                smallest_number = num_coins
                best_change = coins

    return best_change




def convertToChange(val, currency):
    # adds values up to max value
    counter = len(currency) - 1
    max_val = val
    max_converted = []
    while True:
        mod_val = max_val % (currency[counter] + 1)
        max_val = max_val // (currency[counter] + 1)
        if len(max_converted) != len(currency):
            max_converted.insert(0, mod_val)
        if max_val == 0 or max_val == -1:
            break
        counter -= 1
        if counter == 0:
            counter = len(currency) - 1
    while len(max_converted) != len(currency):
        max_converted.insert(0, 0)

    return tuple(max_converted)


def getMaxVal(currency):
    # calculates a max value for the given array
    max_val = 1
    for i in currency:
        max_val *= (i + 1)
    return max_val - 1


def getTotalValue(currency, num_coins):
    counter = 0
    sum = 0

    for x in num_coins:
        sum += currency[counter] * x
        counter += 1
    return sum


if __name__ == "__main__":
    main()