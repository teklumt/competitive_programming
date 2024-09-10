class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:return True
        for i in range((num // 2) , num):
            sec = num - i
            two = int(str(i)[::-1])
            if sec >= 0 and two >= 0 and sec == two:
                return True
        return False
            