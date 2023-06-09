class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==0:
            return -1
        elif  dividend>=0 and divisor>0:
            return dividend//divisor
        else:
            new=(dividend//divisor)
            if new==dividend/divisor:
                if new >( 2**31-1):
                    return( 2**31)-1
                if new<(-( 2**31-1)):
                    return -2**31
                return new
            else:
                if new>=0:
                    return new
                else:
                    return new+1