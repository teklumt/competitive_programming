class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result=nums1[:]+nums2[:]
        result.sort()
        print(result)
        if len(result)%2!=0:
            return result[len(result)//2]
        else:
            return (result[len(result)//2]+result[(len(result)//2)-1])/2