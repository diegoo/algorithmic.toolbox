#!/usr/bin/python3
import sys

DEBUG=False

def print_matrix(m):
    for h in range(len(m)):
        print(m[h])
        
def get_matrix(height, width):
    D = [[0 for x in range(width+1)] for y in range(height+1)]
    return D

def optimal_weight(W, w):
    result = 0

    D = get_matrix(len(w), W)
    if DEBUG:
        print("-"*40, W, w, "-"*40)
        print_matrix(D)

    for i in range(len(w)+1):
      for j in range(W+1):
        if i == 0 or j == 0:
          D[i][j] = 0
        elif w[i-1] > j:
          D[i][j] = D[i-1][j]
        else:
          D[i][j] = max([w[i-1] + D[i-1][j-w[i-1]], D[i-1][j]])
    result = D[len(w)][W]
    if DEBUG: print_matrix(D)
    
    return result


if __name__ == '__main__':

    if DEBUG:
        test_cases = [
            (10, 3, [1, 4, 8], 9),
            (10, 3, [3, 4, 5], 7),
            (10, 4, [6, 3, 4, 2], 10),
        ]
        for (capacity, number_of_bars, weights, expected_weight) in test_cases:
            result = optimal_weight(capacity, weights)
            print("result:", result)
            assert(result == expected_weight)
    
    else:
        input = sys.stdin.read()
        W, n, *w = list(map(int, input.split()))
        print(optimal_weight(W, w))
