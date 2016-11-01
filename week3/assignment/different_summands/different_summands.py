#!/usr/bin/python3
import sys

debug = False

def optimal_summands(n):
    if n <= 2: return [n]
    summands = []
    k = n
    l = 1
    while l <= n/2:
        if k <= 2 * l: break
        summands.append(l)
        k -= l
        l += 1
    if k != 0:
        summands.append(k)
    return summands

if __name__ == '__main__':

    if debug:
        for n in range(1, 101):
            result = optimal_summands(n)
            print(n, result)
            assert(sum(result) == n)

        assert([1] == optimal_summands(1))
        assert([2] == optimal_summands(2))
        assert([1,2] == optimal_summands(3))
        assert([1,3] == optimal_summands(4))
        assert([1,4] == optimal_summands(5))
        assert([1,2,3] == optimal_summands(6))
        assert([1,2,5] == optimal_summands(8))
        assert([1,2,3,4,5] == optimal_summands(15))
        assert([1,2,3,4,5,8] == optimal_summands(23))
        assert(len(optimal_summands(987654321)) == 44443)
        assert(len(optimal_summands(12345678910)) == 157134)
        assert(len(optimal_summands(2673516735757)) == 2312364)

    else:
        input = sys.stdin.read()
        n = int(input)
        summands = optimal_summands(n)
        print(len(summands))
        for x in summands:
            print(x, end=' ')

# --------------------------------------------------------------------------------

# recursive versions:

# def optimal_summands(n):
#     if n == 1:
#         return [1]
#     if n == 2:
#         return [2]
#     return solve(n, 1)
# def solve(k, l):
#     if debug: print("solving k", k, "l", l)
#     if k <= 2 * l:
#         summands = list(range(1, l))
#         if k != 0:
#             summands.append(k)
#             if debug: print("added k", k, "summands", summands)
#         return summands
#     else:
#         if debug: print("added l", l)
#         return solve(k-l, l+1)

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
