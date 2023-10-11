class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0 
        right=len(s)-1
        while left<right:
            s1=s[left:right]
            s2=s[left+1:right+1]
            if s[left]!=s[right]:
                if s1==s1[::-1] or s2==s2[::-1]:
                    return True
                return False
            right-=1
            left+=1
        return True