class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res=""
        for i in words:
            if i in s and len(res)<len(s):
                res+=i
            else:
                break
        
        return res==s