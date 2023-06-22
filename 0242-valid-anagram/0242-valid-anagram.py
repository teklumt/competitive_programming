class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bol=True
        if len(t)!=len(s):
            return False
        new1=(list(s))
        new2=(list(t))
        new1.sort()
        new2.sort()
        for n in range(len(new1)):
            if new1[n]!=new2[n]:
                bol=False
        return bol