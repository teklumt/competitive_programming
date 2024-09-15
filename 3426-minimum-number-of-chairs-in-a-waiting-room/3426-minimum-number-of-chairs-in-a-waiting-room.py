class Solution:
    def minimumChairs(self, s: str) -> int:
        temp = 0
        res = 0
        for i in s:
            if i == "E":
                if temp:temp -= 1
                else: 
                    res += 1
            else:
                if temp or res:
                    temp += 1
                else:
                    res += 1
                    temp += 1
        return res

