class Solution(object):
    def sortedSquares(self, nums):
        # for num in nums:
        #     a=sorted(nums)
        # return nums
        # nums.sort()
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return nums    