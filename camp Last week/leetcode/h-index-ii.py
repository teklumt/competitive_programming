class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = max(citations)
        res = -inf
        while left <= right:
            mid = (left + right) // 2
            ind = bisect_left(citations, mid)

            if mid >= n:
                right = mid - 1
            else:
                if  mid <= n - ind: 
                    res = max(res, mid)
                    left = mid + 1
                else:
                    right = mid - 1
        res = max(res,min(len(citations),citations[0]))
        return res


