class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        store = {}
        flag = 0
        for i in passengers:
            store[i] = 1
        res = []
        buses.sort()
        passengers.sort()
        queue = collections.deque(passengers)

        for i in range(len(buses)):
            k = capacity
            while queue and queue[0] <= buses[i] and k > 0:
                m = queue.popleft()
                if i+1 == len(buses)-1:
                    flag = m
                if i == len(buses)-1:
                    res.append(m)
                k -= 1

        if len(res) == 0:
            return  buses[-1]
        elif len(res) < capacity:
            pp=-1
            for i in range(res[-1]+1, buses[-1]+1):
                    if i not in store:
                        pp = max(pp, i)
                    else:
                        break
            if pp != -1:
                return pp
            else:
                for i in range(res[-1]-1, 0, -1):
                    if i not in store:
                        return i
                        break
        else:
                if len(res) == 1:
                    
                    for i in range(res[-1]-1,0,-1):
                        if i not in store:
                            return i
                else:
                    p = res[-2]
                    pp = -1

                    for i in range(p+1, buses[-1]+1):
                        if i not in store:
                            pp = max(pp, i)
                        else:
                            break
                    if pp != -1:
                        return pp
                    else:
                        for i in range(p-1, 0, -1):
                            if i not in store:
                                return i
                                break