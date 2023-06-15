class Solution:
    def frequencySort(self, s: str) -> str:
        new = list(s)
        result = []
        for m in set(new):
            result.append([s.count(m), m])
        result.sort()
        final = ""
        for m in range(len(result)-1, -1, -1):
            final += "".join([result[m][1]]*result[m][0])
        return final