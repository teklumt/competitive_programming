class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        tar = 1
        while time:
            if tar == n: dir = 0
            elif tar == 1: dir = 1

            if not dir: tar -= 1
            else: tar += 1
            time -= 1
        return tar
