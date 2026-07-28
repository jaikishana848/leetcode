class Solution(object):
    def findDisappearedNumbers(self, nums):
        b=set(nums)
        a=[]
        for i in range(1,len(nums)+1):
            if i not in b:
                a.append(i)
        return a
