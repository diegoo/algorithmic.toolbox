#!/usr/bin/python3

import sys
from math import floor

debug = False

def get_majority_element_naive(a):
    n = len(a)
    for i in a:
        count = 0
        for j in a:
            if j == i: count += 1
    if count > n/2:
        if debug: print("found it", i)
        return 1
    return 0

def get_majority_element(a, left, right):
    if left == right:
        if debug: print(left, " == ", right)
        return a[left]

    mid = left + floor((right-left)/2)
    first_half_majority_element = get_majority_element(a, left, mid)
    second_half_majority_element = get_majority_element(a, mid+1, right)
    if debug: print(left,mid,first_half_majority_element,"|",mid+1,right,second_half_majority_element)

    if first_half_majority_element == second_half_majority_element:
        return first_half_majority_element

    if first_half_majority_element != -1 and second_half_majority_element == -1:
        count = sum([1 for i in a[left:right+1] if i == first_half_majority_element])
        if count > mid-left: return first_half_majority_element

    if second_half_majority_element != -1 and first_half_majority_element == -1:
        count = sum([1 for i in a[left:right+1] if i == second_half_majority_element])
        if count > mid-left: return second_half_majority_element

    return -1

if __name__ == '__main__':

    def test(a, expected_naive, expected):
        assert(expected_naive == get_majority_element_naive(a))
        result = get_majority_element(a, 0, len(a)-1)
        print("*"*80,result)
        assert(expected == result)
        
    if debug:
        test([2,3,9,2,2], 1, 2)
        test([3,2,9,2,2], 1, 2)
        test([12,8,12,4,12], 1, 12)
        test([1,2,3,4], 0, -1)
        test([1,2,3,1], 0, -1)

    else:
        input = sys.stdin.read()
        n, *a = list(map(int, input.split()))
        if get_majority_element(a, 0, n) != -1:
            print(1)
        else:
            print(0)
