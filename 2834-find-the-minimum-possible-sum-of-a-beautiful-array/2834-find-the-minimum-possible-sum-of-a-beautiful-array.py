class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ans = set()
        cur = 1
        while len(ans) < n:
            if target - cur not in ans:
                ans.add(cur)
            cur += 1
        return sum(ans)