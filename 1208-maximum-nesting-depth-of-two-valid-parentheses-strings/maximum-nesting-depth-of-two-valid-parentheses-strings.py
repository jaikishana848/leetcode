class Solution(object):
    def maxDepthAfterSplit(self, seq):
        a=[]
        b=0
        for i in seq:
            if i=="(":
                b+=1
                a.append(b%2)
            else:
                a.append(b%2)
                b-=1
        return a
        