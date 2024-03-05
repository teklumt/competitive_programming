class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        my_dict={
            "2":{'a','b','c'},"3":{'d','e','f'},"4":{'g','h','i'},"5":{'j','k','l'}
            ,"6":{'m','n','o'},"7":{'p','q','r','s'},"8":{'t','u','v'},
            "9":{'w','x','y','z'}
        }

        res , temp = [], []

        def backtrack(i):
            if len(temp) == len(digits):
                res.append("".join(temp.copy()))
                return 
            
            for j in my_dict[digits[i]]:
                temp.append(j)
                backtrack(i + 1)
                temp.pop()
        backtrack(0)
        return res