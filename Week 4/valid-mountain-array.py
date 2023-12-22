class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        bol=True
        
        up=0
        if len(arr)<3  or arr[::-1]==sorted(arr):
            return False

        for i in range(len(arr)-1):
            if arr[i]<arr[i+1]:
                pass
            elif arr[i]==arr[i+1]:
                return False
            else:
                up=i+1
                break
        
        for i in range(up,len(arr)-1,+1):
            if arr[i]>arr[i+1]:
                pass
            else:
                return False
        
        return True 
            