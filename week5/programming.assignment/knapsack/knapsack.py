#!/usr/bin/python3
import sys

DEBUG=True # False

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

    for i in range(len(w)+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                D[i][j] = 0
            elif w[i-1] > j:
                if DEBUG: print("case 1 (w[%d] > %d): i" % (i-1, j), i, "j", j, "w[%d]" % (i-1), w[i-1], "D[%d][%d]" % (i-1, j), D[i-1][j], " => D[%d][%d] = D[%d][%d]" % (i, j, i-1, j))
                D[i][j] = D[i-1][j]
                if DEBUG: print_matrix(D)
            else:
                m = max([w[i-1] + D[i-1][j-w[i-1]], D[i-1][j]])
                if DEBUG: print("case 2 (w[%d] <= %d): i" % (i-1, j), i, "j", j, "w[%d]" % (i-1), w[i-1], "D[%d][%d]" % (i-1, j-w[i-1]), D[i-1][j-w[i-1]], "D[%d][%d]" % (i-1, j), D[i-1][j], 
                                "max([w[%d] + D[%d][%d], D[%d][%d]]" % (i-1, i-1, j-w[i-1], i-1, j), m, " => D[%d][%d] = %d" % (i, j, m))
                D[i][j] = m
                if DEBUG: print_matrix(D)
    result = D[len(w)][W]
    if DEBUG: print("\n"); print_matrix(D)
    
    return result


if __name__ == '__main__':

    if DEBUG:
        test_cases = [
            (4, 2, [3, 2], 3),
            (10, 3, [1, 4, 8], 9),
            (10, 3, [3, 4, 5], 9),
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

## examples:

# ---------------------------------------- 4 [3, 2] ----------------------------------------
# case 1 (w[0] > 1): i 1 j 1 w[0] 3 D[0][1] 0  => D[1][1] = D[0][1]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# case 1 (w[0] > 2): i 1 j 2 w[0] 3 D[0][2] 0  => D[1][2] = D[0][2]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0]
# case 2 (w[0] <= 3): i 1 j 3 w[0] 3 D[0][0] 0 D[0][3] 0 max([w[0] + D[0][0], D[0][3]] 3  => D[1][3] = 3
# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 0]
# [0, 0, 0, 0, 0]
# case 2 (w[0] <= 4): i 1 j 4 w[0] 3 D[0][1] 0 D[0][4] 0 max([w[0] + D[0][1], D[0][4]] 3  => D[1][4] = 3
# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3]
# [0, 0, 0, 0, 0]
# case 1 (w[1] > 1): i 2 j 1 w[1] 2 D[1][1] 0  => D[2][1] = D[1][1]
# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3]
# [0, 0, 0, 0, 0]
# case 2 (w[1] <= 2): i 2 j 2 w[1] 2 D[1][0] 0 D[1][2] 0 max([w[1] + D[1][0], D[1][2]] 2  => D[2][2] = 2
# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3]
# [0, 0, 2, 0, 0]
# case 2 (w[1] <= 3): i 2 j 3 w[1] 2 D[1][1] 0 D[1][3] 3 max([w[1] + D[1][1], D[1][3]] 3  => D[2][3] = 3
# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3]
# [0, 0, 2, 3, 0]
# case 2 (w[1] <= 4): i 2 j 4 w[1] 2 D[1][2] 0 D[1][4] 3 max([w[1] + D[1][2], D[1][4]] 3  => D[2][4] = 3
# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3]
# [0, 0, 2, 3, 3]


# [0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3]
# [0, 0, 2, 3, 3]
# result: 3
# ---------------------------------------- 10 [1, 4, 8] ----------------------------------------
# case 2 (w[0] <= 1): i 1 j 1 w[0] 1 D[0][0] 0 D[0][1] 0 max([w[0] + D[0][0], D[0][1]] 1  => D[1][1] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 2): i 1 j 2 w[0] 1 D[0][1] 0 D[0][2] 0 max([w[0] + D[0][1], D[0][2]] 1  => D[1][2] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 3): i 1 j 3 w[0] 1 D[0][2] 0 D[0][3] 0 max([w[0] + D[0][2], D[0][3]] 1  => D[1][3] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 4): i 1 j 4 w[0] 1 D[0][3] 0 D[0][4] 0 max([w[0] + D[0][3], D[0][4]] 1  => D[1][4] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 5): i 1 j 5 w[0] 1 D[0][4] 0 D[0][5] 0 max([w[0] + D[0][4], D[0][5]] 1  => D[1][5] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 6): i 1 j 6 w[0] 1 D[0][5] 0 D[0][6] 0 max([w[0] + D[0][5], D[0][6]] 1  => D[1][6] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 7): i 1 j 7 w[0] 1 D[0][6] 0 D[0][7] 0 max([w[0] + D[0][6], D[0][7]] 1  => D[1][7] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 8): i 1 j 8 w[0] 1 D[0][7] 0 D[0][8] 0 max([w[0] + D[0][7], D[0][8]] 1  => D[1][8] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 9): i 1 j 9 w[0] 1 D[0][8] 0 D[0][9] 0 max([w[0] + D[0][8], D[0][9]] 1  => D[1][9] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 10): i 1 j 10 w[0] 1 D[0][9] 0 D[0][10] 0 max([w[0] + D[0][9], D[0][10]] 1  => D[1][10] = 1
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 1): i 2 j 1 w[1] 4 D[1][1] 1  => D[2][1] = D[1][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 2): i 2 j 2 w[1] 4 D[1][2] 1  => D[2][2] = D[1][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 3): i 2 j 3 w[1] 4 D[1][3] 1  => D[2][3] = D[1][3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 4): i 2 j 4 w[1] 4 D[1][0] 0 D[1][4] 1 max([w[1] + D[1][0], D[1][4]] 4  => D[2][4] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 5): i 2 j 5 w[1] 4 D[1][1] 1 D[1][5] 1 max([w[1] + D[1][1], D[1][5]] 5  => D[2][5] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 6): i 2 j 6 w[1] 4 D[1][2] 1 D[1][6] 1 max([w[1] + D[1][2], D[1][6]] 5  => D[2][6] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 7): i 2 j 7 w[1] 4 D[1][3] 1 D[1][7] 1 max([w[1] + D[1][3], D[1][7]] 5  => D[2][7] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 8): i 2 j 8 w[1] 4 D[1][4] 1 D[1][8] 1 max([w[1] + D[1][4], D[1][8]] 5  => D[2][8] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 9): i 2 j 9 w[1] 4 D[1][5] 1 D[1][9] 1 max([w[1] + D[1][5], D[1][9]] 5  => D[2][9] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 10): i 2 j 10 w[1] 4 D[1][6] 1 D[1][10] 1 max([w[1] + D[1][6], D[1][10]] 5  => D[2][10] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 1): i 3 j 1 w[2] 8 D[2][1] 1  => D[3][1] = D[2][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 2): i 3 j 2 w[2] 8 D[2][2] 1  => D[3][2] = D[2][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 3): i 3 j 3 w[2] 8 D[2][3] 1  => D[3][3] = D[2][3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 4): i 3 j 4 w[2] 8 D[2][4] 4  => D[3][4] = D[2][4]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 5): i 3 j 5 w[2] 8 D[2][5] 5  => D[3][5] = D[2][5]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 0, 0, 0, 0, 0]
# case 1 (w[2] > 6): i 3 j 6 w[2] 8 D[2][6] 5  => D[3][6] = D[2][6]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 5, 0, 0, 0, 0]
# case 1 (w[2] > 7): i 3 j 7 w[2] 8 D[2][7] 5  => D[3][7] = D[2][7]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 5, 5, 0, 0, 0]
# case 2 (w[2] <= 8): i 3 j 8 w[2] 8 D[2][0] 0 D[2][8] 5 max([w[2] + D[2][0], D[2][8]] 8  => D[3][8] = 8
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 5, 5, 8, 0, 0]
# case 2 (w[2] <= 9): i 3 j 9 w[2] 8 D[2][1] 1 D[2][9] 5 max([w[2] + D[2][1], D[2][9]] 9  => D[3][9] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 0]
# case 2 (w[2] <= 10): i 3 j 10 w[2] 8 D[2][2] 1 D[2][10] 5 max([w[2] + D[2][2], D[2][10]] 9  => D[3][10] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 9]


# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# [0, 1, 1, 1, 4, 5, 5, 5, 5, 5, 5]
# [0, 1, 1, 1, 4, 5, 5, 5, 8, 9, 9]
# result: 9
# ---------------------------------------- 10 [3, 4, 5] ----------------------------------------
# case 1 (w[0] > 1): i 1 j 1 w[0] 3 D[0][1] 0  => D[1][1] = D[0][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[0] > 2): i 1 j 2 w[0] 3 D[0][2] 0  => D[1][2] = D[0][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 3): i 1 j 3 w[0] 3 D[0][0] 0 D[0][3] 0 max([w[0] + D[0][0], D[0][3]] 3  => D[1][3] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 4): i 1 j 4 w[0] 3 D[0][1] 0 D[0][4] 0 max([w[0] + D[0][1], D[0][4]] 3  => D[1][4] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 5): i 1 j 5 w[0] 3 D[0][2] 0 D[0][5] 0 max([w[0] + D[0][2], D[0][5]] 3  => D[1][5] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 6): i 1 j 6 w[0] 3 D[0][3] 0 D[0][6] 0 max([w[0] + D[0][3], D[0][6]] 3  => D[1][6] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 7): i 1 j 7 w[0] 3 D[0][4] 0 D[0][7] 0 max([w[0] + D[0][4], D[0][7]] 3  => D[1][7] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 8): i 1 j 8 w[0] 3 D[0][5] 0 D[0][8] 0 max([w[0] + D[0][5], D[0][8]] 3  => D[1][8] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 9): i 1 j 9 w[0] 3 D[0][6] 0 D[0][9] 0 max([w[0] + D[0][6], D[0][9]] 3  => D[1][9] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 10): i 1 j 10 w[0] 3 D[0][7] 0 D[0][10] 0 max([w[0] + D[0][7], D[0][10]] 3  => D[1][10] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 1): i 2 j 1 w[1] 4 D[1][1] 0  => D[2][1] = D[1][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 2): i 2 j 2 w[1] 4 D[1][2] 0  => D[2][2] = D[1][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 3): i 2 j 3 w[1] 4 D[1][3] 3  => D[2][3] = D[1][3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 4): i 2 j 4 w[1] 4 D[1][0] 0 D[1][4] 3 max([w[1] + D[1][0], D[1][4]] 4  => D[2][4] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 5): i 2 j 5 w[1] 4 D[1][1] 0 D[1][5] 3 max([w[1] + D[1][1], D[1][5]] 4  => D[2][5] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 6): i 2 j 6 w[1] 4 D[1][2] 0 D[1][6] 3 max([w[1] + D[1][2], D[1][6]] 4  => D[2][6] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 7): i 2 j 7 w[1] 4 D[1][3] 3 D[1][7] 3 max([w[1] + D[1][3], D[1][7]] 7  => D[2][7] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 8): i 2 j 8 w[1] 4 D[1][4] 3 D[1][8] 3 max([w[1] + D[1][4], D[1][8]] 7  => D[2][8] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 9): i 2 j 9 w[1] 4 D[1][5] 3 D[1][9] 3 max([w[1] + D[1][5], D[1][9]] 7  => D[2][9] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 10): i 2 j 10 w[1] 4 D[1][6] 3 D[1][10] 3 max([w[1] + D[1][6], D[1][10]] 7  => D[2][10] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 1): i 3 j 1 w[2] 5 D[2][1] 0  => D[3][1] = D[2][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 2): i 3 j 2 w[2] 5 D[2][2] 0  => D[3][2] = D[2][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 3): i 3 j 3 w[2] 5 D[2][3] 3  => D[3][3] = D[2][3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 4): i 3 j 4 w[2] 5 D[2][4] 4  => D[3][4] = D[2][4]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 5): i 3 j 5 w[2] 5 D[2][0] 0 D[2][5] 4 max([w[2] + D[2][0], D[2][5]] 5  => D[3][5] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 6): i 3 j 6 w[2] 5 D[2][1] 0 D[2][6] 4 max([w[2] + D[2][1], D[2][6]] 5  => D[3][6] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 5, 0, 0, 0, 0]
# case 2 (w[2] <= 7): i 3 j 7 w[2] 5 D[2][2] 0 D[2][7] 7 max([w[2] + D[2][2], D[2][7]] 7  => D[3][7] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 5, 7, 0, 0, 0]
# case 2 (w[2] <= 8): i 3 j 8 w[2] 5 D[2][3] 3 D[2][8] 7 max([w[2] + D[2][3], D[2][8]] 8  => D[3][8] = 8
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 5, 7, 8, 0, 0]
# case 2 (w[2] <= 9): i 3 j 9 w[2] 5 D[2][4] 4 D[2][9] 7 max([w[2] + D[2][4], D[2][9]] 9  => D[3][9] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 5, 7, 8, 9, 0]
# case 2 (w[2] <= 10): i 3 j 10 w[2] 5 D[2][5] 4 D[2][10] 7 max([w[2] + D[2][5], D[2][10]] 9  => D[3][10] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 5, 7, 8, 9, 9]


# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
# [0, 0, 0, 3, 4, 4, 4, 7, 7, 7, 7]
# [0, 0, 0, 3, 4, 5, 5, 7, 8, 9, 9]
# result: 9
# ---------------------------------------- 10 [6, 3, 4, 2] ----------------------------------------
# case 1 (w[0] > 1): i 1 j 1 w[0] 6 D[0][1] 0  => D[1][1] = D[0][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[0] > 2): i 1 j 2 w[0] 6 D[0][2] 0  => D[1][2] = D[0][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[0] > 3): i 1 j 3 w[0] 6 D[0][3] 0  => D[1][3] = D[0][3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[0] > 4): i 1 j 4 w[0] 6 D[0][4] 0  => D[1][4] = D[0][4]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[0] > 5): i 1 j 5 w[0] 6 D[0][5] 0  => D[1][5] = D[0][5]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 6): i 1 j 6 w[0] 6 D[0][0] 0 D[0][6] 0 max([w[0] + D[0][0], D[0][6]] 6  => D[1][6] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 7): i 1 j 7 w[0] 6 D[0][1] 0 D[0][7] 0 max([w[0] + D[0][1], D[0][7]] 6  => D[1][7] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 8): i 1 j 8 w[0] 6 D[0][2] 0 D[0][8] 0 max([w[0] + D[0][2], D[0][8]] 6  => D[1][8] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 9): i 1 j 9 w[0] 6 D[0][3] 0 D[0][9] 0 max([w[0] + D[0][3], D[0][9]] 6  => D[1][9] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[0] <= 10): i 1 j 10 w[0] 6 D[0][4] 0 D[0][10] 0 max([w[0] + D[0][4], D[0][10]] 6  => D[1][10] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 1): i 2 j 1 w[1] 3 D[1][1] 0  => D[2][1] = D[1][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[1] > 2): i 2 j 2 w[1] 3 D[1][2] 0  => D[2][2] = D[1][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 3): i 2 j 3 w[1] 3 D[1][0] 0 D[1][3] 0 max([w[1] + D[1][0], D[1][3]] 3  => D[2][3] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 4): i 2 j 4 w[1] 3 D[1][1] 0 D[1][4] 0 max([w[1] + D[1][1], D[1][4]] 3  => D[2][4] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 5): i 2 j 5 w[1] 3 D[1][2] 0 D[1][5] 0 max([w[1] + D[1][2], D[1][5]] 3  => D[2][5] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 6): i 2 j 6 w[1] 3 D[1][3] 0 D[1][6] 6 max([w[1] + D[1][3], D[1][6]] 6  => D[2][6] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 7): i 2 j 7 w[1] 3 D[1][4] 0 D[1][7] 6 max([w[1] + D[1][4], D[1][7]] 6  => D[2][7] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 8): i 2 j 8 w[1] 3 D[1][5] 0 D[1][8] 6 max([w[1] + D[1][5], D[1][8]] 6  => D[2][8] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 9): i 2 j 9 w[1] 3 D[1][6] 6 D[1][9] 6 max([w[1] + D[1][6], D[1][9]] 9  => D[2][9] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[1] <= 10): i 2 j 10 w[1] 3 D[1][7] 6 D[1][10] 6 max([w[1] + D[1][7], D[1][10]] 9  => D[2][10] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 1): i 3 j 1 w[2] 4 D[2][1] 0  => D[3][1] = D[2][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 2): i 3 j 2 w[2] 4 D[2][2] 0  => D[3][2] = D[2][2]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[2] > 3): i 3 j 3 w[2] 4 D[2][3] 3  => D[3][3] = D[2][3]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 4): i 3 j 4 w[2] 4 D[2][0] 0 D[2][4] 3 max([w[2] + D[2][0], D[2][4]] 4  => D[3][4] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 5): i 3 j 5 w[2] 4 D[2][1] 0 D[2][5] 3 max([w[2] + D[2][1], D[2][5]] 4  => D[3][5] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 6): i 3 j 6 w[2] 4 D[2][2] 0 D[2][6] 6 max([w[2] + D[2][2], D[2][6]] 6  => D[3][6] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 7): i 3 j 7 w[2] 4 D[2][3] 3 D[2][7] 6 max([w[2] + D[2][3], D[2][7]] 7  => D[3][7] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 8): i 3 j 8 w[2] 4 D[2][4] 3 D[2][8] 6 max([w[2] + D[2][4], D[2][8]] 7  => D[3][8] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 9): i 3 j 9 w[2] 4 D[2][5] 3 D[2][9] 9 max([w[2] + D[2][5], D[2][9]] 9  => D[3][9] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 0]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[2] <= 10): i 3 j 10 w[2] 4 D[2][6] 6 D[2][10] 9 max([w[2] + D[2][6], D[2][10]] 10  => D[3][10] = 10
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 1 (w[3] > 1): i 4 j 1 w[3] 2 D[3][1] 0  => D[4][1] = D[3][1]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[3] <= 2): i 4 j 2 w[3] 2 D[3][0] 0 D[3][2] 0 max([w[3] + D[3][0], D[3][2]] 2  => D[4][2] = 2
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[3] <= 3): i 4 j 3 w[3] 2 D[3][1] 0 D[3][3] 3 max([w[3] + D[3][1], D[3][3]] 3  => D[4][3] = 3
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 0, 0, 0, 0, 0, 0, 0]
# case 2 (w[3] <= 4): i 4 j 4 w[3] 2 D[3][2] 0 D[3][4] 4 max([w[3] + D[3][2], D[3][4]] 4  => D[4][4] = 4
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 0, 0, 0, 0, 0, 0]
# case 2 (w[3] <= 5): i 4 j 5 w[3] 2 D[3][3] 3 D[3][5] 4 max([w[3] + D[3][3], D[3][5]] 5  => D[4][5] = 5
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 0, 0, 0, 0, 0]
# case 2 (w[3] <= 6): i 4 j 6 w[3] 2 D[3][4] 4 D[3][6] 6 max([w[3] + D[3][4], D[3][6]] 6  => D[4][6] = 6
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 6, 0, 0, 0, 0]
# case 2 (w[3] <= 7): i 4 j 7 w[3] 2 D[3][5] 4 D[3][7] 7 max([w[3] + D[3][5], D[3][7]] 7  => D[4][7] = 7
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 6, 7, 0, 0, 0]
# case 2 (w[3] <= 8): i 4 j 8 w[3] 2 D[3][6] 6 D[3][8] 7 max([w[3] + D[3][6], D[3][8]] 8  => D[4][8] = 8
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 6, 7, 8, 0, 0]
# case 2 (w[3] <= 9): i 4 j 9 w[3] 2 D[3][7] 7 D[3][9] 9 max([w[3] + D[3][7], D[3][9]] 9  => D[4][9] = 9
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# case 2 (w[3] <= 10): i 4 j 10 w[3] 2 D[3][8] 7 D[3][10] 10 max([w[3] + D[3][8], D[3][10]] 10  => D[4][10] = 10
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6]
# [0, 0, 0, 3, 3, 3, 6, 6, 6, 9, 9]
# [0, 0, 0, 3, 4, 4, 6, 7, 7, 9, 10]
# [0, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result: 10
