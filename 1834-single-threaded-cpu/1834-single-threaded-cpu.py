class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        Heap = []
        res = []
        num  = []
        for i in range(len(tasks)):
            num.append((tasks[i][0], tasks[i][1], i))
        num.sort()
        i = 0
        time = num[0][0]
        while i <len(num) or Heap:
            while i <len(num) and num[i][0] <= time:
                heappush(Heap, (num[i][1], num[i][2]))
                i += 1
            if not Heap:
                time = num[i][0]
            else:
                t, ind = heappop(Heap)
                time += t
                res.append(ind)
        return res