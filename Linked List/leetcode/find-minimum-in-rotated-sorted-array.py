class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right =  len(nums) - 1
        
        while left  < right:
            mid = (left + right) // 2
            if  nums[left] > nums[mid] < nums[right]:
                if nums[left] > nums[right]:
                    right = mid
                else:
                    left = mid
            elif nums[left] <= nums[mid]:
                if nums[left] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return nums[left]

