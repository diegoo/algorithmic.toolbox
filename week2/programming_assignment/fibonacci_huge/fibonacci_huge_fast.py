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
    for i in range(2,n):
        numbers[i] = numbers[i-1] + numbers[i-2]
    return numbers[n-1] % m    

# pisano period cycle begins with [0, 1]; keep adding until we find it
def pisano_period(n):
    if (n <= 1): return n
    numbers = []
    numbers.append(0)
    numbers.append(1)
    keep_adding = True
    i = 2
    while(keep_adding):
        numbers.append((numbers[i-1] + numbers[i-2]) % n)
        if numbers[i] == 1 and numbers[i-1] == 0:
            keep_adding = False
        else:
            i += 1
    return len(numbers[:i-1])

def fib_mod(n, m):
    p = pisano_period(m)
    remainder = n % p
    if debug: print("pisano", p, "remainder", remainder)
    return get_fibonacci_huge_fast(remainder, m)
    
if __name__ == '__main__':
    
    if debug:
        expected = [0,1,3,8,6,20,24,16,12,24,60,10,24]
        for i in range(0, 10):
            print(i, expected[i], pisano_period(i))
            assert(expected[i] == pisano_period(i))

        assert(fib_mod(1, 239) == 1)
        assert(fib_mod(239, 1000) == 161)
        assert(fib_mod(2816213588, 30524) == 10249)
        assert(fib_mod(100, 100000) == get_fibonacci_huge_naive(100, 100000))

    else:
        input = sys.stdin.read();
        n, m = map(int, input.split())
        print(fib_mod(n, m))
