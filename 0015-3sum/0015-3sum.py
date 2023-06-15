class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for n in range(len(nums)):
            if n > 0 and nums[n] == nums[n-1]:
                continue
            l = n+1
            r = len(nums)-1
            while l < r:
                summ = nums[l]+nums[r]+nums[n]
                if summ < 0:
                    l = l+1
                elif summ > 0:
                    r = r-1
                else:
                    result.append([nums[n], nums[l], nums[r]])
                    l = l+1
                    while nums[l] == nums[l-1] and l < r:
                        l = l+1
        return result