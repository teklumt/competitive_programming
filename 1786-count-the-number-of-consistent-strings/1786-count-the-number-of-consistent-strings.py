class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check = set(allowed)
        res = 0
        for i in words:
            if check.intersection(set(i)) == set(i):
                res += 1
        return res