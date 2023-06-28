class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        else:
            if n<0:
                return False
            result=math.log2(n)
            return result==int(result)