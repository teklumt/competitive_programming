class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        reserve=[]
        for i in timeSeries:
            reserve.append([i,i+duration-1])
        reserve.sort()
        new_list=[reserve[0]]
        for i in range(1,len(reserve)):
            if new_list[-1][1]>=reserve[i][0]:
                new_list[-1][1]=max(new_list[-1][1],reserve[i][1])
               
            else:
                new_list.append(reserve[i])
        res=0
        for i in new_list:
            res+=(i[1]-i[0]+1)
        return res 