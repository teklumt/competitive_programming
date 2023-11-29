class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:return False 
        ori=x
        rev=0
        while ori!=0:
            rem=ori%10
            rev=rev*10+rem
            ori=ori//10
        return rev==x