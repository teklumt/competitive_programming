class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        cur = 0
        num = [1]
        seen = set([1])
        while n:
            cur = heappop(num)
            n -= 1
            for i in primes:
                if i * cur not in seen:
                    heappush(num, i * cur)
                    seen.add(i * cur)
        return cur
