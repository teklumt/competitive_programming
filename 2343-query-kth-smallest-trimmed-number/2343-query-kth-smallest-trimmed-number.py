class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        final=[]
        store=[]
        for i in range(len(queries)):
            store.append([queries[i][1],queries[i][0],i])
        for i in store:
            rem=[]
            for j in range(len(nums)):
                rem.append([nums[j][-i[0]:],j])
            rem.sort()
            final.append(rem[i[1]-1][1])
        return final