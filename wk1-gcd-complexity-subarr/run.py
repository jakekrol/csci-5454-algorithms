#!/usr/bin/env python3
from f import cont_frac, cont_frac2ints, cont_frac_aprx, gcd, lcm, add_fracs, max_sub_sum_tbl_B, max_sub_sum_tbl_C, C_recurrence, C_lookup
import numpy as np
### Q1b
print('BEGIN Q1b')
print('running examples')

a,b = 2,7
arr = cont_frac(a,b)
print(f'a: {a} b: {b} arr: {arr}')

a,b = 19,29
arr = cont_frac(a,b)
print(f'a: {a} b: {b} arr: {arr}')

a,b = 707106781187,1000000000000
arr = cont_frac(a,b)
print(f'a: {a} b: {b} arr: {arr}')
print('END Q1b\n')

### Q1c
print('BEGIN Q1c')
examples = [
    [3,2],
    [1,1,1,9],
    # from q1b
    arr
]

arr = examples[2]
#a,b = cont_frac2ints(arr)
#print('arr:', arr)

a,b = cont_frac2ints(arr)
print('arr:', arr)
print(f'a/b: {a}/{b}')
print('END Q1c')

### Q1d
print('BEGIN Q1d')
def q1d(a,b):
    print(f'a={a},b={b}')
    aprx = cont_frac_aprx(a,b)
    for i in aprx:
        print(i)

print('Tests')
q1d(19,29)
print()
q1d(419,1008)
print()
print('Answers')
q1d(11,39)
print()
q1d(113,312)
print()
q1d(14159265359,100000000000)
#print('add 1 + 1/9', add_fractions(1,1,1,9))
#m = gcd(400, 24) 
#print('gcd', m)
#print('lcm', lcm(4, 3))
#a,b = 113, 312
#arr = cont_frac(a,b)
#print(f'a: {a} b: {b} arr: {arr}')
#
#a,b = 14159265359, 100000000000
#arr = cont_frac(a,b)
#print(f'a: {a} b: {b} arr: {arr}')
print('END Q1d')
print()

print('BEGIN Q3a')
print(max_sub_sum_tbl_B([1,-3,2,1]))
print(max_sub_sum_tbl_C([1,-3,2,1]))
for n in range(1, 101):
    arr = max_sub_sum_tbl_C(np.ones([n]))
    #print('arr_size', i, 'tbl_size', np.sum(arr))
    print(n, np.sum(arr))
arr = np.ones(8)
x = max_sub_sum_tbl_C(arr)
print(x)
x = np.random.randint(-100,100,22)
print('array:',x)
#x = [1,2,3,4]
C = max_sub_sum_tbl_C(x)
print('C table:')
print(C)
print('recurrence')
C_recurrence(C)
print('END Q3a')
print('BEGIN Q3c')
np.random.seed(0)
x = np.random.randint(-100, 100, 53)
print('x\n',x)
C = max_sub_sum_tbl_C(x)
print('C\n',C)
m = C_lookup(C,18,29)
print('m\n',m)
print('END Q3c')


