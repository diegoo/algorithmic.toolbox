#!/usr/bin/python3

import sys
from math import floor

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

def f(a, left, right):
    if left == right:
        if debug: print(left, " == ", right)
        return a[left]

    mid = left + floor((right-left)/2)
    if debug: print("left", left, "mid", mid, "right", right)
    first_half_majority_element = f(a, left, mid)
    second_half_majority_element = f(a, mid+1, right)
    if debug: print(left,mid,first_half_majority_element,"|",mid+1,right,second_half_majority_element)

    if first_half_majority_element == second_half_majority_element:
        return first_half_majority_element

    if first_half_majority_element != -1 and second_half_majority_element == -1:
        count = sum([1 for i in a[left:right+1] if i == first_half_majority_element])
        if count > mid-left: return first_half_majority_element

    if second_half_majority_element != -1 and first_half_majority_element == -1:
        count = sum([1 for i in a[left:right+1] if i == second_half_majority_element])
        if count > right-mid: return second_half_majority_element

    return -1

def get_majority_element(a, left, right):
    return f(a, left, right-1)


if __name__ == '__main__':

    if debug:

        def test(a, expected_naive, expected):
            assert(expected_naive == get_majority_element_naive(a))
            n = len(a)
            result = get_majority_element(a, 0, n)
            print("*"*80,result)
            assert(expected == result)
        
        test([1,2,3,4], 0, -1)
        test([1,2,3,1], 0, -1)
        test([512766168,717383758,5,126144732,5,573799007,5,5,5,405079772], 0, -1)
        test([5,6], 0, -1)

        test([2,3,9,2,2], 1, 2)
        test([3,2,9,2,2], 1, 2)
        test([12,8,12,4,12], 1, 12)
        test([5,5,5,5,6,5], 1, 5)
        test([5,5,5,5,5,5,6], 1, 5)
        
    else:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))
        if get_majority_element(a, 0, n) != -1:
            print(1)
        else:
            print(0)
