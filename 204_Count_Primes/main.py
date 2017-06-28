#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution(object):
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x * x < n:
            if isPrime[x]:
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)
                            

if __name__ == '__main__':
#    print Solution().countPrimes(0)
#    print Solution().countPrimes(1)
    print Solution().countPrimes(2) # expected 0
#    print Solution().countPrimes(3)
#    print Solution().countPrimes(5)
    print Solution().countPrimes(499979) 
