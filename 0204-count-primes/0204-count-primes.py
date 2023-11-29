class Solution:
    def countPrimes(self, n: int) -> int:
            prime = [True for i in range(n)] 
            p = 2
            while (p * p <= n): 
        
                
                if (prime[p] == True): 
        
                    
                    for i in range(p * p, n, p): 
                        prime[i] = False
                p += 1
        
           
            res=0
            for p in range(2, n): 
                    if prime[p]: 
                        res+=1
            return res