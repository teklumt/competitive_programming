class Solution:
    def checkString(self, s: str) -> bool:
        b = -1
        for i in range(len(s)):
            if s[i] == "b":
                b = i
            elif b != -1:
                return False
        return True
        