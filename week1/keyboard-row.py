class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        n = set(list("qwertyuiop"))
        m = set(list("asdfghjkl"))
        o = set(list("zxcvbnm"))
        store = [n, m, o]
        res = []
        for i in words:
            k=i.lower()
            m = set(list(k))
            for j in store:
               
                nn = j.intersection(m)
                if sorted(nn) == sorted(m):
                    res.append(i)
                    break
        return res