class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        res = [-1]*len(intervals)

        num = sorted([i[0] for i in intervals])
        hashT = {}
        for i in range(len(intervals)):
            hashT[intervals[i][0]] = i

        for i in range(len(intervals)):
            ind = bisect_left(num, intervals[i][1])
            if ind < len(intervals):
                res[i] = hashT[num[ind]]
        return res

            