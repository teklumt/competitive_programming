class Trie:
    def __init__(self):
        self.root = {'#' : 0}
    
    def insert(self, word):
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {'#' : 0}
            cur = cur[i]
        cur['#'] = 1

    def search(self, word):
        cur = self.root
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        return cur['#']
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        obj = Trie()
        for i in words:
            if len(i) == 1 or obj.search(i[:-1]):
                obj.insert(i)
        res  = ""
        for i in words:
            if len(i) == 1 or obj.search(i[:-1]):
                if len(res) < len(i): 
                    res = i
                elif len(res) == len(i): 
                    res = min(res, i)
        return res
                
                
        

        