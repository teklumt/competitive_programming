class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for n in words:
            bol = True
            for k in set(n):
                if k not in allowed:
                    bol = False
                    break
            if bol == True:
                count += 1
        return count