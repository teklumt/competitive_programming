class MagicDictionary:

    def __init__(self):
        self.store = defaultdict(list)
        
    def buildDict(self, dictionary: List[str]) -> None:
        for i in dictionary:
            self.store[len(i)].append(i)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.store: return
        for word in self.store[len(searchWord)]:
            cnt = 0
            for i in range(len(word)):
                if word[i] != searchWord[i]:
                    cnt += 1
            if cnt == 1: return True
        return 
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)