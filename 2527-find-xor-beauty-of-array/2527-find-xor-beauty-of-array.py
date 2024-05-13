class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        return reduce(lambda i, x: i ^ x, nums, 0)
