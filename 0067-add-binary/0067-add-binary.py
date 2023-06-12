class Solution:
    def addBinary(self, a: str, b: str) -> str:
        g=int(a,2) + int(b,2)
        g=bin(g)[2:]
        g=str(g)
        return g