class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res1,res2=0,0
        count=0
        for i in range(len(arr)-1):
            if i%2==0:
                if arr[i]<arr[i+1]:
                    count+=1
                else:
                    count=0
            else:
                if arr[i]>arr[i+1]:
                    count+=1
                else:
                    count=0
            res1=max(res1,count)
        count=0
        for i in range(len(arr)-1):
            if i%2!=0:
                if arr[i]<arr[i+1]:
                    count+=1
                else:
                    count=0
            else:
                if arr[i]>arr[i+1]:
                    count+=1
                else:
                    count=0
            res2=max(res2,count)
        res=max(res1,res2)+1
        return res
        