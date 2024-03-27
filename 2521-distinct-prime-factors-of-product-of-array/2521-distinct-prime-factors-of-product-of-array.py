class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            k = 2
            while k <= i:

                while i % k == 0:
                    seen.add(k)
                    i //= k
                k += 1
        return len(seen) 
                