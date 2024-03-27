class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1: return False
        count = Counter(deck)
        num = count.values()
        minn = min(num)
        odd = []
        even = []
        for i in num:
            if i % 2:
                odd.append(i)
            else:
                even.append(i)
        if odd:
            n = gcd(*odd)
            if  n == 1 or min(odd) == 1:
                return False
            for i in even:
                if i % n:
                    return False
        return True

            

   
        