class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        result=[]
        red=[]
        for n in range(len(words)):
            check=[]
            count=1
            if words[n] in red:
                continue
            else:
                check.append(words[n])
                red.append(words[n])
                for m in range(n+1,len(words)):
                        if words[m] in check:
                            count+=1
                check.append(count)
                result.append(check)
        result.sort()
        for n in result:
            n.reverse()
        result.sort()
        for n in range(len(result)):
            for m in range(n+1,len(result)):
                if result[n][0]==result[m][0]:
                    if result[n][1]<result[m][1]:
                            result[n],result[m]=result[m],result[n]     
        final=[]
        for m in range(k):
            final.append(result[-1-m][1])
        return final