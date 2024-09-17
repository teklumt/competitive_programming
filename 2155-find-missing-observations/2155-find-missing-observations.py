class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        summ = sum(rolls)
        target = (len(rolls) + n) * mean - summ
        maxx = target / n
        mod = target % n
        flag = maxx != int(maxx)
        maxx = ceil(maxx)
        if  maxx > 6 or (flag and not (maxx - 1)) or (target < 0):
            return []
  
        return ([maxx] * mod + [maxx - 1] * (n - mod)) if flag else  [maxx] * n 

       