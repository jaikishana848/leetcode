class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        a=0
        for i in nums:
            if i==1:
                count+=1
                a=max(a,count)
            else:
                count=0        
        return a