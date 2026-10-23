class Solution(object):
    def summaryRanges(self, nums):
        n=[]
        m=0
        for i in range(len(nums)):
            if i==len(nums)-1 or nums[i+1]!=nums[i]+1:
                if m==i:
                    n.append(str(nums[i]))
                else:
                    n.append("{}->{}".format(nums[m], nums[i]))
                m=i+1
        return n