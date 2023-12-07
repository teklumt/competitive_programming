class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)
        spac=set(spaces)
        result = []
        for i in range(len(s)):
            if i in spac:
                result.append(" ")
            result.append(s[i])
        return "".join(result)