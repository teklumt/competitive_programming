class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        rep = { 'a': 1, 'e' : 2, 'i': 4, 'o': 8, 'u' : 16}
        state = 0
        firstOccurance = {0 : -1}
        res = 0
        for i in range(len(s)):
            if s[i] in rep:
                state ^= rep[s[i]]
            if state in firstOccurance:
                res = max(res , i - firstOccurance[state])
            else:
                firstOccurance[state] = i
        return res





                    


