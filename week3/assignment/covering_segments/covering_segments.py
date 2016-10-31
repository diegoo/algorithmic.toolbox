#!/usr/bin/python3

import sys
from collections import namedtuple
from operator import attrgetter

debug = True

Segment = namedtuple('Segment', 'start end')

def solve(ordered_segments):
    if debug: print("ordered_segments", ordered_segments)
    points = []
    left_end = [p.start for p in ordered_segments][0]
    right_end = ordered_segments[-1].end
    if debug: print("left_end", left_end, "right_end", right_end)

    p = left_end
    while ordered_segments != [] and p <= right_end:
        first_segment = ordered_segments[0]
        
    
    return points

def optimal_points(segments):
    ordered_segments = sorted(segments, key = attrgetter('end'))
    return solve(ordered_segments, [])


if __name__ == '__main__':
    if debug:
        n = 3
        segments = [Segment(1,3), Segment(2,5), Segment(3,6)]
        expected = (1, [3])
        result = optimal_points(segments)
        print(result)
        assert(expected == (len(result), result))               

        n = 4
        segments = [Segment(4,7), Segment(1,3), Segment(2,5), Segment(5,6)]
        expected = (2, [3, 6])
        result = optimal_points(segments)
        print(result)
        assert(expected == (len(result), result))

    else:
        input = sys.stdin.read()
        n, *data = map(int, input.split())
        segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
        points = optimal_points(segments)
        print(len(points))
        for p in points:
            print(p, end=' ')
