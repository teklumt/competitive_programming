class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2 : return 1
        
        t1 = 0
        t2 = 1
        t3 = 1
        m = 2
        while m < n:
            temp = t1 + t2 + t3
            t1 = t2
            t2 = t3
            t3 = temp
            m += 1
        return t3
        