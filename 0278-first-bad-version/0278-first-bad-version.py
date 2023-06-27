# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        first=0
        last=n-1
        red=n
        while first<=last:
            mid=(first+last)//2
            if isBadVersion(mid+1)==True:
                red=mid+1
                last=mid-1
            elif isBadVersion(mid+1)==False:
                first=mid+1
        return red