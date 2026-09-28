class Solution(object):
    def canJump(self, nums):
        a=0
        for i in range(len(nums)):
            if i>a:
                return False
            a=max(a,i+nums[i])
        return True