class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right, ans = 1, position[-1] - position[0], 1
        while left <= right:
            mid = (left + right) // 2
            atEnd, putted = position[0], 1
            for i in range(1, len(position)):
                if position[i] - atEnd >= mid:
                    atEnd = position[i]
                    putted += 1
            if putted >= m:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans  