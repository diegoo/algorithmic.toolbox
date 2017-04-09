#!/usr/bin/python3
import sys

DEBUG=True

def optimal_weight(W, w):
    result = 0
    return result


if __name__ == '__main__':

    if DEBUG:
        test_cases = [
            (10, 3, [1, 4, 8], 9),
        ]
        for (capacity, numer_of_bars, weights, expected_weight) in test_cases:
            result = optimal_weight(capacity, weights)
            print("result:", result)
            assert(result == expected_weight)
    
    else:
        input = sys.stdin.read()
        W, n, *w = list(map(int, input.split()))
        print(optimal_weight(W, w))
