class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        for n in set(list(words[0])):
            check = []
            check.append((list(words[0])).count(n))
            for m in range(1, len(words)):
                check.append((list(words[m])).count(n))
            w = [n]*min(check)
            result += w
        return result