"""
Brute force algorithm to calculate the most efficient change.

author: Reis Gadsden
version: 19/01/2022
class: CS-5531 @ Appalachian State University
"""
import re
import numpy as np

STATIC_MAX_VAL = 0
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

    bruteForceChange(val, currency)



def bruteForceChange(val, currency):
    pass


def convertToChange(val, currency):
    # adds values up to max value
    counter = 1
    max_val = val
    max_converted = np.zeros(1, len(currency))
    while True:
        mod_val = max_val % (currency[-counter] + 1)
        max_val = max_val // (currency[-counter] + 1)
        max_converted[0][len(currency) - counter] = mod_val
        if max_val == 0 or max_val == -1:
            break
        counter += 1
        if counter > len(currency):
            counter = 1

    return tuple(map(tuple, max_converted))


def getMaxVal(currency):
    # calculates a max value for the given array
    max_val = 1
    count_up = []
    for i in currency:
        max_val *= (i + 1)
        count_up.append(0)
    max_val -= 1
    STATIC_MAX_VAL = max_val


if __name__ == "__main__":
    main()