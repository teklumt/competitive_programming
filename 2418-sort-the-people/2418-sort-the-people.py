class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result=[]
        for i in range(len(heights)):
            result.append([heights[i],i])
        result.sort()
        result.reverse()
        final=[]

        for i in result:
            final.append(names[i[1]])
        return final
