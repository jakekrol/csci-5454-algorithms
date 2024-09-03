#!/usr/bin/env python3
import math
import sys

a,b = int(sys.argv[1]), int(sys.argv[2])
print(a,b)

def cont_fract(a,b):
    # conditions:
    # 1) a,b,q, and r are ints
    # 2) 0 < a < b
    # 3) r in (0,1)

    # formulas:
    # a/b = 1 / (q + r/a)
    # q = floor(b/a)
    # r = b - a(floor(b/a)) = b - aq

    # store each iter's quotient and the final 
    # divisor for reporting continued fraction
    arr = []

    while (a > 1):
        q = math.floor(b/a)
        arr.append(q)
        r = b - (a * q)
        # r/a is new a/b
        a,b = r,a

    # note, upon termination, we want the final a integer which is b
    print(f'quotients: {arr} final frac: {r}/{b}')

cont_fract(a,b)






