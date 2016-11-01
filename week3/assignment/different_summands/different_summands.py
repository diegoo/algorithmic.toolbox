#!/usr/bin/python3
import sys

debug = False

def optimal_summands(n):
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    return solve(n, 1)

def solve(k, l):
    if debug: print("solving k", k, "l", l)
    if k <= 2 * l:
        summands = list(range(1, l))
        if k != 0:
            summands.append(k)
            if debug: print("added k", k, "summands", summands)
        return summands
    else:
        if debug: print("added l", l)
        return solve(k-l, l+1)


# def optimal_summands(n):
#     if n == 1:
#         return [1]
#     return solve(n, 1, summands = [])

# def solve(k, l, summands):
#     if k <= 2 * l:
#         summands.append(k)
#         if debug: print("added k", k, "summands", summands)
#         return summands
#     else:
#         summands.append(l)
#         if debug: print("added l", l, "summands", summands)
#         return solve(k-l, l+1, summands)

# def optimal_summands(n):
#     summands = []
#     for i in range(1, n):
#         n -= i
#         if n < i:
#             summands.append(n)
#             break
#         elif n == 0:
#             summands.append(i)
#             break
#         else:
#             summands.append(i)
#     return summands

if __name__ == '__main__':

    if debug:
        for n in range(1, 101):
            result = optimal_summands(n)
            print(n, result)
            assert(sum(result) == n)

        assert([2] == optimal_summands(2))
        assert([1,2,3] == optimal_summands(6))
        assert([1,2,5] == optimal_summands(8))
        assert([1,2,3,4,5] == optimal_summands(15))
        assert([1,2,3,4,5,8] == optimal_summands(23))
            
    else:
        input = sys.stdin.read()
        n = int(input)
        summands = optimal_summands(n)
        print(len(summands))
        for x in summands:
            print(x, end=' ')
