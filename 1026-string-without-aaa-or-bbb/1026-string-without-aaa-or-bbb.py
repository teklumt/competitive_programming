class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
   
        ac, bc = 0 , 0

        while a or b:
            if (a > b and  ac < 2) or bc == 2:
                res.append('a')
                a -= 1
                ac += 1
                bc = 0
            else:
                res.append('b')
                b -= 1
                bc += 1
                ac = 0
        return "".join(res)
            