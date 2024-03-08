class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        place = []
        for i in range(len(s)):
            if s[i] == '|':
                place.append(i)
        prefix = [0]
        left = 0
        cc = s.count('|') 

        for i in s:
            if i != '|':
                if cc > 0 and left > 0:
                    prefix.append(prefix[-1] + 1)
                else:
                    prefix.append(prefix[-1])
            else:
                    cc -= 1
                    left += 1
                    prefix.append(prefix[-1])
        res = []
        for i in queries:
            ind1 = bisect_left(place, i[0])
            ind2 = bisect_left(place, i[1])
            if ind2 >=len(place): ind2 -= 1
            if ind1 >=len(place): ind1 -= 1
            if ind1 < 0 or ind2 < 0:
                res.append(0)
                continue
            
            if i[0] > place[ind1] and ind1 < len(place) - 1:
                ind1 += 1
            if i[1] < place[ind2]:
                ind2 -= 1
            if ind1 < 0 or ind2 < 0:
                res.append(0)
                continue
            if place[ind1]>=place[ind2] :
                res.append(0)
                continue

            res.append(prefix[place[ind2]] - prefix[place[ind1]])
        return res

