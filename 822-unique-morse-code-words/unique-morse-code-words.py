class Solution(object):
    def uniqueMorseRepresentations(self, words):
       
        table = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
            "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
            "..-","...-",".--","-..-","-.--","--.."
        ]
        return len({''.join(table[ord(c)-97] for c in w) for w in words})