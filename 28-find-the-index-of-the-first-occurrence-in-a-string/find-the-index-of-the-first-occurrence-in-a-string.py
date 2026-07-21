class Solution(object):
    def strStr(self, haystack, needle):
        a=[]
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1

        