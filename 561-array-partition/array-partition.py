class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        a=0
        for i in range(0,len(nums),2):
            a+=nums[i]
        return a