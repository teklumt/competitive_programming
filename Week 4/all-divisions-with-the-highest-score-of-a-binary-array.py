class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        zero_count=[0]
        one_count=[0]
        hash=defaultdict(list)
        
        for i in range(len(nums)):
            if nums[i]==0:
                zero_count.append(zero_count[-1]+1)
            else:
                zero_count.append(zero_count[-1])
                
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==1:
                one_count.append(one_count[-1]+1)
            else:
                one_count.append(one_count[-1])
                
        one_count.reverse()
        
        for i in range(len(zero_count)):
            key=zero_count[i] + one_count[i]
            hash[key].append(i)
            
        res=[]
        for i in hash:
            res.append([i,hash[i]])
        res.sort()
        
        return res[-1][1]

