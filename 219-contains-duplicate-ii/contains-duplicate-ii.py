class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        a = {}
    
        for i, nums in enumerate(nums):
            if nums in a and i - a[nums] <= k:
                return True
            a[nums] = i  
        
        return False
        