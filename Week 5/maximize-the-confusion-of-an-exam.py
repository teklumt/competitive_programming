class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        store={}
        left=0
        res=0
        for i in range(len(answerKey)):
            store[answerKey[i]]=store.get(answerKey[i],0)+1
            while sum(store.values())-max(store.values())>k:
                store[answerKey[left]]-=1
                left+=1
            res=max(res,sum(store.values()))
        return res