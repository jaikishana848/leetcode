class Solution(object):
    def intersect(self, nums1, nums2):
        count={}
        a=[]
        for i in nums1:
            count[i]=count.get(i,0)+1
        for j in nums2:
            if j in count and count[j]>0:
                a.append(j)
                count[j]-=1
        return a