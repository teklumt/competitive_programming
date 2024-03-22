class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            else:
                ind = nums[i] - 1
                if ind >= len(nums) or nums[ind] == nums[i]:
                    i += 1
                else:
                    nums[ind], nums[i]= nums[i], nums[ind]
                    
        # print(nums)
        return [j + 1 for j in range(len(nums)) if j != nums[j] - 1]
        # return [0]