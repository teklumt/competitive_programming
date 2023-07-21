class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        num = [[1], [1, 1], [1, 2, 1]]
        if rowIndex < 3:
            return num[rowIndex]
        else:
            while len(num)-1 < rowIndex:
                ori = [num[-1][0]]
                for i in range(len(num[-1])-1):
                    ori.append((num[-1][i]+num[-1][i+1]))
                ori.append(num[-1][-1])
                num.append(ori)
            return num[rowIndex]
        