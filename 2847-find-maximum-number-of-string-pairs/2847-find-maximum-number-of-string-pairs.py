class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        seen = set()
        for i in range(len(words)):
            if i not in seen:
                for j in range(len(words)):
                    if i != j and words[i] == words[j][::-1] and j not in seen:
                        res += 1
                        seen.add(i)
                        break
        return res


