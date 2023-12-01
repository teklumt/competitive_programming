class Solution:
    def romanToInt(self, s: str) -> int:
        result=0
        store=[]
        dic={
            "I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"IV":4,"IX":9,
            "XL":40,"XC":90,"CD":400,"CM":900
        }
        check=["IV","IX","XL","XC","CD","CM"]
        ori=["I","V","X","L","C","D","M"]
        for n in range(0,len(s)):
            if n in store:
                continue
            elif s[n:n+2] in check:
                result=result+ dic.get(s[n:n+2])
                store.append(n+1)        
            elif s[n] in ori:
                result=result+dic.get(s[n])
        return result
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
