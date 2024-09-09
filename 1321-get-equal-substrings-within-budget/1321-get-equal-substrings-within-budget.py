class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        left = 0
        for i in range(len(s)):
            diff = abs(ord(s[i]) - ord(t[i]))
            while left < i and maxCost < diff:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
            if maxCost >= diff:
                res = max(res, i - left + 1)
                maxCost -= diff
            else:
                left += 1
        return res
                





