class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        num = sorted([a, b , c])
        
        if num[1] < num[2]:

            nn = num[2] - num[1]

            if nn >= num[0]:
                return num[1] + num[0]
            else:
                return num[2] + (num[0] - nn)//2
        return num[2] + (num[0])//2
