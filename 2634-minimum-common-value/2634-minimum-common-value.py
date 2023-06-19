class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        bom=(list(set(nums1) & set(nums2)))
        bom.sort()
        if len(bom)==0:
            return -1
        return bom[0]