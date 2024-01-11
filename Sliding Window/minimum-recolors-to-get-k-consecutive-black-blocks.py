class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k>len(blocks):
            return 0
        store={'W':0,'B':0}
        for i in range(k):
            store[blocks[i]]+=1
        res=store['W']
        left=0
        for i in range(k,len(blocks)):
            store[blocks[i]]+=1
            store[blocks[left]]-=1
            res=min(res,store['W'])
            left+=1
        return res