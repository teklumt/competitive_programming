class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for n in range(len(words)-1):
            for k in range(n+1, len(words)):
                i = (list(set(words[n])))
                i.sort()
                j = (list(set(words[k])))
                j.sort()
                if "".join(i) == "".join(j):
                    count += 1
        return count