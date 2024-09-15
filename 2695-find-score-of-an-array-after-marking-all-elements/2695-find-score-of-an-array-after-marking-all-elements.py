class Solution:
    def findScore(self, nums: List[int]) -> int:
        score  = 0
        heaps = []
        marked = set()
        for i in range(len(nums)):
            heappush(heaps, (nums[i], i))
        while heaps:
            val, ind = heappop(heaps)
            if ind not in marked:
                score += val
                marked.add(ind)
                marked.add(ind + 1)
                marked.add(ind - 1)
        return score