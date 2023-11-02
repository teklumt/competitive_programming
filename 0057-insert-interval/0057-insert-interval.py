class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n=len(intervals)
        new=[intervals[0]]
        for m in range(1,n):
            
            if new[-1][1]>=intervals[m][0]:
                new[-1][1]=max(new[-1][1],intervals[m][1])
            else:
                new.append(intervals[m])
        return new