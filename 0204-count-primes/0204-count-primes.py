class Solution:
    def countPrimes(self, n: int) -> int:         
            prime = [True] * (n + 1)
            prime[0] = False
            if len(prime) > 1:
                prime[1] = False
            prime[-1] = False
            i = 0
            while i < n:
                if prime[i]:
                    m = i * i
                    while m < n:
                        prime[m] = False
                        m += i
                i += 1
            
            return sum(prime)
                    
                    
                