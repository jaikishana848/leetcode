class Solution(object):
    def minimumOperations(self, nums):
        count=0
        a=set()
        for num in nums:
            if num>0:
                a.add(num)
        return len(a)