class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        s1=inf
        s2=inf
        for i in nums:
            if i>s2:
                return True
            if i<=s1:
                s1=i
            else:
                s2=i
        return False





