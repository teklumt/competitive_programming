class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        intial=deque([1,1])
        t=1
        while t < rowIndex:
            temp=deque()
            for i in range(len(intial)-1):
                temp.append(intial[i]+intial[i+1])
            temp.append(1)
            temp.appendleft(1)
            intial=temp.copy()
            t+=1
        return intial