class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=len(nums1)-1
        if len(nums1)>len(nums2):
            i=len(nums2)-1
        j=len(nums2)-1
        res=0
        while i<=j and i>=0 and j>=0:
            if nums1[i]<=nums2[j]:
                res=max(res,j-i)
                i-=1
            else:
                j-=1
                if i>j and i>0:
                    i-=1
              
        return res