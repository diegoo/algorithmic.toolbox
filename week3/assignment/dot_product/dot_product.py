#!/usr/bin/python3

import sys

debug = False

def max_dot_product(profit_per_click, average_clicks):
    result = 0
    while profit_per_click != []:
        best_profit_per_click = max(profit_per_click)
        best_average_clicks = max(average_clicks)
        profit_per_click.remove(best_profit_per_click)
        average_clicks.remove(best_average_clicks)
        result += best_profit_per_click * best_average_clicks
        if debug: print("best_profit_per_click", best_profit_per_click, "best_average_clicks", best_average_clicks, "-> result", result)
    return result

if __name__ == '__main__':

    if debug:
        a = [23]
        b = [39]
        expected = 897
        result = max_dot_product(a, b)
        print("-"*80)
        assert(expected == result)

        a = [1, 3, -5]
        b = [-2, 4, 1]
        expected = 23
        result = max_dot_product(a, b)
        print("-"*80)
        assert(expected == result)

    else:
        input = sys.stdin.read()
        data = list(map(int, input.split()))
        n = data[0]
        a = data[1:(n + 1)]
        b = data[(n + 1):]
        print(max_dot_product(a, b))
