class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x
        
        final = 0

        while left < right and right > 1:
            mid = (left + right )//2
            res = mid * mid
            if  res == x:
                return mid
            elif res < x:
                left = mid
                if res == final:
                    return mid
                final = res
            else:
                right = mid
        return x
