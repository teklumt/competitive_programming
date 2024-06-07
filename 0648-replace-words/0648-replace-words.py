class Trie:

    def __init__(self):
        self.root = {'#' : 0}
        

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {'#' : 0}
            cur = cur[i]
        cur['#'] = 1
    def search(self, word):
        cur = self.root
        res = ""
        for i in word:
            if i in cur and not cur['#']:
                res += i
                cur = cur[i]
            else:
                return res if cur['#'] else ""


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        obj = Trie()
        for i in dictionary:
            obj.insert(i)

        ss = sentence.split(" ")
        res = []
        for i in ss:
            ret = obj.search(i)
            res.append(ret if ret else i)
        return " ".join(res)
        