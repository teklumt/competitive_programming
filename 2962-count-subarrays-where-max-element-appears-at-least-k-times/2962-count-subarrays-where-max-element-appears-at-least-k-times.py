class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        
        maxx = max(nums)
        left = 0
     
        for right in range(len(nums)):
            if nums[right] == maxx:
                count += 1
            while left <= right and count >= k:
                if nums[left] == maxx:
                    count -= 1
                left += 1
            res += left
           
        
        return res

        