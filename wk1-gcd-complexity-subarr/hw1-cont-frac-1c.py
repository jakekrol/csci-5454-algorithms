#!/usr/bin/env python3

def get_b(a,q,r):
    return a * (q + (r/a))

#arr = [3,2]
arr = [1,1,1,9]
#arr = [9,3,17,3,1,9,1,1,3,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1]

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

