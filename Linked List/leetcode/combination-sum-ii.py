class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res =[]
        seen = set()
        def back(i, path, tar):
            if tar  == 0:
                num = tuple(path[::])
                if  num not in seen:
                    res.append(path[::])
                    seen.add(num)
                    return
            j = i
            
            while   j < len(candidates):
                if tar - candidates[j] >= 0:
                    path.append(candidates[j])
                    back(j+1, path, tar-candidates[j])
                    path.pop()
                    while j+1 <len(candidates) and candidates[j]==candidates[j+1]:
                        j+=1

                j+=1
                    

                # else:
                #     return

        back(0,[],target)
        return res



