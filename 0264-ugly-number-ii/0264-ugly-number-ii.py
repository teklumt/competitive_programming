class Solution:
    def nthUglyNumber(self, n: int) -> int:
        Heap = [1]
        Prime = [2,3,5]
        cur = 0
        while n > 0:

            cur = heappop(Heap)

            n -= 1
            for e in Prime:
                if e * cur not in Heap:
                    heappush(Heap, e * cur)
        return cur