class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result=[]
        red=[]
        for n in range(len(nums1)):
            if nums1[n] not in nums2:
                if nums1[n] not in red:
                    red.append(nums1[n])
        result.append(red)
        red=[]
        for n in range(len(nums2)):
            if nums2[n] not in nums1:
                if nums2[n] not in red:
                    red.append(nums2[n])
        result.append(red)

        return result