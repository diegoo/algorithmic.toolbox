#!/usr/bin/python3

import sys
from operator import itemgetter

debug = False

def solve(capacity, items, accum_value):
    if debug: print("capacity", capacity, "items", items)

    if capacity == 0 or items == []:
        return accum_value
 
    best_item = items[0]
    
    kgs_added = 0
    w, v, v_per_kg = best_item
    while kgs_added < capacity and kgs_added < w:
        accum_value += v_per_kg
        kgs_added += 1
        best_item = (best_item[0] - 1, v, v_per_kg)
        if debug: print("value added", v_per_kg, "best_item", best_item)
        
    capacity -= kgs_added
        
    if best_item[0] == 0:
        items = items[1:]
    else:
        items = [best_item] + items[1:]
    if debug: print("items after using best", items)
    if debug: print("accum_value", accum_value)
    
    return solve(capacity, items, accum_value)
    
def get_optimal_value(capacity, weights, values):
    items_sorted_by_value_per_kg = sorted([(w,v,v/w) for (w,v) in zip(weights, values)], key=itemgetter(2), reverse=True)
    return solve(capacity, items_sorted_by_value_per_kg, 0.0)


if __name__ == "__main__":

    if debug:
        capacityW = 50
        data = [(60, 20), (100, 50), (120, 30)]
        weights = [y for (x,y) in data]
        values = [x for (x,y) in data]
        expected = 180.0 # (30 * 40) + (20 * 3)
        result = get_optimal_value(capacityW, weights, values)
        print("expected", expected, "result", result)
        assert(abs(expected - result) <= 0.001)

        capacityW = 10
        data = [(500, 30)]
        weights = [y for (x,y) in data]
        values = [x for (x,y) in data]
        expected = 166.6667
        result = get_optimal_value(capacityW, weights, values)
        print("expected", expected, "result", result)
        assert(abs(expected - result) <= 0.0001)
        
    else:
        data = list(map(int, sys.stdin.read().split()))
        n, capacity = data[0:2]
        values = data[2:(2 * n + 2):2]
        weights = data[3:(2 * n + 2):2]
        opt_value = get_optimal_value(capacity, weights, values)
        print("{:.10f}".format(opt_value))
