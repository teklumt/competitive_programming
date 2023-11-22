class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        store1={}
        store2={}
        list1=s.split()
        for i in range(len(pattern)):
            store1[pattern[i]]=store1.get(pattern[i],"")+str(i)
        for i in range(len(list1)):
            store2[list1[i]]=store2.get(list1[i],"")+str(i)
        if len(store1)!=len(store2):
            return False
        return "".join(store1.values())=="".join(store2.values())