class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        cc = 1
        Map = {}
        for i in sorted(score, reverse = True):
            if cc == 1:
                Map[i] = "Gold Medal"
            elif cc == 2:
                Map[i] = "Silver Medal"
            elif cc == 3:
                Map[i] = "Bronze Medal"
            else:
                Map[i] = f"{cc}"
            cc += 1
        return [Map[i] for i in score]
                
            
        