class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        if n%2==0:
            return (pow(20,n//2,mod))%mod
        elif n%2!=0:
            return (pow(20,n//2,mod)*5)%mod