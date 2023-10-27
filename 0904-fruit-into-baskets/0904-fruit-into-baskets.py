class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        store={}
        res=0
        for i in range(len(fruits)):
            if len(store)<2:
                store[fruits[i]]=store.get(fruits[i],0)+1
            elif len(store)==2:

                if fruits[i] in store:
                    store[fruits[i]]+=1
                else:
                    k=i-1
                    count=0
                    while k>=0:
                        if fruits[i-1]==fruits[k]:
                            count+=1
                            k-=1
                        else:
                            break

                    store={fruits[i-1]:count}
                    store[fruits[i]]=1
                    
            res=max(res,sum(store.values()))
        return res