class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res=0
        for i in range(len(arr1)):
            bol=True
            for j in range(len(arr2)):
                if abs(arr2[j]-arr1[i])<=d:
                    bol=False
            if bol:
                res+=1
        return res