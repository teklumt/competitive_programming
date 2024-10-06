class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 , size2 = len(nums1), len(nums2)
        if size2 < size1:
            nums1, nums2  = nums2, nums1
            size1, size2 = size2, size1
        left , right = 0, size1
        target = (size1 + size2 + 1) // 2
        
        while left <= right:
            mid = (left + right) // 2
            mid2 = target - mid
            l1 = l2 = -inf
            r1 = r2 = inf

            if mid < size1: r1 = nums1[mid]
            if mid2 < size2: r2 = nums2[mid2]
            if (mid - 1) >= 0: l1 = nums1[mid - 1]
            if (mid2 - 1) >= 0: l2 = nums2[mid2 - 1]

            if (l1 <= r2 and l2 <= r1): 
                if (size1 + size2) % 2: return max(l1 , l2)
                else: return (min(r1, r2) + max(l1, l2)) / 2
            elif(l1 > r2):
                right = mid  - 1
            else:
                left = mid + 1



               
            
            
            