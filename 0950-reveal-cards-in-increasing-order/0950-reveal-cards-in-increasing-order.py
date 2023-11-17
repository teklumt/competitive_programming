class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        deck.reverse()
        res=[]
        for i in deck:
            if len(res)>0:
                res.insert(0,res.pop())
            res.insert(0,i)
        return res