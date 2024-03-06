class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = sorted(set(houses))
        heaters = list(set(heaters))
        newTemp = []
        
        for i in heaters:
            
            newTemp.append(i-1)
        newTemp.sort()
        res = -inf
        m = 0
        for i in houses:
            cc = 0
            for j in range(m,len(newTemp)):
                if i - 1 == newTemp[j]:
                    res = max(res, 0)
                    cc = j
                    break
                elif i - 1  < newTemp[j]:
                    if j == 0:
                        res = max(res, newTemp[j] - (i - 1))
                        cc = j
                        break
                    else:
                        re1 = ((newTemp[j] - (i - 1)))
                        re2 = ((- newTemp[j-1] + (i - 1)))
                        res = max(res, min(re1, re2))
                        cc = j
                        break
                elif j == len(newTemp) - 1:
                    re1 = (i - 1) - (newTemp[j])
                    res = max(res,re1)
                    cc = j
                    break
                cc = j
            m=j                
        return res