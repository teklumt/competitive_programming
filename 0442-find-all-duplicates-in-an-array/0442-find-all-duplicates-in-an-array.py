class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        res = set()
        while i < len(nums):
            if i == nums[i]  - 1:
                i += 1
            else:
                ind = nums[i] - 1
                if nums[ind] == nums[i] :
                    res.add(nums[i])
                    i += 1
                else:
                    nums[ind],nums[i] = nums[i], nums[ind]
        return res
            
                    
        
