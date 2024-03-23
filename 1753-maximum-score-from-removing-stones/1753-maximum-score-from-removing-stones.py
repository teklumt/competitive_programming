class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        num = sorted([a, b , c])
        
        if num[1] < num[2]:

            offSet = num[2] - num[1]

            if offSet >= num[0]:
                return num[1] + num[0]
            else:
                return num[2] + (num[0] - offSet)//2
            
        return num[2] + (num[0])//2
