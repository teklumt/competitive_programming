class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        one_place=[]
        res=[]
        for i in range(len(boxes)):
            if boxes[i]=='1':
                one_place.append(i)
        for i in range(len(boxes)):
            nn=0
            for j in one_place:
                nn+=abs(j-i)
            res.append(nn)
        return res