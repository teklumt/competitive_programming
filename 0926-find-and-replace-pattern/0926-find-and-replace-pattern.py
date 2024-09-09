class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def func(arr):
            ans = defaultdict(list)        
            for i in range(len(arr)):
                ans[arr[i]].append(i)
            sorted_ans = sorted(ans.items(), key=lambda x: len(x[1]), reverse=True)
            return sorted_ans
        check = func( pattern)
        res = []
        for i in words:
            new_ = func(i)
            if len(new_) == len(check):
                bol = True 
                for j in range(len(check)):
                    if check[j][1] != new_[j][1]:
                        bol = False
                        break
                if bol:   
                    res.append(i)
        return  res