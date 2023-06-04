class Solution:
    def isValid(self, s: str) -> bool:
        n=[]
        def valid(expr):
            left="({["
            right=")}]"
            for c in expr:
                if c in left:
                    n.append(c)
                elif c in right:
                    if len(n)==0:
                        return False
                    if right.index(c)!=left.index(n.pop()):
                        return False
            return len(n)==0
        return valid(s)