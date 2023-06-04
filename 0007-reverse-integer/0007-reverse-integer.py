class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if (x>2**31)or(x<(-1*2**31)):return 0
        if x<0:
            x=-1*x
            while x!=0:
                rem=x%10
                rev=rev*10 + rem
                x=x//10
            rev=-1*rev
            if (rev<(-1*(2**31))):return 0
            return rev
        else:
            while x!=0:
                rem=x%10
                rev=rev*10 + rem
                x=x//10
            if (rev>(2**31)):return 0
            return rev