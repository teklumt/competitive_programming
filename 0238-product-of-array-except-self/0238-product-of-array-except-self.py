class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        ls = [1]
        for i in range(1, len(nums)):
            ls.append(nums[i - 1] * prefix)
            prefix = ls[i]
        for j in range(len(nums) -1, 0, -1):
            nums[j] = postfix * nums[j]
            postfix = nums[j]
        nums = nums[1:]
        nums.append(1)
        for i in range(len(nums)):
            ls[i] = ls[i]*nums[i]
        return ls
