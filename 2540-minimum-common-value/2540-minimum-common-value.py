class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        return sorted((list(set(nums1) & set(nums2))))[0] if len((list(set(nums1) & set(nums2))))!=0   else -1
    
    
    
    
    
    
    
    
    
    
    
    
    
        # bom=(list(set(nums1) & set(nums2)))
        # bom.sort()
        # if len(bom)==0:
        #     return -1
        # return bom[0]