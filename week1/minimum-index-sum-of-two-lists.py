class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    res.append([i+j,list1[i]])
        res.sort()
        final={}
        for i in res:
            final[i[0]]=final.get(i[0],[])+[i[1]]
        for i in final:
            return final[i]