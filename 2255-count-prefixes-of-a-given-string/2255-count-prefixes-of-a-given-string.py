class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for i in words:
            m=s.find(i)
            if m==0:
                count+=1
        return count