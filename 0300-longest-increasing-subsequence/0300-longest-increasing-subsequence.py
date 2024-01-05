class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[nums[0]]

        for i in range(1,len(nums)):
            if nums[i]>arr[-1]:
                arr.append(nums[i])
            else:
                arr[bisect_left(arr,nums[i])]=nums[i]
        return len(arr)