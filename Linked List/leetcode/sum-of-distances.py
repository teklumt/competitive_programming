class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        store=defaultdict(list)

        for i in range(len(nums)):
            store[nums[i]].append(i)
        
        for  i in store:
            if len(store[i])!=1:
                preCount=0
                postCount=len(store[i])-1
                tof=list(accumulate(store[i],initial=0))
                tob=list(accumulate(store[i][::-1],initial=0))[::-1]
                
                for j in range(len(store[i])):
                    res= (preCount*store[i][j]  - tof[j]) + (tob[j+1] -  postCount*store[i][j])
                    preCount+=1
                    postCount-=1
                    result[store[i][j]]=res
        return result 