#!/usr/bin/python3

import sys
from math import floor

test = True
debug = True

def get_majority_element_naive(a):
    n = len(a)
    for i in a:
        count = 0
        for j in a:
            if j == i: count += 1
        if count > floor(n/2):
            if debug: print("found it", i)
            return 1
    return 0

def get_majority_element(a, left, right):
    if left == right:
        if debug: print("(left:%d,right:%d)" % (left,right))
        return -1
    if left + 1 == right:
        if debug: print("leaf", "(left:%d,right:%d)->%d" % (left,right,a[left]))
        return a[left]

    mid = floor((left+right-1)/2)
    if debug: print("all", a[left:right+1], "mid", mid, a[mid],"halves", a[left:mid+1], a[mid+1:right+1])
    first_half = get_majority_element(a, left, mid+1)
    second_half = get_majority_element(a, mid+1, right)

    half_of_all = floor((right-left)/2)
    
    first_half_majority_element = sum([1 for i in range(left, right) if a[i] == first_half])
    if first_half_majority_element > half_of_all:
        if debug: print("(%d,%d)->%d" % (left,mid,first_half_majority_element))
        return first_half

    second_half_majority_element = sum([1 for i in range(left, right) if a[i] == second_half])
    if second_half_majority_element > half_of_all:
        if debug: print("(%d,%d)->%d" % (mid+1,right,second_half_majority_element))
        return second_half

    return -1


if __name__ == '__main__':

    if test:

        def test(a, expected_naive, expected):
            assert(expected_naive == get_majority_element_naive(a))
            n = len(a)
            result = get_majority_element(a, 0, n)
            print("*"*80,result)
            assert(expected == result)

        test([1,2,3,4], 0, -1)
        test([12,8,12,4,12], 1, 12)
        test([1], 1, 1)
        test([2,124554847,2,941795895,2,2,2,2,792755190,756617003], 1, 2)
        test([2,3,9,2,2], 1, 2)
        test([3,2,9,2,2], 1, 2)
        test([5,5,5,5,5,5,6], 1, 5)
        test([5,5,5,5,6,5], 1, 5)
        test([5,6], 0, -1)
        test([512766168,717383758,5,126144732,5,573799007,5,5,5,405079772], 0, -1)
        test([1,2,2], 1, 2)
        test([1,2,3,1], 0, -1)
        
    else:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))
        if get_majority_element(a, 0, n) != -1:
            print(1)
        else:
            print(0)
