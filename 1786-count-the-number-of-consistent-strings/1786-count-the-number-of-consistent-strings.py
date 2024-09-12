class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check = set(list(allowed))
        res = 0
        for i in words:
            if check.intersection( set(list(i)))  == set(list(i)):
                res += 1
        return res