class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        chear = [i for i in range(len(times))]
        times = sorted([(times[i][0], times[i][1], i) for i in range(len(times))])

        heap = []
        
        for i , j, k in times:
             
            while heap and heap[0][0] <= i:
                dest, ch = heappop(heap)
                heappush(chear, ch)
            if not chear:
                dest, ch = heappop(heap)
                if k == targetFriend:
                    return ch
                heappush(heap,(j, ch))
            else:
                ch = heappop(chear)
                if k == targetFriend:
                    return ch
                heappush(heap,(j, ch))
     
