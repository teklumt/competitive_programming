class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        my_dict={
            "2":{'a','b','c'},"3":{'d','e','f'},"4":{'g','h','i'},"5":{'j','k','l'}
            ,"6":{'m','n','o'},"7":{'p','q','r','s'},"8":{'t','u','v'},
            "9":{'w','x','y','z'}
        }
        result=[]
        for n in digits:
                result.append(list(my_dict.get(n)))
        if len(result)==1:
            return result[0]
        final=[]
        if len(result)==2:
            for n in result[0]:
                    for m in range(1,len(result)):
                            for k in result[m]:
                                    t=n+k
                                    final.append(t)
            return final  
        if len(result)==3:
            for n in result[0]:
                for m in result[1]:
                    for k in result[2]:
                        t=n+m+k
                        final.append(t)
            return final
        if len(result)==4:
            for n in result[0]:
                for m in result[1]:
                    for k in result[2]:
                        for  j in result[3]:
                            t=n+m+k+j
                            final.append(t)
            return final