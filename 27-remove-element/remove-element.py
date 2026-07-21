class Solution(object):
    def removeElement(self, nums, val):
        a=len(nums)
        while a>0:
            if nums[a-1]==val:
                nums.remove(val)
            a-=1


            

          