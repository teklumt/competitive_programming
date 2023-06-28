class Solution:
    def pivotInteger(self, n: int) -> int:
        i = 0
        j = n
        if n==1:
            return 1 
        result = -1
        mid = (i+j)//2
        while mid < n:
            if ((mid*(mid+1))//2) == (((n*(n+1))//2)-((mid*(mid+1))//2))+mid:
                result = mid
                break
            mid += 1
        return result
