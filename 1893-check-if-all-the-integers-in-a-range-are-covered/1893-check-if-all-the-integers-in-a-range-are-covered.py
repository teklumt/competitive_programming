class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        hash={}
        for rang in ranges:
            for i in range(rang[0],rang[1]+1):
                hash[i]='p'
        for i in range(left,right+1):
            if i not in hash:
                return False
        return True
