class Solution(object):
    def findRelativeRanks(self, score):
        a=sorted(score,reverse=True)
        b={}
        for i in range(len(a)):
            if i==0:
                b[a[i]]="Gold Medal"
            elif i==1:
                b[a[i]]="Silver Medal"
            elif i==2:
                b[a[i]]="Bronze Medal"
            else:
                b[a[i]]=str(i+1)
        c=[]
        for j in score:
            c.append(b[j])
        return c

        
    
        