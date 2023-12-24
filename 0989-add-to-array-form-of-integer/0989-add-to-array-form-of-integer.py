class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        str_num=0
        for i in num:
            str_num=str_num*10 + i
        
        str_num+=k
        res=[]
        while str_num>0:
            res.append(str_num%10)
            str_num//=10

        return res[::-1]