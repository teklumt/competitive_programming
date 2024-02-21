class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort(reverse=True)
        ans=deque()

        for i in deck:
            if len(ans)>0:
                ans.appendleft(ans.pop())
            ans.appendleft(i)
        return ans