class Solution:
    def minOperations(self, s: str) -> int:
        
        count1=0
        count2=0
        comp1="01"*((len(s)//2)+1)
        comp2="10"*((len(s)//2)+1)
        
        for i in range(len(s)):
            if s[i]!=comp1[i]:
                count1+=1
            if s[i]!=comp2[i]:
                count2+=1
        return min(count1,count2)