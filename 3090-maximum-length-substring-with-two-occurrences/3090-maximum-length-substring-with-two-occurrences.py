class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = Counter()
        res = 0
        
        left = 0
        for right in range(len(s)):
            while count[s[right]] >= 2:
                count[s[left]] -= 1
                left += 1
            count[s[right]] += 1
            res = max(res, right - left + 1)
     
        return res

            

