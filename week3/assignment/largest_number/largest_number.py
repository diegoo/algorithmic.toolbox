#!/usr/bin/python3
import sys

debug = False

def is_greater_or_equal(n, m):
    if not m:
        return True
    return int(str(n)+str(m)) >= int(str(m)+str(n))

def largest_number(numbers):
    result = ""
    while numbers != []:
        max_number = None
        for number in numbers:
            if debug: print("number", number)
            if is_greater_or_equal(number, max_number):
                if debug: print("number", number, "is >=", max_number)
                max_number = number
        result += str(max_number)
        numbers.remove(max_number)
    return result

if __name__ == '__main__':

    if debug:
        def check(numbers, expected):
            result = largest_number(numbers)
            print(numbers, expected, result)
            assert(expected == result)

        check([2,21], "221")
        check([9,4,6,1,9], "99641")
        check([23,39,92], "923923")

    else:
        input = sys.stdin.read()
        data = input.split()
        a = data[1:]
        print(largest_number(a))
