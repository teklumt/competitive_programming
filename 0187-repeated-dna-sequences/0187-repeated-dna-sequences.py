class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<=10:
            return []
        res=[]
        left=0
        r=""
        myhash={}
        for i in range(10):
            r+=s[i]
        myhash[r]=1 + myhash.get(r,0)
        for i in range(10,len(s)):
            r+=s[i]
            r=r[1:]
            myhash[r]=1 + myhash.get(r,0)
        result=[]
        for i in myhash:
            if myhash[i]>=2:
                result.append(i)
        return result
