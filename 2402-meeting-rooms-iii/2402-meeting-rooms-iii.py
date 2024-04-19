class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        res = [0] * n
        
        Heap = []
        free = [i for i in range(n - 1, -1, -1)]
        heapify(free)
        meetings.sort()
        for start, end in meetings:
            if Heap:
                while  Heap and Heap[0][0] <= start:
                    curend, ind = heappop(Heap)
                    heappush(free, ind)
                if not free:
                    curend,  ind  = heappop(Heap)
                    res[ind] += 1
                    heappush(Heap, (curend + end - start,  ind))
                else:
                    ind = heappop(free)
                    res[ind] += 1
                    heappush(Heap, (end, ind))
            else:
                ind = heappop(free)
                res[ind] += 1
                heappush(Heap, ( end, ind))

        return res.index(max(res))


