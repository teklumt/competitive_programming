class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        def check(fruits):
            Hash=defaultdict(int)
            i=0
            j=0
            res=0
            while i<len(fruits):
                Hash[fruits[i]]+=1
                while len(Hash)>2:
                    Hash[fruits[j]]-=1
                    if Hash[fruits[j]]==0:
                        del Hash[fruits[j]]
                    j+=1
                res=max(res,i-j+1)
                i+=1
            # res=max(res,i-j+1)
            return res

        return check(fruits)
