class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res=[]
        hash={}
        final=[]
        for pa in paths:
            num=pa.split(" ")
            for i in range(1,len(num)):
                res.append(num[0]+'/'+num[i])
        for i in res:
            num=i.split('(')
            hash[num[-1]]=hash.get(num[-1],[])+[num[0]]
        for i in hash:
            if len(hash[i])>1:
                final.append(hash[i])
        return final
