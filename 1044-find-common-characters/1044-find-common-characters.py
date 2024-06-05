class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = set(words[0])
        cc = Counter()
        for i in words:
            res &= set(list(i))
            temp  = Counter(i)
            for j in temp:
                if cc[j]:
                    cc[j] = min(cc[j], temp[j])
                else:
                    cc[j] = temp[j]
            
        final = []
        for i in res:
            final += [i] * cc[i]
        return final