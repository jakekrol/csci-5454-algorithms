#!/usr/bin/env python3
import math
import sys

### Q1b
print('BEGIN Q1b')
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
    r=math.inf
    while (r > 0):
        q = math.floor(b/a)
        arr.append(q)
        r = b - (a * q)
        # r/a is new a/b
        a,b = r,a
    return arr
    # note, upon termination, we want the final a integer which is b
    #print(f'quotients: {arr} final frac: {r}/{b}')

if len(sys.argv) > 1:
    a,b = int(sys.argv[1]), int(sys.argv[2])
    print('a',a,'b',b)
    arr = cont_fract(a,b)
    print('arr', arr)
else: 
    print('running examples')

    a,b = 2,7
    print('a',a,'b',b)
    arr = cont_fract(a,b)
    print('arr', arr)

    a,b = 19,29
    print('a',a,'b',b)
    arr = cont_fract(a,b)
    print('arr', arr)

    a,b = 707106781187,1000000000000
    print('a',a,'b',b)
    arr = cont_fract(a,b)
    print('arr', arr)
    print('END Q1b\n')

### Q1c
#!/usr/bin/env python3

print('BEGIN Q1c')
def get_b(a,q,r):
    return a * (q + (r/a))

examples = [
    [3,2],
    [1,1,1,9],
    [9,3,17,3,1,9,1,1,3,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]
]

print('arr', arr)

n = len(arr) - 1
a = arr[n]
r = 1
while (n > 0):
    q = arr[n-1]
    b = get_b(a,q,r)
    print('a', a, 'q', q, 'b', b)
    r = a
    a = b
    n -=1
#a = arr[0]
#q = arr[1]
#r = 1
#
#b = get_b(a,q,r)
#a = a
print(f'a/b: {r}/{b}')

