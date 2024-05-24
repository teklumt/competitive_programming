class WordDictionary:

    def __init__(self):
        self.root = {'#' : 0}      

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {'#' : 0}
            cur = cur[i]
        cur['#'] = 1
        
    def search(self, word: str) -> bool:
        cur  = self.root

        def Find(i, cur):
            if i == len(word):
                return cur['#']
            if word[i] !='.' and word[i] not in cur:
                return False
            if word[i] != '.':
               
                return Find(i + 1, cur[word[i]])
            else:
                ans = 0
                for j in cur:
                    if j != '#':
                        ans = ans | Find(i + 1, cur[j])
                return ans
        return Find(0, cur)

    
     

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)