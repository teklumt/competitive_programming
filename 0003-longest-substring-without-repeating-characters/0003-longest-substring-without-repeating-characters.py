class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num = []
        l = 0
        for i in range(len(s)):
            num.append(s[i])
            if len(num) == len(set(num)) and len(num) > l:
                l = len(num)
            else:
                while len(num) != len(set(num)):
                    del num[0]
        return l
