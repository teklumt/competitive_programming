class Solution:
    def reverseWords(self, s: str) -> str:
        nn=""
        
        num=s.split()
        return " ".join(reversed(num))
        