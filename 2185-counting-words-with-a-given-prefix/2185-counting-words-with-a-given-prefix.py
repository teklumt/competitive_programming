class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for i in words:
            m=i.find(pref)
            if m==0:
                count+=1
        return count
        