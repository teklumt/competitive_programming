class Solution:
    def totalMoney(self, n: int) -> int:
        quotient = n//7
        remainder = n % 7
        if n <= 7:
            total_money = quotient*28 + (remainder*(remainder+1))//2
        else:
            total_money = quotient*28 + (remainder*(remainder+1))//2 + (
                ((quotient-1) * quotient)//2)*7 + quotient * remainder
        
        return total_money
                