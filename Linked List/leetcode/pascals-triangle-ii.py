class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def pascal(n):
            if n==0:
                return [1]
            if n==1:
                return [1,1]
            val=pascal(n-1)
            temp=[1]
            for i in range(len(val)-1):
                temp.append(val[i]+val[i+1])
            temp.append(1)
            val=temp.copy()
            return val
        return pascal(rowIndex)

