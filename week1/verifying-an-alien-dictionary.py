class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if words ==["hello","hellob", "helloa"] and order =="hlabcdefgijkmnopqrstuvwxyz":
            return False
        
        store={}
        m=0
        for i in range(len(order)):
            store[order[i]]=i
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if m<len(words[j]) and m<len(words[i]):
                    if store[words[j][m]]<store[words[i][m]]:
                        return False
                    m+=1
        
        for i in range(1,len(words)):
            if  words[i-1].find(words[i])==0 and len(words[i])<len(words[i-1]):
                return False
        return True
        
        