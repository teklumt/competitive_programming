# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left  = 1
        right = n
        res = n
        while left <= right:
            mid = (left + right)//2
            
            if isBadVersion(mid):
                right = mid - 1

                res = right 
            else:
                left = mid + 1
        return res + 1
            
