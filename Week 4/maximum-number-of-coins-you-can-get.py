class Solution:
    def maxCoins(self, piles: List[int]) -> int: 
        
        piles.sort()
        bob=0
        me=len(piles)-2
        res=0
        
        while bob<me:
            
            res+=piles[me]
            me-=2
            bob+=1
        return res