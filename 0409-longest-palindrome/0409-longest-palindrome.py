class Solution:
    def longestPalindrome(self, s: str) -> int:
        Count = Counter(list(s))
        res = 0
        maxx = 0
        for i in Count:
            if Count[i] %2 :
                maxx = 1
                res += Count[i] - 1
            else: res += Count[i]
        return res + (1 if maxx else 0)