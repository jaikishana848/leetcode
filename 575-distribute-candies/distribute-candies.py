class Solution(object):
    def distributeCandies(self, candyType):
        a=len(candyType)
        b=a/2
        return min(b,len(set(candyType)))