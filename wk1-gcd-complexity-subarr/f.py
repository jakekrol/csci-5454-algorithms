import math
import numpy as np

def gcd(m, n):
    while n > 0:
        m,n = n, m%n
    return m

def lcm(m, n):
    return (m*n) // gcd(m, n)


def add_fracs(n1, d1, n2, d2):
    # find least common demoninator (lcd)
    # scale numerators using lcd
    lcd = lcm(d1, d2)
    n1 = n1 * (lcd // d1)
    n2 = n2 * (lcd // d2)
    return n1 + n2, lcd

# conditions:
# 1) a,b,q, and r are ints
# 2) 0 < a < b
# 3) r in (0,1)

# formulas:
# a/b = 1 / (q + r/a)
# q = floor(b/a)
# r = b - a(floor(b/a)) = b - aq
def cont_frac(a,b):

    arr = []
    r=math.inf
    while (r > 0):
        q = math.floor(b/a)
        arr.append(q)
        r = b - (a * q)
        a,b = r,a
    return arr
#def cont_frac2ints(arr):
#    def get_b(a,q,r):
#        return a * (q + (r/a))
#
#    n = len(arr) - 1
#    a = arr[n]
#    r = 1
#    while (n > 0):
#        q = arr[n-1]
#        b = get_b(a,q,r)
#        r = a
#        a = b
#        n -=1
#    return r,b

def cont_frac2ints(arr):
    i,j = 0,1
    while (j < len(arr) + 1):
        a = arr[i:j]
        a.reverse()
        # last denom
        n1 = 1
        d1 = a[0]
        for k in a[1:]:
            n1,d1 = add_fracs(n1,d1, n2=k, d2=1)
            n1,d1 = d1,n1
        j+=1
    return n1,d1

def cont_frac_aprx(a,b):
    arr = cont_frac(a,b)
    aprx = []
    i,j = 0,1
    while (j < len(arr) + 1):
        a = arr[i:j]
        #print('a',a)
        a.reverse()
        # last denom
        n1 = 1
        d1 = a[0]
        #print('n1', n1, 'd1', d1)
        for k in a[1:]:
            n1,d1 = add_fracs(n1,d1, n2=k, d2=1)
            # take reciprocal
            n1,d1 = d1,n1
            #print('n1', n1, 'd1', d1)
        aprx.append(f'{n1}/{d1} = {n1/d1}')
#        eps = 1 / a[0]
#        print('init eps', eps)
#        for k in a[1:]:
#            eps = 1 / (k + eps)
#            print('eps', eps, 'k', k)
#        aprx.append(eps)
        j+=1
    return aprx

def max_sub_sum_tbl_B(arr):
    n = len(arr)
    B = np.zeros([n,n],dtype=int)
    for i in range(n):
        for j in range(n):
            print('i', i, 'arr[i]', arr[i])
            print('j', j, 'arr[j]', arr[j])
            # +1 for inclusive stop idx
            B[i,j] = max(arr[i:i+j + 1])
    return B

def max_sub_sum_tbl_C(arr):
    n = len(arr)
    C = np.zeros([n,math.ceil(math.log2(n+1))],dtype=int)
    for i in range(n):
        j = 0
        while (i + (math.pow(2,j)) <= n):
            #if j==0 :
                #C[i,j] = arr[i]
            #else:
            stop = i + (2**j)
            #print('stop',stop)
            C[i,j] = max(arr[i:stop]) # inclusive stop
#        for j in range(n):
#            if (i + (2**j) <= n):
#            # +1 for inclusive stop idx
#                C[i,j] = max(arr[i:i+j + 1])
#            else:
#                C[i,j] = 0 
            j+=1
    return C

def C_recurrence(C):
    n = C.shape[0]
    print('n',n)
    for i in range(n):
        j = 0
        while (i + (math.pow(2,j)) <= n):
            #print('i',i,'j',j,'a',a,'b',b,'c',c)
            print('i',i,'j',j)
            a = C[i,j]
            b = C[i, j+1]
            c = C[i + (2**j), j]
            print('C[i, j+1]',b,'\tC[i,j]',a,'\tC[i + 2^j, j]',c,'\ti',i,'\tj',j)
          
            j+=1
    return 

def C_lookup(C,l,u):
    j = math.ceil(math.log2(u-l+1))
    return max(C[l,j], C[l + j - 1, j])

