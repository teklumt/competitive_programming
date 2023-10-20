class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        m = list(p)
        n = list(s)
        m.sort()
        m = "".join(m)
        k = len(p)
        for i in range(len(n)+1-k):
            g = n[i:i+k]
            g.sort()
            g = "".join(g)
            if g == m:
                result.append(i)
        return result
