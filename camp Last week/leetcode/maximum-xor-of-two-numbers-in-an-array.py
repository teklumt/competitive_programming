class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(2) ]

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if cur.children[int(i)] is None:
                cur.children[int(i)] = TrieNode()
            cur = cur.children[int(i)]
        cur.is_end = True

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        obj = Trie()
        arr = []
        for num in nums:
            bit = bin(num)[2:]
            if len(bit) < 32:
                bit = '0' * (32 - len(bit)) + bit
            arr.append(bit)
      


        for i in arr:
            obj.insert(i)
        
        ans = -inf
        for num in arr:
            res = ""
            cur = obj.root
            for i in num:
                if i == '0':
                    if  cur.children[1]:
                        cur = cur.children[1] 
                        res += '1'
                    else:
                        cur = cur.children[0] 
                        res += '0'

                elif i == '1':
                    if  cur.children[0]:
                        cur = cur.children[0] 
                        res += '1'
                    else:
                        res += '0'
                        cur = cur.children[1] 
            ans = max(ans, int(res, 2))

        return ans
