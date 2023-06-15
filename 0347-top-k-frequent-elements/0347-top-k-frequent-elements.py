class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        for n in set(nums):
            result.append([nums.count(n), n])
        result.sort()
        final = []
        for m in range(k):
            final.append(result[-1-m][1])
        return final