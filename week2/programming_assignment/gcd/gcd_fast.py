#!/usr/bin/python3

import sys

debug = False

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    if b == 0:
        return a
    remainder = a % b
    if debug: print(a, b, remainder)
    
    return gcd_fast(b, remainder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    
    if debug:
        print(a, b)
        slow_solution = gcd_naive(a, b)
        fast_solution = gcd_fast(a, b)
        print("slow solution: %s" % slow_solution)
        print("fast solution: %s" % fast_solution)
        assert(slow_solution == fast_solution)

    print(gcd_fast(a, b))
