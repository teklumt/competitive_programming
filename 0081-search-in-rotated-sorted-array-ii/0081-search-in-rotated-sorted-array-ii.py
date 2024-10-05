class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        def func():
            nonlocal left, right
            while left < right and nums[left] == nums[right]:
                left += 1
        func()
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid  + 1
                else:
                    right = mid - 1
            func()
        return False
