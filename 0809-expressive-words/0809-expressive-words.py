class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res=0
        store={0:1}
        j=0
        n=list(set(list(s)))
        n.sort()
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                store[j]+=1
            else:
                j+=1
                store[j]=1
        for word in words:
            w=list(set(list(word)))
            w.sort()
            if n!=w:
                continue
            store2={0:1}
            k=0
            for l in range(1,len(word)):
                if word[l]==word[l-1]:
                    store2[k]+=1
                else:
                    k+=1
                    store2[k]=1
            if len(store2)==len(store):
                flag=True
                for i in store.keys():
                    if store[i]<=2:
                        if store[i]!=store2[i]:
                            flag=False
                            break
                    else:
                        if store[i]<store2[i]:
                            flag=False
                            break
                if flag==True:
                    res+=1
        return res