class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new=s.split()
        result=len(new[len(new)-1])
        return result