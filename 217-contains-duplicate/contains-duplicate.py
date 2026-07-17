class Solution(object):
    def containsDuplicate(self, nums):
    
        for i in nums:
            if len(nums)!=len(set(nums)):
                return True
            else:
                return False