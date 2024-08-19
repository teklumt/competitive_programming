class Solution:
    def minimumPushes(self, word: str) -> int:
        capa = {1:8, 2:8, 3:8, 4:2}
        count = Counter(list(word))
        

        ans = [[count[i], i] for i in count]
        ans.sort(reverse=True)
 
        res = 0
        cc = 1
        for i, j in ans:
            res +=  i * cc
            capa[cc] -= 1
        
            if capa[cc] == 0: cc += 1
        return res
            


