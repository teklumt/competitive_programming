class Solution:
    def countEven(self, num: int) -> int:
        COUNT  = 0
        for i in range(1, num + 1):
            summ = 0
            for j in str(i):
                summ += int(j)
            if summ % 2 == 0:
                COUNT += 1
        return COUNT 
        