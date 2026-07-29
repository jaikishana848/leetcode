class Solution(object):
    def addBinary(self, a, b):
        c=bin(int(a,2)+int(b,2))[2:]
        return c
        
        