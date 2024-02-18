class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        stack=[]
        for i in points:
            if stack:
                if i[0] > stack[-1][1]:
                    stack.append(i)
                else:
                    num=stack.pop()
                    stack.append([min(num[0],i[0]),min(num[1],i[1])])           
            else:
                stack.append(i)
        return len(stack)