class Solution:
    def freqAlphabets(self, s: str) -> str:
        res=""
        num=[]
        for i in s:
            if i!='#':
                num.append(i)
            else:
                if len(num)>2:
                    while len(num)>2:
                        res+=chr(96+int(num[0]))
                        del num[0]
                if len(num)==2:
                    res+=chr(96+int("".join(num)))
                    num=[]
        while num:
            res+=chr(96+int(num[0]))
            del num[0]
        return res
