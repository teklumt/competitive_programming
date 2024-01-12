class Solution:
    def balancedString(self, s: str) -> int:
        def check(num1,num2):
            if len(num1)!=len(num2):
                return False
            for i in num2:
                if num2[i]<num1[i]:
                    return False
            return True

        count=Counter(s)
        Hash=Counter()
        n=len(s)//4
        for i in count:
            if count[i]>n:
                Hash[i]=count[i]-n
        print(Hash)
    
        j=0
        i=0
        minn=len(s)+1
        win=Counter()
        while i <len(s):
            if s[i] in Hash:
                win[s[i]]+=1
            if win==Hash and i-j+1<minn:
                minn=i-j+1
            while j<len(s) and check(Hash,win):
                if i-j+1<minn:
                    minn=i-j+1
                if s[j] in win:
                    win[s[j]]-=1
                j+=1
            i+=1
        
        print(win)
        print(Counter({'Q': 2, 'W': 1})==Counter({'Q': 1, 'W': 1}))
        return minn if minn>0 else 0