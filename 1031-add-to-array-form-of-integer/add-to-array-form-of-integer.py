class Solution(object):
    def addToArrayForm(self, num, k):
        n=int("".join(map(str,num)))
        a=n+k
        return list(map(int,str(a)))