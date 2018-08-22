#!/bin/pyhton

"""
   Use O(logN) implementation find the median for two sorted arrays
"""

# O(n+m) ==> O(n)
def merge(a,b):
    la = len(a)
    lb = len(b)
    if la == 0: return b
    if lb == 0: return a
    i = 0
    j = 0
    c = []
    while i < la and j < lb:
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif b[j] < a[i]:
            c.append(b[j])
            j += 1

    if i < la:
        c += a[i:]
    if j < lb:
        c += b[j:]
    return c
    

def find_median_On(a,b):
    if len(a) == 0 and len(b) == 0: return 0    
    # O(N)
    c = merge(a,b)
    l = len(c)
    if l % 2 != 0:
        ans = c[(l-1)/2]
    else:
        ans = float(c[l/2 - 1] + c[l/2]) / 2
    return ans

def find_median_Onlogn(a,b):
    if len(a) == 0 and len(b) == 0: return 0
    # Timsort - O(NlogN)
    c = sorted(a+b)   
    l = len(c)
    ans = 0
    if l % 2 != 0:
        ans = c[(l-1)/2]
    else:
        ans = float(c[l/2 - 1] + c[l/2]) / 2
    return ans

def findKth(a, b, k):
    n1 = len(a)
    n2 = len(b)
    if n1 > n2:
        return findKth(b, a, k)
    k = (n1+n2+1)/2
    l = 0
    r = n1
    while l < r:
        m1 = l + (r - l) /2
        m2 = k - m1
        if a[m1] < b[m2 - 1]:
            l = m1 + 1
        else:
            r = m1
    m1 = l
    m2 = k - l
    c1 = max(float('-inf') if m1 <= 0 else a[m1-1], 
             float('-inf') if m2 <= 0 else b[m2-1])
    if (n1 + n2) % 2 == 1:
        return c1
    c2 = min(float('inf') if m1 >= n1 else a[m1],
             float('inf') if m2 >= n2 else b[m2])
    return float(c1 + c2) / 2

def find_median_Ologn(a, b):
    la = len(a)
    lb = len(b)
    if la == 0 and lb == 0: return 0
    l = la + lb
    ans = 0
    n = 0

    if l % 2 == 1:
        n = (l-1) / 2  
    elif l % 2 == 0:
        n = l / 2 
    ans = findKth(a, b, n)        
    return ans
    
    

if __name__ == '__main__':
    # Testcase1, Expect 5.5
    a = [1,3,5,7,9]
    b = [2,4,6,8,10]

    # Testcase2, Expect 5.5
    a = [1,2,3,4,5]
    b = [6,7,8,9,10]
    
    # Testcase3, Expect 5.5
    a = [1,2,3,4,10]
    b = [5,6,7,8,9]

    # Testcase4, Expect 5
    a = [1,2,3,4]
    b = [5,6,7,8,9]

    # Testcase5, Expect 5
    a = [1,2,3,8]
    b = [5,6,9]
 
    # Testcase6, Expect 4.5
    a = [1,2,3,8]
    b = [6,9]
 
    # Testcase 7, Expect 1
    a = [0,0]
    b = [1,1,1]
 
    # Testcase 8, Expect 2
    a = []
    b = [1,2,3]
 
    # Testcase 9, Expect 4
    a = [2,4,6]
    b = []
 
    # Testcase 10, Expect 0
    a = []
    b = []

    # Testcase 11, Expect 0
    a = [1,2]
    b = [3,4]

    #print find_median_Onlogn(a,b)
    #print find_median_On(a,b)
    print find_median_Ologn(a,b)
