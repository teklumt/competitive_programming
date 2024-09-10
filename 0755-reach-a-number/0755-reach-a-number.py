class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        res = 0
        count = 1
        while True:
            res += count
            if res >= target and (res - target) % 2 == 0:
                return count 
            count += 1