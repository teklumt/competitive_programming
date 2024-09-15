class Trie:
    def __init__(self):
        self.root  = {"#":0}

    def insert(self, pattern):
        cur = self.root
        for i in pattern:
            if i not in cur:
                cur[i] = {"#" : 0}
            cur = cur[i]
        cur["#"] = 1
        
    def match(self, given):
        cur = self.root
        i = 0
        while i < len(given):
            
            curChar = given[i]
            if curChar.isupper():
                if curChar not in cur:
                    return False
                cur = cur[curChar]

            elif curChar in cur:
                cur = cur[curChar]
            i += 1
        return cur["#"] == 1

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        tri = Trie()
        tri.insert(pattern)
        res = []
        for i in queries:
            res.append(tri.match(i))
        return res