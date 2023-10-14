class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            a=-1
            for j in range(nums2.index(i),len(nums2)):
                if nums2[j]>i:
                    a=nums2[j]
                    break
            result.append(a)
        return result