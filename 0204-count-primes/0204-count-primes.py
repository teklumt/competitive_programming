class Solution:
    def countPrimes(self, n: int) -> int:         
            find = [True] * (n + 1)
            find[0] = False
            if len(find) > 1:
                find[1] = False
            find[-1] = False
            i = 0
            while i < n:
                if find[i]:
                    m = i * i
                    while m < n:
                        find[m] = False
                        m += i
                i += 1
            
            return sum(find)
                    
                    
                