#!/usr/bin/python3

import sys
from math import floor

debug = False

def binary_search(data, key):
    if debug: print("*"*20, data, key)
    result = -1
    left, right = 0, len(data)-1 

    while left <= right:
        mid = left + floor((right-left)/2)
        if debug: print("mid", mid, "element", data[mid], "left", left, "right", right, "data", data[left:right+1])
        if key < data[mid]:
            right = mid-1
        elif key > data[mid]:
            left = mid+1
        elif key == data[mid]:
            result = mid
            if debug: print("found at", mid, "key", key, "element", data[mid])
            break

    return result

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':

    if debug:
        data, keys = [1,5,8,12,13], [8,1,23,1,11]
        assert([2,0,-1,0,-1] == [linear_search(data, i) for i in keys])
        assert([2,0,-1,0,-1] == [binary_search(data, i) for i in keys])
    
    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        m = data[n + 1]
        a = data[1 : n + 1]
        for x in data[n + 2:]:
            # replace with the call to binary_search when implemented
            # print(linear_search(a, x), end = ' ')
            print(binary_search(a, x), end = ' ')
