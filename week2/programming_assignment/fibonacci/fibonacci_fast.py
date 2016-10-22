#!/usr/bin/python3

debug = False

def calc_fib(n):
    if (n <= 1):
        return n

    n_minus_1 = calc_fib(n - 1)
    n_minus_2 = calc_fib(n - 2)
    if debug: print(n, n_minus_1, n_minus_2)

    return n_minus_1 + n_minus_2

def fast_calc_fib(n):
    if (n <= 1):
        return n

    numbers = [0] * n
    numbers[0] = 1
    numbers[1] = 1
    if debug: print("init", numbers)
    
    for i in range(2,n):
        numbers[i] = numbers[i-1] + numbers[i-2]
    if debug: print("filled", numbers)
    return numbers[n-1]

n = int(input())

if debug: 
    slow_solution = calc_fib(n)
    fast_solution = fast_calc_fib(n)
    print("slow solution: %s" % slow_solution)
    print("fast solution: %s" % fast_solution)
    assert(slow_solution == fast_solution)

print(fast_calc_fib(n))
