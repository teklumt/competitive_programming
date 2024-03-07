class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        MinLeft = [-1]*len(heights)
        MinRight = [-1]*len(heights)
        stack = []
        stack2 = []
        res = -inf

        for  i, val in enumerate(heights):
            
            while stack and stack[-1][-1] > val:
                ind , num = stack.pop()
                MinRight[ind] = i 
            if stack:
                MinLeft [i] = stack[-1][0]
            stack.append([i, val])
        for i in range(len(MinLeft)):
            left  = MinLeft[i]
            right = MinRight[i]

            if MinLeft[i] == -1:
                left = 0
            else:
                left += 1
            if right == -1:
                right = len(heights) 
            res = max(res ,heights[i] * (right - left) )
            
                
        return res









