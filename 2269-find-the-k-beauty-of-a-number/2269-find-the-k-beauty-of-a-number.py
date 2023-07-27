class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        result = 0
        num2 = list(str(num))
        n = num2[:k]
        nn = "".join(n)
        if int(nn) != 0 and num % int(nn) == 0:
            result += 1
        for i in range(k, len(num2)):
            n.append(num2[i])
            del n[0]
            nn = "".join(n)
            if int(nn) != 0 and num % int(nn) == 0:
                result += 1
        return result