class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        k = len(nums)
        num = [[]]
        final = []
        for i in range(k):
            num += (combinations(nums, i+1))
        for i in num:
            final.append(list(i))
        return final
