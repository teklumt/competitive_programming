class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        if len(word1)>len(word2):
            for n in range(len(word2)):
                result+=word1[n]+word2[n]
            result+=word1[len(word2):]
        elif len(word2)==len(word1):
            for n in range(len(word2)):
                result+=word1[n]+word2[n]
        else:
            for n in range(len(word1)):
                result+=word1[n]+word2[n]
            result+=word2[len(word1):]
        return result