class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ""
        for i in s:
            res += str(ord(i) - 96)

        while k:
            summ = 0
            for i in res:
                summ += int(i)
            res = f"{summ}"
            k -= 1
        return int(res)
            
            
        

