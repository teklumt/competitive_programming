class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        result = []
        for i in s1:
            if i not in s2:
                if s1.count(i)==1:
                    result.append(i)
        for i in s2:
            if i not in s1:
                if s2.count(i)==1:
                    result.append(i)
                
        return result