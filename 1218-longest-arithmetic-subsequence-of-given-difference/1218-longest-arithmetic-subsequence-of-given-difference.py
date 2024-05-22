class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = defaultdict(int)
        for i in arr:
           count[i] = count[i - difference] + 1
        return max(count.values())