class Solution(object):
    def merge(self, nums1, m, nums2, n):
        count=nums1.count(0)
        for i in range(count):
            if len(nums1)>m:
                nums1.remove(0)
        nums1.extend(nums2)   
        nums1.sort() 
        