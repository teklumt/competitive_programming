class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        nums_backs=Counter(backs)
        nums_fronts=Counter(fronts)

        ind_front={}
        ind_back={}

        summ=sum(nums_backs.values())

        for i in range(len(fronts)):
            ind_front[fronts[i]] = ind_front.get(fronts[i],[])+[i]
            ind_back[backs[i]] = ind_back.get(backs[i],[])+[i]


        Sorted_fronts = dict(sorted(nums_fronts.items()))
        Sorted_backs = dict(sorted(nums_backs.items()))
        res=[]
        for i in Sorted_fronts:
            if i not in nums_backs:
                res.append(i)
            elif set(ind_front[i]) & set(ind_back[i])==set():
                    res.append(i)
        
        for i in Sorted_backs:
            if i not in nums_fronts:
                res.append(i)
            elif set(ind_front[i]) & set(ind_back[i])==set():
                    res.append(i)
        return min(res) if res else 0
        