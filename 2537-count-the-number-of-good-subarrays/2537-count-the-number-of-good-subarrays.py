class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        ans = 0
        left = 0
        counts = collections.Counter()
        pairs = 0
        for right in range(N):
            pairs += counts[nums[right]]
            counts[nums[right]] += 1
            while pairs >= k:
                counts[nums[left]]-= 1
                pairs -= counts[nums[left]]
                left += 1
            ans += left
        return ans