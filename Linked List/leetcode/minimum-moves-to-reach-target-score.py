class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        while target>1:
            if maxDoubles > 0:
                if target %2==0:
                    count+=1
                    target//=2
                    maxDoubles-=1
                else:
                    count+=1
                    target-=1
            else:
                count+=target-1
                target=1
        return count