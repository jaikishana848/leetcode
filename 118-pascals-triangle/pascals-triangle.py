class Solution(object):
    def generate(self, numRows):
        b=[]
        for i in range(numRows):
            count=1
            a=[]
            for j in range(i+1):
                a.append(count)
                count=count*(i-j)//(j+1)
            b.append(a)
        return b