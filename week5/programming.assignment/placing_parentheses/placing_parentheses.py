#!/usr/bin/python3

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    return 0


test_cases = [
    (0,0),
    (0+0,0),
    (9,9),
    (9*9,81),
    (1+5*6-3,33),
    (9*5*6-3,267),
    (1+1+1+1+1+1+1+1+1+1+1+1+1+1,14),
    (9*9*9*9*9*9*9*9*9*9*9*9*9*9,22876792454961),
    (9*9*9*9*9*9*9*9*9*9*9*9*9*9*9,205891132094649),
    (6*3-2-5+5+0+0+8-6*8+0-4-2+3+2,1650),
    (1+0+3*5+7-3*6*4-0-7+8-4*4*1*6,149040),
    (0*8*3+3-7*2*1+6*3*8*0-8+1-2*7,181125),
]


if __name__ == "__main__":
    print(get_maximum_value(input()))
