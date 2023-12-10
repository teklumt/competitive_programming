class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_hash = {}
        odds = []
        evens = 0

        for i in s:
            count_hash[i] = count_hash.get(i,0) + 1
        
        for i in count_hash:
            
            if count_hash[i]%2==0:
                evens+=count_hash[i]
            
            else:
                odds.append(count_hash[i])
        
        odds.sort()

        for i in range(len(odds)-1,-1,-1):

            if i == len(odds)-1:
                evens += odds[i]
            
            else:

                evens += odds[i]-1
        return evens
        

        

        