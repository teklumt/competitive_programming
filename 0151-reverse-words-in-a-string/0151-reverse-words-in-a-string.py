class Solution:
    def reverseWords(self, s: str) -> str:
        g=s.split()
        g.reverse()
        g=" ".join(g)
        return f"{g}"
