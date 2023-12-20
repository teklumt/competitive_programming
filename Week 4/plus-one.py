class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num=""
        
        for i in digits:
            str_num+=str(i)
        
        res=str(int(str_num)+1)

        return [int(i) for i in res]

