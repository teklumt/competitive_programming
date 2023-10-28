class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[height[0]]*n
        max_right=[height[-1]]*n
        res=0
        for i in range(1,n):
            max_left[i]=max(max_left[i-1],height[i])
            max_right[n-i-1]=max(max_right[n-i],height[n-i-1])
        for i in range(n):
            res+=min(max_left[i],max_right[i])-height[i]
        return res
        
