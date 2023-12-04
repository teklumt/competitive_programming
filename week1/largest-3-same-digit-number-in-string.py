class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=[]
        chack=[]
        for i in range(len(num)):
            if chack:
                if len(chack)<3:
                    if num[i]==chack[-1]:
                        chack.append(num[i])
                    else:
                        chack=[num[i]]
                else:
                    res.append("".join(chack))
                    chack=[num[i]]
            else:
                chack.append(num[i])
        if len(chack)==3:
            res.append("".join(chack))
        res.sort()
        return res[-1] if res else ""

        