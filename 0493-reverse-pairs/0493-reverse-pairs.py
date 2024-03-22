class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        def merge(left , right):
            nonlocal res

            l = 0
            r = 0

            while l < len(left):
                while r < len(right):
                    if left[l] > 2 * right[r]:
                        r += 1
                    else:
                        break
                res += r
                l += 1
            
            i = 0
            j = 0
            SortedArray = []
            while i< len(left) and j <len(right):
                if left[i] <= right[j]:
                    SortedArray.append(left[i])
                    i += 1
                else:
                    SortedArray.append(right[j])
                    j += 1
            SortedArray.extend(left[i:])
            SortedArray.extend(right[j:])
            return SortedArray
                        
            
            

        
        def mergeSort(nums):
            if len(nums) <=1:
                return nums
            mid = len(nums) // 2
            left = mergeSort(nums[:mid ])
            right = mergeSort(nums[mid :])

            return merge(left, right)
        mergeSort(nums)
        return res
