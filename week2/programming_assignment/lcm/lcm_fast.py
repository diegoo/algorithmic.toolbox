#!/usr/bin/python3

import sys, math

debug = False

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    if b == 0:
        return a
    remainder = a % b
    return gcd(b, remainder)

def lcm_fast(a, b):
    gcd_ab = gcd(a, b)
    if debug: print(gcd_ab)
    return math.floor((a * b) / gcd_ab)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())

    if debug:
        print(a, b)
        slow_solution = lcm_naive(a, b)
        fast_solution = lcm_fast(a, b)
        print("slow solution: %s" % slow_solution)
        print("fast solution: %s" % fast_solution)
        assert(slow_solution == fast_solution)
    else:
        print(lcm_fast(a, b))
