class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = 0
        sum = 0
        while n != 0:
            n = n-1
            sum += digits[i]*(10**n)
            i = i+1
        sum += 1
        n = int(math.log10(sum))
        i = 0
        result = []
        while n >= 0:

            b = sum//(10**n)
            result.append(b)
            sum = sum-(b*(10**n))
            n -= 1

        return result