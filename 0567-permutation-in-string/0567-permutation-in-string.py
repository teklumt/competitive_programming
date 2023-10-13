class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        check=[]
        size=len(s1)
        for i in range(size):
            check.append(s2[i])
        new=check.copy()
        new.sort()
        new2=list(s1)
        new2.sort()
        if new==new2:
            return True
        for j in range(size,len(s2)):
            check.append(s2[j])
            del check[0]
            new=check.copy()
            new.sort()
            if new==new2:
                return True
        return False
