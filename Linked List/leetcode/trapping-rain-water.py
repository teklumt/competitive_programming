class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]
        res=0
        for i in range(len(height)):
            temp=0
            while stack and stack[-1][1]<=height[i]:
                index,num=stack.pop()
                res+=(i-index-1)*min(num,height[i]) - temp*(i-index-1)
                temp=num
            if stack:
                index=stack[-1][0]
                res+=(i-index-1)*height[i] - temp*(i-index-1)
            stack.append([i,height[i]])
            
        return res 

