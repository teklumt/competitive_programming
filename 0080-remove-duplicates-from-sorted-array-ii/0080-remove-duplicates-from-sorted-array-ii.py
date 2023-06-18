class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for n in nums:
            m=nums.count(n)
            if m >2:
                for m in range(m-2):
                    nums.remove(n)
        return len(nums)