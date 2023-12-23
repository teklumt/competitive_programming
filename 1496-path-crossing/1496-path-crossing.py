class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur=[0,0]
        myset=set()
        myset.add(tuple(cur))

        for i in path:
            if i =="E":
                cur[0]+=1
                if tuple(cur) in myset:
                    return True
                myset.add(tuple(cur))
            elif i=='W':
                cur[0]-=1
    
                if tuple(cur) in myset:
                    return True
                myset.add(tuple(cur))
            elif i=='N':
                cur[1]+=1
    
                if tuple(cur) in myset:
                    return True
                myset.add(tuple(cur))
            elif i=='S':
                cur[1]-=1
                
                if tuple(cur) in myset:
                    return True
                myset.add(tuple(cur))
        return False





