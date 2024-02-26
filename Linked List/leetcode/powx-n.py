class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if n==0:
               return 1
            if n<0:
                x=1/x
                n=abs(n)
            if n%2==1:
                return x*(power(x*x,n//2))
            else:
                return power(x*x,n//2)
        return power(x,n)
       