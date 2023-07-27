class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count=0
        for n in range(1,min([a,b])+1):
            if a%n==0 and b%n==0:
                count=count+1
        return count