class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n= set(nums1).intersection(set(nums2))
        if n:
            return min(n)
        else:
            return min(nums1[0],nums2[0])*10+max(nums1[0],nums2[0])