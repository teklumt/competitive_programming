class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList)==0 or len(secondList)==0:
            return []
        first=0
        second=0
        res=[]
        while first<len(firstList) and second<len(secondList):
            temp=[]
            if firstList[first][1]<=secondList[second][1]:
                if firstList[first][1]>=secondList[second][0]:
                    temp=[max(firstList[first][0],secondList[second][0]),min(secondList[second][1],firstList[first][1])]
                    if firstList[first][1]==secondList[second][1]:
                        first+=1
                        second+=1
                    elif firstList[first][1] < secondList[second][1]:
                        first+=1
                    else:
                        second+=1
                else:
                    first+=1

            elif firstList[first][1]>=secondList[second][1]:
                if firstList[first][0]<=secondList[second][1]:
                    temp=[max(firstList[first][0],secondList[second][0]),min(secondList[second][1],firstList[first][1])]

                    # temp=[firstList[first][0],secondList[second][1]]
                    if firstList[first][1]==secondList[second][1]:
                        first+=1
                        second+=1
                    elif firstList[first][1] > secondList[second][1]:
                        second+=1
                    else:
                        first+=1
                else:
                    second+=1
            else:
                if first<second:
                    first+=1
                elif second<first:
                    second+=1
                else:
                    first+=1
                    second+=1
            if temp:
                res.append(temp)
        return res