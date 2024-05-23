class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if cur.children[ord(i) - ord('a')] is None:
                cur.children[ord(i) - ord('a')] = TrieNode()
            cur = cur.children[ord(i) - ord('a')]
        cur.is_end = True

        

    def search(self, word: str) -> bool:
        cur = self.root

        cur = cur.children[ord(word[0]) - ord('a')]
        j = 1
        while cur  and j < len(word):
            cur = cur.children[ord(word[j]) - ord('a')]
            j += 1
        

        return  cur.is_end if cur else False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        cur = cur.children[ord(prefix[0]) - ord('a')]
        j = 1
        while cur  and j < len(prefix):
            cur = cur.children[ord(prefix[j]) - ord('a')]
            j += 1
        

        return   j == len(prefix) and cur
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)