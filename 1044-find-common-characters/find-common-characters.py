class Solution:
    def commonChars(self, words):
        ans = list(words[0])

        for word in words[1:]:
            temp = []
            for ch in ans:
                if ch in word:
                    temp.append(ch)
                    word = word.replace(ch, "", 1)
            ans = temp

        return ans