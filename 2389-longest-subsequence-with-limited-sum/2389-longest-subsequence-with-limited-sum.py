class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res=[nums[0]]
        for i in range(1,len(nums)):
            res.append(res[-1]+nums[i])
        return [bisect_right(res,q) for q in queries]
        