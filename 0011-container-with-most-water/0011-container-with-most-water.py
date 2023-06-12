class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        m = len(height)-1
        n = 0
        while n < m:
            area = (m-n)*(min(height[m], height[n]))
            if area > result:
                result = area
            if height[n] < height[m]:
                n += 1
            elif height[n] > height[m]:
                m -= 1
            else:
                m = m-1
        return result