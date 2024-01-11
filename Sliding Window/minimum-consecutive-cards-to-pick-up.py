class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res=len(cards)+5
        hash=defaultdict(int)
        for i in range(len(cards)):
            if cards[i] in hash:
                res=min(res,i-hash[cards[i]]+1)
            hash[cards[i]]=i
        return res if res!=len(cards)+5 else -1