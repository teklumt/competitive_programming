from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        num = SortedList(nums)
        for i in range(len(nums)):
            res.append(bisect_left(num,nums[i]))
            num.remove(nums[i])
        return res  