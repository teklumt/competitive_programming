class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == '1':  
            return False
        
        can = [False] * len(s)
        can[0] = True
        maxx = 0
        for i in range(len(s)):
            if can[i]:
                start = max(i + minJump, maxx)
                end = min(i + maxJump, len(s) - 1)
                
                for j in range(start, end + 1):
                    if s[j] == '0':
                        can[j] = True
                
                maxx = max(maxx, end)
            if can[-1]:
                return True
        return False