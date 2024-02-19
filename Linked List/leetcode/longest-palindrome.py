class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_hash = Counter(s)
        res = 0
        bol=False
        for i in count_hash:

            if count_hash[i]%2==0:
                res+=count_hash[i]
            
            else:
                bol=True
                res+=count_hash[i]-1
        return res + (1 if bol else 0)
       