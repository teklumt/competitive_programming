class Solution:
    def makeGood(self, s: str) -> str:
        res = []
 
        bol = True
        for i in s:
            if res and res[-1].isupper() != i.isupper() and res[-1].lower() == i.lower():
                res.pop()
            else:
                res.append(i)
                    
        return "".join(res)


