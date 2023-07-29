class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myhash=defaultdict(list)
        result=[]
        for i in strs:
            mykey=sorted(i)
            myhash[tuple(mykey)].append(i)
        for val in myhash.values():
            result.append(val)
        return result