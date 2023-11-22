class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        store1={}
        store2={}
        for i in range(len(s)):
            store1[s[i]]=store1.get(s[i],"")+str(i)
        for i in range(len(t)):
            store2[t[i]]=store2.get(t[i],"")+str(i)
        if len(store1)!=len(store2):
            return False
        return "".join(store1.values())=="".join(store2.values())