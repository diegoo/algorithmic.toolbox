#!/usr/bin/python3

DEBUG=False

def print_matrix(m, s1, s2):
    print("\n      " + ', '.join([c for c in s2]))
    for h in range(len(m)):
        if h > 0:
            print(s1[h-1], m[h])
        else:
            print(" ", m[h])

def get_matrix(s1, s2):
    height, width = len(s1), len(s2)
    D = [[0 for x in range(width+1)] for y in range(height+1)]
    for y in range(height+1):
        D[y][0] = y
        for x in range(width+1):
            D[0][x] = x
    return D

def edit_distance(s1, s2):
    D = get_matrix(s1, s2)
    if DEBUG:
        print("-"*40, s1, s2, "-"*40)
        print_matrix(D, s1, s2)

    height, width = len(s1)+1, len(s2)+1
    for x in range(1, width):
        for y in range(1, height):
            insertion = D[y][x-1] + 1
            deletion  = D[y-1][x] + 1
            match     = D[y-1][x-1]
            mismatch  = D[y-1][x-1] + 1
            # if DEBUG: print("y:%d" % (y), s1[y-1], "x:%d" % (x), s2[x-1], "D[y]", D[y])
            if s1[y-1] == s2[x-1]: D[y][x] = min([insertion, deletion, match])
            else: D[y][x] = min([insertion, deletion, mismatch])

    if DEBUG: print_matrix(D, s1, s2)
    return D[height-1][width-1]


if __name__ == "__main__":
    
    if DEBUG:
        test_cases = [
            ("ab", "ab", 0),
            ("ab", "abc", 1),
            ("short", "ports", 3),
            ("editing", "distance", 5),
        ]
        for (s1, s2, expected_distance) in test_cases:
            result = edit_distance(s1, s2)
            print("result:", result)
            assert(result == expected_distance)
    
    else:
        print(edit_distance(input(), input()))
