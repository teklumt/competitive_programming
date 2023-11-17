class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]
        maxx=arr[-1]
        for i in range(len(arr)-1,-1,-1):
            maxx=max(maxx,arr[i])
            res.append(maxx)
        res.pop()
        return res[::-1]