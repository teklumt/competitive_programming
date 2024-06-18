class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxxInd, maxxVal = [], []
        for ind, val in sorted(zip(difficulty, profit)):
            maxxInd.append(ind)
            if maxxVal:
                maxxVal.append(max(maxxVal[-1], val))
            else:
                maxxVal.append(val) 
        res = 0
        for i in worker:
            ind = bisect_right(maxxInd, i) - 1
            if ind >= 0:
                res += maxxVal[ind]
            
        return res
            
