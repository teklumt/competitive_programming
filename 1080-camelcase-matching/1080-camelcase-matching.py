class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for i in queries:
            l = 0
            bol = True
            for j in range(len(i)):
                if  l < len(pattern) and pattern[l] == i[j] :
                    l += 1
                elif ord(i[j]) < 97:
                    res.append(False)
                    bol = False
                    break
                # if l == len(pattern):break
            if bol:
                if l == len(pattern):
                    res.append(True)
                else:
                    res.append(False)

        return res
            