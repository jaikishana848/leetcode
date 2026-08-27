class Solution(object):
    def repeatedNTimes(self, nums):
        a=[]
        for i in nums:
            if i in a:
                return i
            a.append(i)