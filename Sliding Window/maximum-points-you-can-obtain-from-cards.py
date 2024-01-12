class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints)==k:
            return sum(cardPoints)
        summ=sum(cardPoints)
        left=0
        right=len(cardPoints)-k
        window=0
        for i in range(right):
            window+=cardPoints[i]
        res=summ-window
        for i in range(right,len(cardPoints)):
            window+=cardPoints[i]
            window-=cardPoints[left]
            res=max(res,summ-window)
            left+=1
        return res