#!/usr/bin/python3
import sys

debug = False

denominations = [10, 5, 1]

def solve(n_coins, amount):
    if amount == 0:
        return n_coins
    for denomination in denominations:
        if amount - denomination >= 0:
            amount -= denomination
            n_coins += 1
            if debug: print("denomination", denomination, "n_coins", n_coins, "amount", amount)
            break
    return solve(n_coins, amount)

def get_change(m):
    return solve(n_coins=0, amount=m)

if __name__ == '__main__':

    if debug:
        for (amount, expected) in [(2, 2), (28, 6), (40, 4), (16, 3), (17, 4)]:
            print("calculating change for amount", amount)
            result = get_change(amount)
            print("coins: %d" % expected, "got: %d" % result)
            print("-"*80)
            assert(expected == result)
    else:
        m = int(sys.stdin.read())
        print(get_change(m))
