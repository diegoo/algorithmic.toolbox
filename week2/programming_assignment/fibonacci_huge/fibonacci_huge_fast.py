#!/usr/bin/python3

import sys

debug = False

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m

def get_fibonacci_huge_fast(n, m):
    if (n <= 1):
        return n
    numbers = [0] * n
    numbers[0] = 1
    numbers[1] = 1
    # if debug: print("init", numbers)
    for i in range(2,n):
        numbers[i] = numbers[i-1] + numbers[i-2]
    # if debug: print("filled", numbers)
    return numbers[n-1] % m    

def pisano_period(n):
    c=[1,1]
    a=[]
    while (c in a) < 1 % n:
        a += [c]
        c = [c[1], sum(c) % n]
    return len(a) or 1

# calculate the remainder of N % sizeOfPisanoPeriod. The remainder will be the index of the PISANO[remainder] array.

def fib_mod(n, m):
    p = pisano_period(m)
    remainder = n % p
    if debug: print("pisano", p, "remainder", remainder)
    return get_fibonacci_huge_fast(remainder, m)
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())

    # --------------------------------------------------------------------------------

    if debug:
        print("pisano")
        for i in range(1, 10):
            print(pisano_period(i)),
        print

        assert(fib_mod(1, 239) == 1)
        assert(fib_mod(239, 1000) == 161)
        assert(fib_mod(2816213588, 30524) == 10249)

        slow_solution = get_fibonacci_huge_naive(n, m)
        fast_solution = fib_mod(n, m)
        print("slow solution: %s" % slow_solution)
        print("fast solution: %s" % fast_solution)
        assert(slow_solution == fast_solution)

    else:
        print(fib_mod(n, m))

