class Solution(object):
    def commonChars(self, words):
        a=list(words[0])
        for i in words[1:]:
            b=[]
            for j in a:
                if j in i:
                    b.append(j)
                    i=i.replace(j,"",1)      
            a=b
        return a