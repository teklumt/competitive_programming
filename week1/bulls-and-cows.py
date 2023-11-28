class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        num={}
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                num[i]=i
        for i in range(len(secret)):
            if secret[i]!=guess[i]:
                for j in range(len(secret)):
                    if secret[i]==guess[j] and j not in num:
                        cows+=1
                        num[j]=j
                        break
        return f"{bulls}A{cows}B" 
        