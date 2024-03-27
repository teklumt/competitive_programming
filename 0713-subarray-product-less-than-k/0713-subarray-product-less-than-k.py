class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        pro = 1
        
        for i in range(len(nums)):
            pro *= nums[i]
            while pro >= k and left <= i:

                pro //= nums[left]
                left += 1
            count += i - left + 1
        return count
    
    
    
    

        """
        class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        pro = 1
        i = 0
        while i < len(nums):
            pro *= nums[i]
            while pro >= k and left <= i:
                n = i - left 
             
                count += max(n - 1, 0)
                pro //= nums[left]
                left += 1

            i += 1
        n = i - left 
        count += n *(n - 1) //2 
        
        for j in nums:
            if j < k:
                count += 1
        return count
        
        """