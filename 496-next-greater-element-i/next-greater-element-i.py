class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack=[]
        d={}
        for i in nums2:
            while stack and stack[-1]<i:
                d[stack.pop()]=i
            stack.append(i)
        for j in stack:
            d[j]=-1
        return [d[k] for k in nums1]