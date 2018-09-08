#!/bin/python

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        l = len(bits) - 1
        while i < l:
            i += bits[i] + 1
        return i == l
        
