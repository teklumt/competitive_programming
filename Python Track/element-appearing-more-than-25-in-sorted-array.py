class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        target=len(arr)//4

        hash={}

        for i in arr:

            hash[i] = hash.get(i,0)+1

        for i in hash:
            if hash[i]>target:
                return i