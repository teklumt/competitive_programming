class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res=0
        n=len(plants)
        mm=capacity
        for i in range(n):
            if plants[i]<=mm:
                res+=1
                mm-=plants[i]
            else:
                res+=i+i+1
                mm=capacity
                mm-=plants[i]
                
        return res